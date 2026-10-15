# ieinstal.exe

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `2cf44880a0da18c284d20ce9049bd76007ae5eaf046cf2ddfdadf7ff5f7a649c` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/ieinstal.exe`
- Bytes: 492,032
- SHA-256: `2cf44880a0da18c284d20ce9049bd76007ae5eaf046cf2ddfdadf7ff5f7a649c`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x14000fa70` (RVA `0xfa70`)
- ImageBase: `0x140000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`, `TERMINAL_SERVER_AWARE`
- Timestamp field: `2019-12-17T00:29:22Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `ieinstal.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0xfb94 | 0xfc00 | `0x140001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x7bc | 0x200 | `0x140011000` | 0x10000 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x8ac | 0xa00 | `0x140012000` | 0x10200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x1c26 | 0x1e00 | `0x140013000` | 0x10c00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x650e0 | 0x65200 | `0x140015000` | 0x12a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x49c | 0x600 | `0x14007b000` | 0x77c00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Import` | `0x136a8` | 0x104 |
| `Resource` | `0x15000` | 0x650e0 |
| `Exception` | `0x12000` | 0x8ac |
| `BaseReloc` | `0x7b000` | 0x49c |
| `Debug` | `0x1170` | 0x1c |
| `LoadConfig` | `0x3fe0` | 0x94 |
| `IAT` | `0x13000` | 0x6a0 |

## Static imports

- `ADVAPI32.dll`: 40 imports
- `AUTHZ.dll`: 5 imports
- `iertutil.dll`: 6 imports
- `KERNEL32.dll`: 76 imports
- `msvcrt.dll`: 32 imports
- `ntdll.dll`: 4 imports
- `ole32.dll`: 14 imports
- `OLEAUT32.dll`: 7 imports
- `RPCRT4.dll`: 3 imports
- `urlmon.dll`: 6 imports
- `USER32.dll`: 3 imports
- `WINTRUST.dll`: 4 imports

## Delay-load imports

- None recovered.

## Exports

none recovered

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/ieinstal.exe.objdump.txt` and `analysis/report/generated/pe-struct.json`.
