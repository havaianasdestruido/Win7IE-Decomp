#!/usr/bin/env python3
"""Regression checks for analysis/tools/pe.py against locked corpus images.

These tests assert structural facts already published in the Phase 0 inventory
(SHA-256, architecture, entry RVA, section names). They read bin/ and never
write it.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pe import parse_pe_path

ROOT = Path(__file__).resolve().parents[2]
BIN = ROOT / "bin"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def expect(cond: bool, message: str, failures: list[str]) -> None:
    if not cond:
        failures.append(message)


def test_iexplore(failures: list[str]) -> None:
    path = BIN / "iexplore.exe"
    expect(sha256(path) == "cff801d6dc847bb832d0077ce38ddb66ef5b4637ff947bbdbc228eef10494f97", "iexplore.exe hash drift", failures)
    image = parse_pe_path(path)
    expect(image.format == "PE32+", "iexplore.exe is PE32+", failures)
    expect(image.machine_name == "IMAGE_FILE_MACHINE_AMD64", "iexplore.exe machine", failures)
    expect(image.address_of_entry_point == 0x19F0, "iexplore.exe entry RVA", failures)
    expect(image.image_base == 0x140000000, "iexplore.exe image base", failures)
    expect(image.subsystem_name == "IMAGE_SUBSYSTEM_WINDOWS_GUI", "iexplore.exe subsystem", failures)
    expect([s.name for s in image.sections] == [".text", ".data", ".pdata", ".idata", ".didat", ".rsrc", ".reloc"], "iexplore.exe sections", failures)
    expect({s.dll for s in image.imports} >= {"KERNEL32.dll", "USER32.dll", "msvcrt.dll"}, "iexplore.exe static imports", failures)
    expect({s.dll for s in image.delay_imports} == {"IEFRAME.dll"}, "iexplore.exe delay-load IEFRAME", failures)
    expect(all(s.by_ordinal for s in image.delay_imports), "iexplore.exe delay-load ordinals", failures)
    pdbs = [d.pdb_path for d in image.debug if d.pdb_path]
    expect(pdbs == ["iexplore.pdb"], "iexplore.exe CodeView PDB name", failures)


def test_iediagcmd(failures: list[str]) -> None:
    path = BIN / "iediagcmd.exe"
    expect(sha256(path) == "412df2da4d524e6b78ed6c7bc595224643574510fba194ee940e495d981a6510", "iediagcmd.exe hash drift", failures)
    image = parse_pe_path(path)
    expect(image.format == "PE32", "iediagcmd.exe is PE32", failures)
    expect(image.machine_name == "IMAGE_FILE_MACHINE_I386", "iediagcmd.exe machine", failures)
    expect(image.has_clr, "iediagcmd.exe CLR directory", failures)
    expect(image.clr_directory is not None and image.clr_directory.rva == 0x2008, "iediagcmd.exe CLR RVA", failures)
    expect(image.clr_directory is not None and image.clr_directory.size == 0x48, "iediagcmd.exe CLR size", failures)
    expect([(s.dll, s.name) for s in image.imports] == [("mscoree.dll", "_CorExeMain")], "iediagcmd.exe import", failures)
    expect([d.pdb_path for d in image.debug if d.pdb_path] == ["IEDiagCmd.pdb"], "iediagcmd.exe PDB", failures)


def test_mui_and_exports(failures: list[str]) -> None:
    mui = parse_pe_path(BIN / "en-US" / "iexplore.exe.mui")
    expect(mui.format == "PE32", "mui format", failures)
    expect(mui.address_of_entry_point == 0, "mui entry is zero", failures)
    expect([s.name for s in mui.sections] == [".rsrc"], "mui has only .rsrc", failures)
    expect(mui.imports == [] and mui.exports == [], "mui has no IAT/EAT", failures)

    shims = parse_pe_path(BIN / "IEShims.dll")
    names = [e.name for e in shims.exports]
    expect(
        names
        == [
            "AcRedirNotify",
            "AcRedirNotifySetEnabled",
            "AcRedirSetEnabled",
            "IEShims_AdminCheckAndLaunch",
            "IEShims_CreateWindowEx",
            "IEShims_GetOriginatingThreadId",
            "IEShims_InDllMainContext",
            "IEShims_Initialize",
            "IEShims_SetRedirectRegistryForThread",
            "IEShims_Uninitialize",
        ],
        "IEShims.dll export names",
        failures,
    )

    sqm = parse_pe_path(BIN / "sqmapi.dll")
    expect(len(sqm.exports) == 63, "sqmapi.dll has 63 exports", failures)
    expect(all(name and name.startswith("Sqm") for name in (e.name for e in sqm.exports)), "sqmapi.dll Sqm* exports", failures)


def main() -> int:
    failures: list[str] = []
    test_iexplore(failures)
    test_iediagcmd(failures)
    test_mui_and_exports(failures)
    if failures:
        print("FAIL")
        for item in failures:
            print(f"  - {item}")
        return 1
    print("ok: pe structural facts hold for iexplore.exe, iediagcmd.exe, MUI, IEShims.dll, sqmapi.dll")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
