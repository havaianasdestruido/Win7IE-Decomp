# ielowutil.exe

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `7099cea38e986d13f1a882a9ccd0ecf5666ff1c6d807abdc4bbe90ab90963769` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/ielowutil.exe`
- Bytes: 222,720
- SHA-256: `7099cea38e986d13f1a882a9ccd0ecf5666ff1c6d807abdc4bbe90ab90963769`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x140002940` (RVA `0x2940`)
- ImageBase: `0x140000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`, `TERMINAL_SERVER_AWARE`
- Timestamp field: `2019-12-17T00:55:29Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `ielowutil.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x20ec | 0x2200 | `0x140001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x714 | 0x200 | `0x140004000` | 0x2600 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x1c8 | 0x200 | `0x140005000` | 0x2800 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0xb6c | 0xc00 | `0x140006000` | 0x2a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x32cb0 | 0x32e00 | `0x140007000` | 0x3600 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x30 | 0x200 | `0x14003a000` | 0x36400 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Import` | `0x62a8` | RVA | 0xa0 |
| `Resource` | `0x7000` | RVA | 0x32cb0 |
| `Exception` | `0x5000` | RVA | 0x1c8 |
| `BaseReloc` | `0x3a000` | RVA | 0x30 |
| `Debug` | `0x1080` | RVA | 0x1c |
| `LoadConfig` | `0x1370` | RVA | 0x94 |
| `IAT` | `0x6000` | RVA | 0x2a0 |

## Static imports

- `iertutil.dll`: 1 imports
- `KERNEL32.dll`: 39 imports
- `msvcrt.dll`: 20 imports
- `ntdll.dll`: 3 imports
- `ole32.dll`: 7 imports
- `USER32.dll`: 5 imports
- `WININET.dll`: 2 imports

## Delay-load imports

- None recovered.

## Exports

none recovered

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/ielowutil.exe.objdump.txt` and `analysis/report/generated/pe-struct.json`.
