#!/usr/bin/env python3
"""Stdlib PE/COFF structural parser used by the Phase 0 inventory.

The parser reads bytes only. It never writes the input path. Field names follow
the Microsoft PE/COFF specification; flag lists are decoded from well-known
bitmasks and are not behavioral claims.
"""
from __future__ import annotations

import json
import struct
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

DOS_MAGIC = b"MZ"
PE_SIGNATURE = b"PE\x00\x00"
PE32_MAGIC = 0x10B
PE32PLUS_MAGIC = 0x20B

MACHINE_NAMES = {
    0x14C: "IMAGE_FILE_MACHINE_I386",
    0x8664: "IMAGE_FILE_MACHINE_AMD64",
    0x1C0: "IMAGE_FILE_MACHINE_ARM",
    0xAA64: "IMAGE_FILE_MACHINE_ARM64",
}

SUBSYSTEM_NAMES = {
    0: "IMAGE_SUBSYSTEM_UNKNOWN",
    1: "IMAGE_SUBSYSTEM_NATIVE",
    2: "IMAGE_SUBSYSTEM_WINDOWS_GUI",
    3: "IMAGE_SUBSYSTEM_WINDOWS_CUI",
    7: "IMAGE_SUBSYSTEM_POSIX_CUI",
    9: "IMAGE_SUBSYSTEM_WINDOWS_CE_GUI",
    10: "IMAGE_SUBSYSTEM_EFI_APPLICATION",
}

DATA_DIRECTORY_NAMES = [
    "Export",
    "Import",
    "Resource",
    "Exception",
    "Security",
    "BaseReloc",
    "Debug",
    "Architecture",
    "GlobalPtr",
    "TLS",
    "LoadConfig",
    "BoundImport",
    "IAT",
    "DelayImport",
    "CLR",
    "Reserved",
]

DEBUG_TYPE_NAMES = {
    0: "IMAGE_DEBUG_TYPE_UNKNOWN",
    1: "IMAGE_DEBUG_TYPE_COFF",
    2: "IMAGE_DEBUG_TYPE_CODEVIEW",
    3: "IMAGE_DEBUG_TYPE_FPO",
    4: "IMAGE_DEBUG_TYPE_MISC",
    5: "IMAGE_DEBUG_TYPE_EXCEPTION",
    6: "IMAGE_DEBUG_TYPE_FIXUP",
    9: "IMAGE_DEBUG_TYPE_BORLAND",
    10: "IMAGE_DEBUG_TYPE_RESERVED10",
    12: "IMAGE_DEBUG_TYPE_CLSID",
    16: "IMAGE_DEBUG_TYPE_REPRO",
}

COFF_CHARACTERISTICS = [
    (0x0001, "RELOCS_STRIPPED"),
    (0x0002, "EXECUTABLE_IMAGE"),
    (0x0004, "LINE_NUMS_STRIPPED"),
    (0x0008, "LOCAL_SYMS_STRIPPED"),
    (0x0020, "LARGE_ADDRESS_AWARE"),
    (0x0100, "32BIT_MACHINE"),
    (0x0200, "DEBUG_STRIPPED"),
    (0x0400, "REMOVABLE_RUN_FROM_SWAP"),
    (0x0800, "NET_RUN_FROM_SWAP"),
    (0x1000, "SYSTEM"),
    (0x2000, "DLL"),
    (0x4000, "UP_SYSTEM_ONLY"),
]

DLL_CHARACTERISTICS = [
    (0x0020, "HIGH_ENTROPY_VA"),
    (0x0040, "DYNAMIC_BASE"),
    (0x0080, "FORCE_INTEGRITY"),
    (0x0100, "NX_COMPAT"),
    (0x0200, "NO_ISOLATION"),
    (0x0400, "NO_SEH"),
    (0x0800, "NO_BIND"),
    (0x1000, "APPCONTAINER"),
    (0x2000, "WDM_DRIVER"),
    (0x4000, "GUARD_CF"),
    (0x8000, "TERMINAL_SERVER_AWARE"),
]

