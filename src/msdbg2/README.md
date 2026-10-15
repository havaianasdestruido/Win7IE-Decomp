# msdbg2.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `ee4065d7ddfb9e588a81fa1e2a760c01f6e8275581d46381a1ee5e168c38a8d0` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/msdbg2.dll`
- Bytes: 400,968
- SHA-256: `ee4065d7ddfb9e588a81fa1e2a760c01f6e8275581d46381a1ee5e168c38a8d0`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x18000164c` (RVA `0x164c`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `12.0`; OS version: `6.0`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2013-07-12T02:40:34Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `msdbg2.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0xb11b | 0xb200 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.orpc` | 0x1995 | 0x1a00 | `0x18000d000` | 0xb600 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.rdata` | 0x3ee78 | 0x3f000 | `0x18000f000` | 0xd000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.data` | 0xca18 | 0xa800 | `0x18004e000` | 0x4c000 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0xb04 | 0xc00 | `0x18005b000` | 0x56800 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x418 | 0x600 | `0x18005c000` | 0x57400 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x6440 | 0x6600 | `0x18005d000` | 0x57a00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x4d2b0` | 0xa3 |
| `Import` | `0x4d354` | 0x64 |
| `Resource` | `0x5c000` | 0x418 |
| `Exception` | `0x5b000` | 0xb04 |
| `Security` | `0x5e000` | 0x3e48 |
| `BaseReloc` | `0x5d000` | 0x6440 |
| `Debug` | `0xf3b0` | 0x38 |
| `LoadConfig` | `0x4c990` | 0x70 |
| `IAT` | `0xf000` | 0x338 |

## Static imports

- `KERNEL32.dll`: 64 imports
- `ole32.dll`: 4 imports
- `OLEAUT32.dll`: 8 imports
- `RPCRT4.dll`: 23 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/msdbg2.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
