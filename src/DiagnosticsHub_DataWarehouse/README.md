# DiagnosticsHub.DataWarehouse.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `d6371d20de031d63297012546fd04767b55866beacd1f56600786991c3fa3344` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/DiagnosticsHub.DataWarehouse.dll`
- Bytes: 666,624
- SHA-256: `d6371d20de031d63297012546fd04767b55866beacd1f56600786991c3fa3344`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180069330` (RVA `0x69330`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T01:07:58Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `DiagnosticsHub.DataWarehouse.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x980c5 | 0x98200 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x4798 | 0x2400 | `0x18009a000` | 0x98600 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x59a0 | 0x5a00 | `0x18009f000` | 0x9aa00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x1198 | 0x1200 | `0x1800a5000` | 0xa0400 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x460 | 0x600 | `0x1800a7000` | 0xa1600 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0xee4 | 0x1000 | `0x1800a8000` | 0xa1c00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0x99060` | RVA | 0x65 |
| `Import` | `0xa5408` | RVA | 0x64 |
| `Resource` | `0xa7000` | RVA | 0x460 |
| `Exception` | `0x9f000` | RVA | 0x59a0 |
| `BaseReloc` | `0xa8000` | RVA | 0xee4 |
| `Debug` | `0x1e50` | RVA | 0x1c |
| `LoadConfig` | `0x10140` | RVA | 0x94 |
| `IAT` | `0xa5000` | RVA | 0x400 |

## Static imports

- `KERNEL32.dll`: 115 imports
- `ole32.dll`: 2 imports
- `OLEAUT32.dll`: 6 imports
- `USER32.dll`: 1 imports

## Delay-load imports

- None recovered.

## Exports

`DllGetClassObject`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/DiagnosticsHub.DataWarehouse.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