SECTION_CHARACTERISTICS = [
    (0x00000020, "CNT_CODE"),
    (0x00000040, "CNT_INITIALIZED_DATA"),
    (0x00000080, "CNT_UNINITIALIZED_DATA"),
    (0x02000000, "MEM_DISCARDABLE"),
    (0x04000000, "MEM_NOT_CACHED"),
    (0x08000000, "MEM_NOT_PAGED"),
    (0x10000000, "MEM_SHARED"),
    (0x20000000, "MEM_EXECUTE"),
    (0x40000000, "MEM_READ"),
    (0x80000000, "MEM_WRITE"),
]


def _flags(value: int, table: list[tuple[int, str]]) -> list[str]:
    return [name for bit, name in table if value & bit]


def _u16(data: bytes, off: int) -> int:
    return struct.unpack_from("<H", data, off)[0]


def _u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]


def _u64(data: bytes, off: int) -> int:
    return struct.unpack_from("<Q", data, off)[0]


def _cstring(data: bytes, off: int, limit: int = 512) -> str:
    end = data.find(b"\x00", off, off + limit)
    if end < 0:
        end = min(len(data), off + limit)
    return data[off:end].decode("ascii", errors="replace")


def _guid_rsds(raw: bytes) -> str:
    data1, data2, data3 = struct.unpack_from("<IHH", raw, 0)
    data4 = raw[8:16]
    return f"{{{data1:08x}-{data2:04x}-{data3:04x}-{data4[0]:02x}{data4[1]:02x}-{data4[2:].hex()}}}"


@dataclass
class DataDirectory:
    name: str
    rva: int
    size: int


@dataclass
class Section:
    name: str
    virtual_size: int
    virtual_address: int
    size_of_raw_data: int
    pointer_to_raw_data: int
    characteristics: int
    characteristics_names: list[str]


@dataclass
class ImportedSymbol:
    dll: str
    name: str | None
    hint: int | None
    ordinal: int | None
    by_ordinal: bool
    delayed: bool = False

    def display(self) -> str:
        if self.by_ordinal or not self.name:
            return f"ordinal:{self.ordinal}"
        return self.name


@dataclass
class ExportedSymbol:
    name: str | None
    ordinal: int
    rva: int
    forwarder: str | None

    def display(self) -> str:
        if self.name:
            return self.name
        return f"ordinal:{self.ordinal}"


@dataclass
class DebugRecord:
    type: int
    type_name: str
    size: int
    rva: int
    pointer: int
    pdb_path: str | None = None
    guid: str | None = None
    age: int | None = None


@dataclass
class PeImage:
    format: str
    machine: int
    machine_name: str
    section_count: int
    timestamp: int
    characteristics: int
    characteristics_names: list[str]
    magic: int
    linker_version: str
    size_of_code: int
    size_of_initialized_data: int
    size_of_uninitialized_data: int
    address_of_entry_point: int
    base_of_code: int
    image_base: int
    section_alignment: int
    file_alignment: int
    os_version: str
    image_version: str
    subsystem_version: str
    size_of_image: int
    size_of_headers: int
    checksum: int
    subsystem: int
    subsystem_name: str
    dll_characteristics: int
    dll_characteristics_names: list[str]
    size_of_stack_reserve: int
    size_of_stack_commit: int
    size_of_heap_reserve: int
    size_of_heap_commit: int
    number_of_rva_and_sizes: int
    data_directories: list[DataDirectory] = field(default_factory=list)
    sections: list[Section] = field(default_factory=list)
    imports: list[ImportedSymbol] = field(default_factory=list)
    delay_imports: list[ImportedSymbol] = field(default_factory=list)
    exports: list[ExportedSymbol] = field(default_factory=list)
    debug: list[DebugRecord] = field(default_factory=list)
    clr_directory: DataDirectory | None = None

    @property
    def is_pe32plus(self) -> bool:
        return self.magic == PE32PLUS_MAGIC

    @property
    def is_dll(self) -> bool:
        return "DLL" in self.characteristics_names

    @property
    def has_clr(self) -> bool:
        return bool(self.clr_directory and self.clr_directory.rva and self.clr_directory.size)

    def entry_point_va(self) -> int:
        return self.image_base + self.address_of_entry_point

    def imports_by_dll(self, delayed: bool = False) -> dict[str, list[ImportedSymbol]]:
        src = self.delay_imports if delayed else self.imports
        grouped: dict[str, list[ImportedSymbol]] = {}
        for item in src:
            grouped.setdefault(item.dll, []).append(item)
        return grouped

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["entry_point_va"] = f"0x{self.entry_point_va():x}"
        payload["image_base_hex"] = f"0x{self.image_base:x}"
        payload["has_clr"] = self.has_clr
        return payload


