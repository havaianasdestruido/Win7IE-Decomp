# iexplore.exe

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `cff801d6dc847bb832d0077ce38ddb66ef5b4637ff947bbdbc228eef10494f97` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/iexplore.exe`
- Bytes: 810,376
- SHA-256: `cff801d6dc847bb832d0077ce38ddb66ef5b4637ff947bbdbc228eef10494f97`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x1400019f0` (RVA `0x19f0`)
- ImageBase: `0x140000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`, `TERMINAL_SERVER_AWARE`
- Timestamp field: `2019-12-16T23:36:35Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `iexplore.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x3c70 | 0x3e00 | `0x140001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x7e8 | 0x800 | `0x140005000` | 0x4200 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x4a4 | 0x600 | `0x140006000` | 0x4a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0xc58 | 0xe00 | `0x140007000` | 0x5000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.didat` | 0x30 | 0x200 | `0x140008000` | 0x5e00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.rsrc` | 0xbd848 | 0xbda00 | `0x140009000` | 0x6000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x60 | 0x200 | `0x1400c7000` | 0xc3a00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Import` | `0x72d8` | 0xa0 |
| `Resource` | `0x9000` | 0xbd848 |
| `Exception` | `0x6000` | 0x4a4 |
| `Security` | `0xc3c00` | 0x2188 |
| `BaseReloc` | `0xc7000` | 0x60 |
| `Debug` | `0x46c0` | 0x38 |
| `LoadConfig` | `0x2600` | 0x94 |
| `IAT` | `0x7000` | 0x2d0 |
| `DelayImport` | `0x4610` | 0x40 |

## Static imports

- `api-ms-win-downlevel-advapi32-l1-1-0.dll`: 8 imports
- `api-ms-win-downlevel-shell32-l1-1-0.dll`: 2 imports
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll`: 1 imports
- `iertutil.dll`: 7 imports
- `KERNEL32.dll`: 39 imports
- `msvcrt.dll`: 20 imports
- `USER32.dll`: 6 imports

## Delay-load imports

- `IEFRAME.dll`: 5 delay-load imports

## Exports

none recovered

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/iexplore.exe.objdump.txt` and `analysis/report/generated/pe-struct.json`.
