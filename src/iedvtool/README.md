# iedvtool.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `f188b636065cfa5bdae6c6c4b2ae3fe1df7ff2b700c2144b1291dee7f5f9f912` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/iedvtool.dll`
- Bytes: 950,784
- SHA-256: `f188b636065cfa5bdae6c6c4b2ae3fe1df7ff2b700c2144b1291dee7f5f9f912`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180099490` (RVA `0x99490`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T02:39:52Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `iedvtool.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0xae4c5 | 0xae600 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0xeac | 0x600 | `0x1800b0000` | 0xaea00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x55ec | 0x5600 | `0x1800b1000` | 0xaf000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x398a | 0x3a00 | `0x1800b7000` | 0xb4600 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x2e8e0 | 0x2ea00 | `0x1800bb000` | 0xb8000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x1770 | 0x1800 | `0x1800ea000` | 0xe6a00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0xaf420` | 0xa5 |
| `Import` | `0xb7e98` | 0x168 |
| `Resource` | `0xbb000` | 0x2e8e0 |
| `Exception` | `0xb1000` | 0x55ec |
| `BaseReloc` | `0xea000` | 0x1770 |
| `Debug` | `0x2310` | 0x1c |
| `LoadConfig` | `0x101a0` | 0x94 |
| `IAT` | `0xb7000` | 0xe90 |

## Static imports

- `ADVAPI32.dll`: 10 imports
- `GDI32.dll`: 36 imports
- `IEFRAME.dll`: 9 imports
- `iertutil.dll`: 22 imports
- `KERNEL32.dll`: 95 imports
- `MSHTML.dll`: 1 imports
- `MSIMG32.dll`: 2 imports
- `msvcrt.dll`: 55 imports
- `ole32.dll`: 12 imports
- `OLEACC.dll`: 2 imports
- `OLEAUT32.dll`: 17 imports
- `SHELL32.dll`: 3 imports
- `SHLWAPI.dll`: 20 imports
- `urlmon.dll`: 10 imports
- `USER32.dll`: 140 imports
- `UxTheme.dll`: 1 imports
- `WININET.dll`: 14 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/iedvtool.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