class PeError(ValueError):
    pass


class _Reader:
    def __init__(self, data: bytes, image: PeImage):
        self.data = data
        self.image = image

    def rva_to_off(self, rva: int) -> int | None:
        if rva == 0:
            return None
        if rva < self.image.size_of_headers:
            return rva
        for section in self.image.sections:
            span = max(section.virtual_size, section.size_of_raw_data)
            if section.virtual_address <= rva < section.virtual_address + span:
                delta = rva - section.virtual_address
                off = section.pointer_to_raw_data + delta
                if 0 <= off < len(self.data):
                    return off
                return None
        return None

    def u16_rva(self, rva: int) -> int:
        off = self.rva_to_off(rva)
        if off is None:
            raise PeError(f"RVA 0x{rva:x} is not mapped")
        return _u16(self.data, off)

    def u32_rva(self, rva: int) -> int:
        off = self.rva_to_off(rva)
        if off is None:
            raise PeError(f"RVA 0x{rva:x} is not mapped")
        return _u32(self.data, off)

    def cstring_rva(self, rva: int) -> str:
        off = self.rva_to_off(rva)
        if off is None:
            return ""
        return _cstring(self.data, off)

    def slice_rva(self, rva: int, size: int) -> bytes:
        off = self.rva_to_off(rva)
        if off is None:
            return b""
        return self.data[off : off + size]


