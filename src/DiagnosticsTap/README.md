# DiagnosticsTap.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `92ca2180dc18f21bb9b394bbb3bbff040d90564e3d984b13bd6d7a3f24b359eb` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/DiagnosticsTap.dll`
- Bytes: 244,224
- SHA-256: `92ca2180dc18f21bb9b394bbb3bbff040d90564e3d984b13bd6d7a3f24b359eb`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x18002b460` (RVA `0x2b460`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T00:40:47Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `DiagnosticsTap.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x341b0 | 0x34200 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x1170 | 0xa00 | `0x180036000` | 0x34600 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x2094 | 0x2200 | `0x180038000` | 0x35000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x1948 | 0x1a00 | `0x18003b000` | 0x37200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x27a8 | 0x2800 | `0x18003d000` | 0x38c00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x5d0 | 0x600 | `0x180040000` | 0x3b400 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x350f0` | 0xc0 |
| `Import` | `0x3b610` | 0xb4 |
| `Resource` | `0x3d000` | 0x27a8 |
| `Exception` | `0x38000` | 0x2094 |
| `BaseReloc` | `0x40000` | 0x5d0 |
| `Debug` | `0x15e0` | 0x1c |
| `LoadConfig` | `0x6840` | 0x94 |
| `IAT` | `0x3b000` | 0x608 |

## Static imports

- `ADVAPI32.dll`: 28 imports
- `KERNEL32.dll`: 68 imports
- `msvcrt.dll`: 46 imports
- `ole32.dll`: 5 imports
- `OLEAUT32.dll`: 14 imports
- `SHLWAPI.dll`: 2 imports
- `urlmon.dll`: 2 imports
- `USER32.dll`: 20 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllInstall`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/DiagnosticsTap.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
