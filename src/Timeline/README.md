# Timeline.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `e8149b60852195407bb0a42cab61d248ac28756b0f3acdf67e982572ff1f2b5b` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/Timeline.dll`
- Bytes: 219,136
- SHA-256: `e8149b60852195407bb0a42cab61d248ac28756b0f3acdf67e982572ff1f2b5b`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x1800299e0` (RVA `0x299e0`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T00:34:36Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `Timeline.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x30dae | 0x30e00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0xcd0 | 0x600 | `0x180032000` | 0x31200 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x19f8 | 0x1a00 | `0x180033000` | 0x31800 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0xcac | 0xe00 | `0x180035000` | 0x33200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x11e0 | 0x1200 | `0x180036000` | 0x34000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x4ac | 0x600 | `0x180038000` | 0x35200 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x31d40` | 0x6e |
| `Import` | `0x35328` | 0x8c |
| `Resource` | `0x36000` | 0x11e0 |
| `Exception` | `0x33000` | 0x19f8 |
| `BaseReloc` | `0x38000` | 0x4ac |
| `Debug` | `0x13c0` | 0x1c |
| `LoadConfig` | `0x6170` | 0x94 |
| `IAT` | `0x35000` | 0x320 |

## Static imports

- `KERNEL32.dll`: 33 imports
- `msvcrt.dll`: 47 imports
- `ole32.dll`: 1 imports
- `OLEAUT32.dll`: 10 imports
- `SHLWAPI.dll`: 2 imports
- `USER32.dll`: 1 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/Timeline.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