def parse_pe(data: bytes) -> PeImage:
    if data[:2] != DOS_MAGIC:
        raise PeError("not a DOS/MZ image")
    if len(data) < 0x40:
        raise PeError("truncated DOS header")
    e_lfanew = _u32(data, 0x3C)
    if e_lfanew + 24 > len(data) or data[e_lfanew : e_lfanew + 4] != PE_SIGNATURE:
        raise PeError("missing PE signature")

    coff = e_lfanew + 4
    machine = _u16(data, coff)
    section_count = _u16(data, coff + 2)
    timestamp = _u32(data, coff + 4)
    size_of_optional = _u16(data, coff + 16)
    characteristics = _u16(data, coff + 18)
    opt = coff + 20
    if opt + size_of_optional > len(data):
        raise PeError("truncated optional header")

    magic = _u16(data, opt)
    if magic not in (PE32_MAGIC, PE32PLUS_MAGIC):
        raise PeError(f"unsupported optional-header magic 0x{magic:x}")
    pe32plus = magic == PE32PLUS_MAGIC

    linker_version = f"{data[opt + 2]}.{data[opt + 3]}"
    size_of_code = _u32(data, opt + 4)
    size_of_initialized_data = _u32(data, opt + 8)
    size_of_uninitialized_data = _u32(data, opt + 12)
    address_of_entry_point = _u32(data, opt + 16)
    base_of_code = _u32(data, opt + 20)

    if pe32plus:
        image_base = _u64(data, opt + 24)
    else:
        image_base = _u32(data, opt + 28)

    # PE32 and PE32+ share the next fields after ImageBase, but PE32 inserts BaseOfData.
    base = opt + (24 if pe32plus else 28) + (8 if pe32plus else 4)
    section_alignment = _u32(data, base)
    file_alignment = _u32(data, base + 4)
    os_version = f"{_u16(data, base + 8)}.{_u16(data, base + 10)}"
    image_version = f"{_u16(data, base + 12)}.{_u16(data, base + 14)}"
    subsystem_version = f"{_u16(data, base + 16)}.{_u16(data, base + 18)}"
    size_of_image = _u32(data, base + 24)
    size_of_headers = _u32(data, base + 28)
    checksum = _u32(data, base + 32)
    subsystem = _u16(data, base + 36)
    dll_characteristics = _u16(data, base + 38)

    if pe32plus:
        stack_reserve = _u64(data, base + 40)
        stack_commit = _u64(data, base + 48)
        heap_reserve = _u64(data, base + 56)
        heap_commit = _u64(data, base + 64)
        number_of_rva_and_sizes = _u32(data, base + 76)
        dirs_off = base + 80
    else:
        stack_reserve = _u32(data, base + 40)
        stack_commit = _u32(data, base + 44)
        heap_reserve = _u32(data, base + 48)
        heap_commit = _u32(data, base + 52)
        number_of_rva_and_sizes = _u32(data, base + 60)
        dirs_off = base + 64

    directories: list[DataDirectory] = []
    for i in range(min(number_of_rva_and_sizes, 16)):
        rva = _u32(data, dirs_off + i * 8)
        size = _u32(data, dirs_off + i * 8 + 4)
        name = DATA_DIRECTORY_NAMES[i] if i < len(DATA_DIRECTORY_NAMES) else f"Directory{i}"
        directories.append(DataDirectory(name=name, rva=rva, size=size))

    section_off = opt + size_of_optional
    sections: list[Section] = []
    for i in range(section_count):
        rec = section_off + i * 40
        if rec + 40 > len(data):
            raise PeError("truncated section table")
        raw_name = data[rec : rec + 8].split(b"\x00", 1)[0]
        name = raw_name.decode("ascii", errors="replace")
        characteristics_s = _u32(data, rec + 36)
        sections.append(
            Section(
                name=name,
                virtual_size=_u32(data, rec + 8),
                virtual_address=_u32(data, rec + 12),
                size_of_raw_data=_u32(data, rec + 16),
                pointer_to_raw_data=_u32(data, rec + 20),
                characteristics=characteristics_s,
                characteristics_names=_flags(characteristics_s, SECTION_CHARACTERISTICS),
            )
        )

    clr = directories[14] if len(directories) > 14 else None
    image = PeImage(
        format="PE32+" if pe32plus else "PE32",
        machine=machine,
        machine_name=MACHINE_NAMES.get(machine, f"MACHINE_0x{machine:x}"),
        section_count=section_count,
        timestamp=timestamp,
        characteristics=characteristics,
        characteristics_names=_flags(characteristics, COFF_CHARACTERISTICS),
        magic=magic,
        linker_version=linker_version,
        size_of_code=size_of_code,
        size_of_initialized_data=size_of_initialized_data,
        size_of_uninitialized_data=size_of_uninitialized_data,
        address_of_entry_point=address_of_entry_point,
        base_of_code=base_of_code,
        image_base=image_base,
        section_alignment=section_alignment,
        file_alignment=file_alignment,
        os_version=os_version,
        image_version=image_version,
        subsystem_version=subsystem_version,
        size_of_image=size_of_image,
        size_of_headers=size_of_headers,
        checksum=checksum,
        subsystem=subsystem,
        subsystem_name=SUBSYSTEM_NAMES.get(subsystem, f"SUBSYSTEM_{subsystem}"),
        dll_characteristics=dll_characteristics,
        dll_characteristics_names=_flags(dll_characteristics, DLL_CHARACTERISTICS),
        size_of_stack_reserve=stack_reserve,
        size_of_stack_commit=stack_commit,
        size_of_heap_reserve=heap_reserve,
        size_of_heap_commit=heap_commit,
        number_of_rva_and_sizes=number_of_rva_and_sizes,
        data_directories=directories,
        sections=sections,
        clr_directory=clr if clr and clr.rva else None,
    )

    reader = _Reader(data, image)
    image.imports = _parse_import_table(reader, delayed=False)
    image.delay_imports = _parse_delay_import_table(reader)
    image.exports = _parse_export_table(reader)
    image.debug = _parse_debug_directory(reader)
    return image


