# pdm.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `ca795fedc2b655890a19f868f145cc6db0aae797e1d6faf7b2b8ed7ac75723a5` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/pdm.dll`
- Bytes: 542,272
- SHA-256: `ca795fedc2b655890a19f868f145cc6db0aae797e1d6faf7b2b8ed7ac75723a5`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180036a54` (RVA `0x36a54`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `12.0`; OS version: `6.0`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2013-07-12T03:42:28Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `pdm.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x51cdf | 0x51e00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.rdata` | 0x252f2 | 0x25400 | `0x180053000` | 0x52200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.data` | 0x4478 | 0x1c00 | `0x180079000` | 0x77600 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x4800 | 0x4800 | `0x18007e000` | 0x79200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x1750 | 0x1800 | `0x180083000` | 0x7da00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x1474 | 0x1600 | `0x180085000` | 0x7f200 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x76d00` | 0xa0 |
| `Import` | `0x76da0` | 0x78 |
| `Resource` | `0x83000` | 0x1750 |
| `Exception` | `0x7e000` | 0x4800 |
| `Security` | `0x80800` | 0x3e40 |
| `BaseReloc` | `0x85000` | 0x1474 |
| `Debug` | `0x53790` | 0x38 |
| `LoadConfig` | `0x65310` | 0x70 |
| `IAT` | `0x53000` | 0x690 |
| `DelayImport` | `0x76bb8` | 0x60 |

## Static imports

- `ADVAPI32.dll`: 33 imports
- `KERNEL32.dll`: 120 imports
- `ole32.dll`: 18 imports
- `OLEAUT32.dll`: 17 imports
- `USER32.dll`: 17 imports

## Delay-load imports

- `VERSION.dll`: 3 delay-load imports
- `WTSAPI32.dll`: 2 delay-load imports

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/pdm.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
