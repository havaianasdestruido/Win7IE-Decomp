# DiagnosticsHub_is.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `7d75d8efc5107b64c2f0acfc6e7a33937ebacb1027b2c3f96bc1876878185da0` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/DiagnosticsHub_is.dll`
- Bytes: 50,176
- SHA-256: `7d75d8efc5107b64c2f0acfc6e7a33937ebacb1027b2c3f96bc1876878185da0`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180008eb0` (RVA `0x8eb0`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T01:10:36Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `DiagnosticsHub_is.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0xa06e | 0xa200 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x9b0 | 0x400 | `0x18000c000` | 0xa600 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x738 | 0x800 | `0x18000d000` | 0xaa00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x79e | 0x800 | `0x18000e000` | 0xb200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x410 | 0x600 | `0x18000f000` | 0xba00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x32c | 0x400 | `0x180010000` | 0xc000 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0xafc0` | 0xae |
| `Import` | `0xe1c0` | 0x78 |
| `Resource` | `0xf000` | 0x410 |
| `Exception` | `0xd000` | 0x738 |
| `BaseReloc` | `0x10000` | 0x32c |
| `Debug` | `0x11e0` | 0x1c |
| `LoadConfig` | `0x3330` | 0x94 |
| `IAT` | `0xe000` | 0x1b8 |

## Static imports

- `KERNEL32.dll`: 18 imports
- `msvcrt.dll`: 25 imports
- `ole32.dll`: 1 imports
- `OLEAUT32.dll`: 4 imports
- `tdh.dll`: 2 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/DiagnosticsHub_is.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