def parse_pe_path(path: Path) -> PeImage:
    return parse_pe(path.read_bytes())


def _parse_thunk_symbols(reader: _Reader, thunk_rva: int, dll: str, delayed: bool) -> list[ImportedSymbol]:
    image = reader.image
    width = 8 if image.is_pe32plus else 4
    ordinal_bit = 1 << (63 if image.is_pe32plus else 31)
    symbols: list[ImportedSymbol] = []
    index = 0
    while True:
        off = reader.rva_to_off(thunk_rva + index * width)
        if off is None:
            break
        thunk = _u64(reader.data, off) if width == 8 else _u32(reader.data, off)
        if thunk == 0:
            break
        if thunk & ordinal_bit:
            ordinal = thunk & 0xFFFF
            symbols.append(
                ImportedSymbol(
                    dll=dll,
                    name=None,
                    hint=None,
                    ordinal=ordinal,
                    by_ordinal=True,
                    delayed=delayed,
                )
            )
        else:
            name_rva = thunk & 0x7FFFFFFF
            name_off = reader.rva_to_off(name_rva)
            if name_off is None:
                symbols.append(
                    ImportedSymbol(
                        dll=dll,
                        name=None,
                        hint=None,
                        ordinal=None,
                        by_ordinal=False,
                        delayed=delayed,
                    )
                )
            else:
                hint = _u16(reader.data, name_off)
                name = _cstring(reader.data, name_off + 2)
                symbols.append(
                    ImportedSymbol(
                        dll=dll,
                        name=name,
                        hint=hint,
                        ordinal=None,
                        by_ordinal=False,
                        delayed=delayed,
                    )
                )
        index += 1
        if index > 4096:
            break
    return symbols


def _parse_import_table(reader: _Reader, delayed: bool) -> list[ImportedSymbol]:
    directory = next((d for d in reader.image.data_directories if d.name == "Import"), None)
    if not directory or not directory.rva or not directory.size:
        return []
    symbols: list[ImportedSymbol] = []
    desc_rva = directory.rva
    for _ in range(512):
        off = reader.rva_to_off(desc_rva)
        if off is None:
            break
        original_first_thunk = _u32(reader.data, off)
        name_rva = _u32(reader.data, off + 12)
        first_thunk = _u32(reader.data, off + 16)
        if original_first_thunk == 0 and name_rva == 0 and first_thunk == 0:
            break
        dll = reader.cstring_rva(name_rva) or "unknown.dll"
        thunk = original_first_thunk or first_thunk
        symbols.extend(_parse_thunk_symbols(reader, thunk, dll, delayed=delayed))
        desc_rva += 20
    return symbols


