# Timeline_is.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `cc3298491463bf23bae8b0d3d45d0899cfb314f3985aec52911223f58941dd49` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/Timeline_is.dll`
- Bytes: 171,520
- SHA-256: `cc3298491463bf23bae8b0d3d45d0899cfb314f3985aec52911223f58941dd49`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180021450` (RVA `0x21450`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T00:56:45Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `Timeline_is.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x25dc0 | 0x25e00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x1358 | 0xc00 | `0x180027000` | 0x26200 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x171c | 0x1800 | `0x180029000` | 0x26e00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0xbb2 | 0xc00 | `0x18002b000` | 0x28600 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x408 | 0x600 | `0x18002c000` | 0x29200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x5a0 | 0x600 | `0x18002d000` | 0x29800 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0x26d20` | RVA | 0xa0 |
| `Import` | `0x2b2c0` | RVA | 0xc8 |
| `Resource` | `0x2c000` | RVA | 0x408 |
| `Exception` | `0x29000` | RVA | 0x171c |
| `BaseReloc` | `0x2d000` | RVA | 0x5a0 |
| `Debug` | `0x13d0` | RVA | 0x1c |
| `LoadConfig` | `0x5d60` | RVA | 0x94 |
| `IAT` | `0x2b000` | RVA | 0x2b8 |

## Static imports

- `KERNEL32.dll`: 30 imports
- `msvcrt.dll`: 36 imports
- `ole32.dll`: 1 imports
- `OLEAUT32.dll`: 5 imports
- `RPCRT4.dll`: 1 imports
- `SHLWAPI.dll`: 1 imports
- `tdh.dll`: 2 imports
- `USER32.dll`: 1 imports
- `XmlLite.dll`: 1 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/Timeline_is.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
