# ieproxy.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `7bfc8614acfacf4f06887e8e518a5647749a066b0a9832e2edb489022091866c` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/ieproxy.dll`
- Bytes: 805,376
- SHA-256: `7bfc8614acfacf4f06887e8e518a5647749a066b0a9832e2edb489022091866c`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180001ce0` (RVA `0x1ce0`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-16T23:37:15Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `IEProxy.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0xaad34 | 0xaae00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.orpc` | 0x3897 | 0x3a00 | `0x1800ac000` | 0xab200 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x4234 | 0x4200 | `0x1800b0000` | 0xaec00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x1788 | 0x1800 | `0x1800b5000` | 0xb2e00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0xf34 | 0x1000 | `0x1800b7000` | 0xb4600 | CNT_INITIALIZED_DATA, MEM_READ |
| `.didat` | 0x498 | 0x600 | `0x1800b8000` | 0xb5600 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.rsrc` | 0x438 | 0x600 | `0x1800b9000` | 0xb5c00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0xe6d0 | 0xe800 | `0x1800ba000` | 0xb6200 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x3f40` | 0xbe |
| `Import` | `0xb7340` | 0x8c |
| `Resource` | `0xb9000` | 0x438 |
| `Exception` | `0xb5000` | 0x1788 |
| `BaseReloc` | `0xba000` | 0xe6d0 |
| `Debug` | `0xaae8c` | 0x38 |
| `LoadConfig` | `0x3660` | 0x94 |
| `IAT` | `0xb7000` | 0x338 |
| `DelayImport` | `0xa9cf8` | 0x120 |

## Static imports

- `api-ms-win-downlevel-advapi32-l1-1-0.dll`: 6 imports
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll`: 7 imports
- `api-ms-win-downlevel-shlwapi-l2-1-0.dll`: 2 imports
- `KERNEL32.dll`: 39 imports
- `msvcrt.dll`: 18 imports
- `RPCRT4.dll`: 25 imports

## Delay-load imports

- `api-ms-win-downlevel-ole32-l1-1-0.dll`: 2 delay-load imports
- `GDI32.dll`: 10 delay-load imports
- `iertutil.dll`: 3 delay-load imports
- `ole32.dll`: 88 delay-load imports
- `OLEAUT32.dll`: 27 delay-load imports
- `PROPSYS.dll`: 2 delay-load imports
- `SHELL32.dll`: 2 delay-load imports
- `USER32.dll`: 5 delay-load imports

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`, `GetProxyDllInfo`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/ieproxy.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
