# JSProfilerCore.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `a4929d0a664ca0e1ef9d0ab3ec16914e75ddb655cc42490038a8db183b23124e` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/JSProfilerCore.dll`
- Bytes: 67,072
- SHA-256: `a4929d0a664ca0e1ef9d0ab3ec16914e75ddb655cc42490038a8db183b23124e`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x18000b70c` (RVA `0xb70c`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2013-10-14T06:00:33Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `JSProfilerCore.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0xd931 | 0xda00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x938 | 0x200 | `0x18000f000` | 0xde00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0xa2c | 0xc00 | `0x180010000` | 0xe000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0xe32 | 0x1000 | `0x180011000` | 0xec00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x420 | 0x600 | `0x180012000` | 0xfc00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x362 | 0x400 | `0x180013000` | 0x10200 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0xe8c0` | 0x71 |
| `Import` | `0x11370` | 0xb4 |
| `Resource` | `0x12000` | 0x420 |
| `Exception` | `0x10000` | 0xa2c |
| `BaseReloc` | `0x13000` | 0x178 |
| `Debug` | `0x1070` | 0x1c |
| `LoadConfig` | `0x2440` | 0x94 |
| `IAT` | `0x11000` | 0x370 |

## Static imports

- `ADVAPI32.dll`: 7 imports
- `iertutil.dll`: 1 imports
- `KERNEL32.dll`: 41 imports
- `msvcrt.dll`: 36 imports
- `ole32.dll`: 4 imports
- `OLEAUT32.dll`: 9 imports
- `USER32.dll`: 2 imports
- `WINMM.dll`: 2 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/JSProfilerCore.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
