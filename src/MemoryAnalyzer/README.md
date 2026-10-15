# MemoryAnalyzer.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `eeff728c1f190f8febe04ad5312d7bdec285b7fe1bdd1f77684320d51202de3a` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/MemoryAnalyzer.dll`
- Bytes: 1,862,144
- SHA-256: `eeff728c1f190f8febe04ad5312d7bdec285b7fe1bdd1f77684320d51202de3a`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x1801b2700` (RVA `0x1b2700`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T00:50:49Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `MemoryAnalyzer.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x1be3d4 | 0x1be400 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x29d0 | 0x2200 | `0x1801c0000` | 0x1be800 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x2cc4 | 0x2e00 | `0x1801c3000` | 0x1c0a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x1102 | 0x1200 | `0x1801c6000` | 0x1c3800 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x17b8 | 0x1800 | `0x1801c8000` | 0x1c4a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x60c | 0x800 | `0x1801ca000` | 0x1c6200 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0x1bf360` | RVA | 0x74 |
| `Import` | `0x1c6410` | RVA | 0x78 |
| `Resource` | `0x1c8000` | RVA | 0x17b8 |
| `Exception` | `0x1c3000` | RVA | 0x2cc4 |
| `BaseReloc` | `0x1ca000` | RVA | 0x60c |
| `Debug` | `0x13b0` | RVA | 0x1c |
| `LoadConfig` | `0x26440` | RVA | 0x94 |
| `IAT` | `0x1c6000` | RVA | 0x408 |

## Static imports

- `KERNEL32.dll`: 57 imports
- `msvcrt.dll`: 47 imports
- `ole32.dll`: 1 imports
- `OLEAUT32.dll`: 8 imports
- `USER32.dll`: 11 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/MemoryAnalyzer.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
