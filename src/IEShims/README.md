# IEShims.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `e9b0cfa86136da976a12c4ca981e1be1e9d6e6ec43250c0b4939ddd59732638e` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/IEShims.dll`
- Bytes: 386,560
- SHA-256: `e9b0cfa86136da976a12c4ca981e1be1e9d6e6ec43250c0b4939ddd59732638e`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x1800010e0` (RVA `0x10e0`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-16T23:45:34Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `ieshims.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x559e0 | 0x55a00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x1ce8 | 0x1c00 | `0x180057000` | 0x55e00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x42cc | 0x4400 | `0x180059000` | 0x57a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x15f6 | 0x1600 | `0x18005e000` | 0x5be00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.didat` | 0x138 | 0x200 | `0x180060000` | 0x5d400 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.rsrc` | 0x430 | 0x600 | `0x180061000` | 0x5d600 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x8d4 | 0xa00 | `0x180062000` | 0x5dc00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0xf4ac` | RVA | 0x188 |
| `Import` | `0x5e550` | RVA | 0x8c |
| `Resource` | `0x61000` | RVA | 0x430 |
| `Exception` | `0x59000` | RVA | 0x42cc |
| `BaseReloc` | `0x62000` | RVA | 0x8d4 |
| `Debug` | `0x4987c` | RVA | 0x38 |
| `LoadConfig` | `0xebe0` | RVA | 0x94 |
| `IAT` | `0x5e000` | RVA | 0x548 |
| `DelayImport` | `0x49364` | RVA | 0x100 |

## Static imports

- `api-ms-win-downlevel-advapi32-l1-1-0.dll`: 9 imports
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll`: 11 imports
- `iertutil.dll`: 10 imports
- `KERNEL32.dll`: 90 imports
- `msvcrt.dll`: 41 imports
- `ntdll.dll`: 2 imports

## Delay-load imports

- `ADVAPI32.dll`: 2 delay-load imports
- `api-ms-win-downlevel-ole32-l1-1-0.dll`: 6 delay-load imports
- `credui.dll`: 2 delay-load imports
- `MPR.dll`: 1 delay-load imports
- `OLEAUT32.dll`: 4 delay-load imports
- `SHELL32.dll`: 3 delay-load imports
- `USER32.dll`: 14 delay-load imports

## Exports

`AcRedirNotify`, `AcRedirNotifySetEnabled`, `AcRedirSetEnabled`, `IEShims_AdminCheckAndLaunch`, `IEShims_CreateWindowEx`, `IEShims_GetOriginatingThreadId`, `IEShims_InDllMainContext`, `IEShims_Initialize`, `IEShims_SetRedirectRegistryForThread`, `IEShims_Uninitialize`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/IEShims.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
