# jsprofilerui.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `2dce1ffc22f877cb632dda8dc0fd662d1ad0bad08c72420ab0a08f54f7c911bf` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/jsprofilerui.dll`
- Bytes: 628,736
- SHA-256: `2dce1ffc22f877cb632dda8dc0fd662d1ad0bad08c72420ab0a08f54f7c911bf`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180027260` (RVA `0x27260`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T00:32:40Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `jsprofilerui.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x2c524 | 0x2c600 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0xadc | 0x400 | `0x18002e000` | 0x2ca00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x1b9c | 0x1c00 | `0x18002f000` | 0x2ce00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x21ac | 0x2200 | `0x180031000` | 0x2ea00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x685f8 | 0x68600 | `0x180034000` | 0x30c00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x554 | 0x600 | `0x18009d000` | 0x99200 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x2d4d0` | 0x54 |
| `Import` | `0x31850` | 0xf0 |
| `Resource` | `0x34000` | 0x685f8 |
| `Exception` | `0x2f000` | 0x1b9c |
| `BaseReloc` | `0x9d000` | 0x554 |
| `Debug` | `0x14b0` | 0x1c |
| `LoadConfig` | `0x49a0` | 0x94 |
| `IAT` | `0x31000` | 0x848 |

## Static imports

- `ADVAPI32.dll`: 7 imports
- `GDI32.dll`: 20 imports
- `iertutil.dll`: 6 imports
- `KERNEL32.dll`: 69 imports
- `msvcrt.dll`: 44 imports
- `ole32.dll`: 4 imports
- `OLEACC.dll`: 2 imports
- `OLEAUT32.dll`: 10 imports
- `SHLWAPI.dll`: 1 imports
- `urlmon.dll`: 1 imports
- `USER32.dll`: 90 imports

## Delay-load imports

- None recovered.

## Exports

`CreateProfileTab`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/jsprofilerui.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
