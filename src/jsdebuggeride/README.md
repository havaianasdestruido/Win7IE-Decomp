# jsdebuggeride.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `a4ad21edbb7891e1e89c056b970a67955c2eb1c10aaaf90bc1062869a52b722e` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/jsdebuggeride.dll`
- Bytes: 142,336
- SHA-256: `a4ad21edbb7891e1e89c056b970a67955c2eb1c10aaaf90bc1062869a52b722e`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180019d70` (RVA `0x19d70`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2013-10-14T05:42:51Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `jsdebuggeride.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x1e830 | 0x1ea00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0xa68 | 0x400 | `0x180020000` | 0x1ee00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x1650 | 0x1800 | `0x180021000` | 0x1f200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x1232 | 0x1400 | `0x180023000` | 0x20a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x418 | 0x600 | `0x180025000` | 0x21e00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x7d0 | 0x800 | `0x180026000` | 0x22400 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0x1f7c0` | RVA | 0x70 |
| `Import` | `0x23470` | RVA | 0xc8 |
| `Resource` | `0x25000` | RVA | 0x418 |
| `Exception` | `0x21000` | RVA | 0x1650 |
| `BaseReloc` | `0x26000` | RVA | 0x3b4 |
| `Debug` | `0x1060` | RVA | 0x1c |
| `LoadConfig` | `0x3e00` | RVA | 0x94 |
| `IAT` | `0x23000` | RVA | 0x470 |

## Static imports

- `ADVAPI32.dll`: 8 imports
- `KERNEL32.dll`: 43 imports
- `msvcrt.dll`: 45 imports
- `ole32.dll`: 7 imports
- `OLEAUT32.dll`: 14 imports
- `SHLWAPI.dll`: 1 imports
- `urlmon.dll`: 2 imports
- `USER32.dll`: 6 imports
- `WININET.dll`: 7 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/jsdebuggeride.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