def _parse_delay_import_table(reader: _Reader) -> list[ImportedSymbol]:
    directory = next((d for d in reader.image.data_directories if d.name == "DelayImport"), None)
    if not directory or not directory.rva or not directory.size:
        return []
    symbols: list[ImportedSymbol] = []
    desc_rva = directory.rva
    for _ in range(64):
        off = reader.rva_to_off(desc_rva)
        if off is None:
            break
        attrs = _u32(reader.data, off)
        name_val = _u32(reader.data, off + 4)
        int_rva = _u32(reader.data, off + 16)
        iat_rva = _u32(reader.data, off + 12)
        if attrs == 0 and name_val == 0 and int_rva == 0 and iat_rva == 0:
            break
        # Modern descriptors store RVAs; the legacy VC6 form stored VAs.
        name_rva = name_val if attrs & 1 or name_val < reader.image.size_of_image else name_val - reader.image.image_base
        thunk = int_rva or iat_rva
        if attrs & 1 == 0 and thunk > reader.image.size_of_image:
            thunk -= reader.image.image_base
        dll = reader.cstring_rva(name_rva) or "unknown.dll"
        symbols.extend(_parse_thunk_symbols(reader, thunk, dll, delayed=True))
        desc_rva += 32
    return symbols


def _parse_export_table(reader: _Reader) -> list[ExportedSymbol]:
    directory = next((d for d in reader.image.data_directories if d.name == "Export"), None)
    if not directory or not directory.rva or not directory.size:
        return []
    off = reader.rva_to_off(directory.rva)
    if off is None:
        return []
    ordinal_base = _u32(reader.data, off + 16)
    number_of_functions = _u32(reader.data, off + 20)
    number_of_names = _u32(reader.data, off + 24)
    addr_functions = _u32(reader.data, off + 28)
    addr_names = _u32(reader.data, off + 32)
    addr_ordinals = _u32(reader.data, off + 36)
    if number_of_functions > 8192 or number_of_names > 8192:
        return []

    names: dict[int, str] = {}
    for i in range(number_of_names):
        name_rva = reader.u32_rva(addr_names + i * 4)
        ordinal_index = reader.u16_rva(addr_ordinals + i * 2)
        names[ordinal_index] = reader.cstring_rva(name_rva)

    exports: list[ExportedSymbol] = []
    export_begin = directory.rva
    export_end = directory.rva + directory.size
    for idx in range(number_of_functions):
        rva = reader.u32_rva(addr_functions + idx * 4)
        if rva == 0:
            continue
        forwarder = None
        if export_begin <= rva < export_end:
            forwarder = reader.cstring_rva(rva)
        exports.append(
            ExportedSymbol(
                name=names.get(idx),
                ordinal=ordinal_base + idx,
                rva=rva,
                forwarder=forwarder,
            )
        )
    exports.sort(key=lambda item: (item.name or "", item.ordinal))
    return exports


def _parse_debug_directory(reader: _Reader) -> list[DebugRecord]:
    directory = next((d for d in reader.image.data_directories if d.name == "Debug"), None)
    if not directory or not directory.rva or not directory.size:
        return []
    records: list[DebugRecord] = []
    count = directory.size // 28
    for i in range(count):
        off = reader.rva_to_off(directory.rva + i * 28)
        if off is None:
            continue
        dtype = _u32(reader.data, off + 12)
        size = _u32(reader.data, off + 16)
        rva = _u32(reader.data, off + 20)
        pointer = _u32(reader.data, off + 24)
        rec = DebugRecord(
            type=dtype,
            type_name=DEBUG_TYPE_NAMES.get(dtype, f"DEBUG_TYPE_{dtype}"),
            size=size,
            rva=rva,
            pointer=pointer,
        )
        blob = b""
        if 0 < pointer < len(reader.data):
            blob = reader.data[pointer : pointer + size]
        elif rva:
            blob = reader.slice_rva(rva, size)
        if blob.startswith(b"RSDS") and len(blob) >= 24:
            rec.guid = _guid_rsds(blob[4:20])
            rec.age = _u32(blob, 20)
            rec.pdb_path = _cstring(blob, 24, limit=len(blob) - 24)
        records.append(rec)
    return records


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if not args:
        print("usage: pe.py <image> [<image> ...]", file=sys.stderr)
        return 2
    payload = []
    for raw in args:
        path = Path(raw)
        image = parse_pe_path(path)
        payload.append({"path": str(path), **image.to_dict()})
    json.dump(payload if len(payload) > 1 else payload[0], sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
