# perfcore.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `b41c4d0cb9e42d7d9020184944f05fa23873ad039454a53247691f4b0a0daf7a` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/perfcore.dll`
- Bytes: 161,280
- SHA-256: `b41c4d0cb9e42d7d9020184944f05fa23873ad039454a53247691f4b0a0daf7a`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x18001a5ac` (RVA `0x1a5ac`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2013-10-14T06:41:35Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `perfcore.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x1f280 | 0x1f400 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0xb68 | 0x600 | `0x180021000` | 0x1f800 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x1434 | 0x1600 | `0x180022000` | 0x1fe00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0xabe | 0xc00 | `0x180024000` | 0x21400 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x4d10 | 0x4e00 | `0x180025000` | 0x22000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x652 | 0x800 | `0x18002a000` | 0x26e00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x201e0` | 0xa0 |
| `Import` | `0x24288` | 0x8c |
| `Resource` | `0x25000` | 0x4d10 |
| `Exception` | `0x22000` | 0x1434 |
| `BaseReloc` | `0x2a000` | 0x39c |
| `Debug` | `0x1050` | 0x1c |
| `LoadConfig` | `0x3c40` | 0x94 |
| `IAT` | `0x24000` | 0x288 |

## Static imports

- `ADVAPI32.dll`: 5 imports
- `KERNEL32.dll`: 28 imports
- `msvcrt.dll`: 34 imports
- `ntdll.dll`: 3 imports
- `ole32.dll`: 1 imports
- `OLEAUT32.dll`: 4 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/perfcore.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
