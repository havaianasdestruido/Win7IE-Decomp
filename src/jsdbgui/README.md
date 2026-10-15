# jsdbgui.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `a786eaf21f6bc5bbd9bf5a2b6d744e8082df267e83170ac0475db1c976ebe26a` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/jsdbgui.dll`
- Bytes: 565,248
- SHA-256: `a786eaf21f6bc5bbd9bf5a2b6d744e8082df267e83170ac0475db1c976ebe26a`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180052c30` (RVA `0x52c30`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2013-10-14T05:39:23Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `jsdbgui.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x61436 | 0x61600 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0xeec | 0x600 | `0x180063000` | 0x61a00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x3924 | 0x3a00 | `0x180064000` | 0x62000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x27d4 | 0x2800 | `0x180068000` | 0x65a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x208e8 | 0x20a00 | `0x18006b000` | 0x68200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x1330 | 0x1400 | `0x18008c000` | 0x88c00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x623b0` | 0x86 |
| `Import` | `0x689f8` | 0x104 |
| `Resource` | `0x6b000` | 0x208e8 |
| `Exception` | `0x64000` | 0x3924 |
| `BaseReloc` | `0x8c000` | 0xb0c |
| `Debug` | `0x10c0` | 0x1c |
| `LoadConfig` | `0x88c0` | 0x94 |
| `IAT` | `0x68000` | 0x9f8 |

## Static imports

- `ADVAPI32.dll`: 10 imports
- `GDI32.dll`: 35 imports
- `iertutil.dll`: 6 imports
- `KERNEL32.dll`: 63 imports
- `MSIMG32.dll`: 1 imports
- `msvcrt.dll`: 50 imports
- `ole32.dll`: 6 imports
- `OLEACC.dll`: 2 imports
- `OLEAUT32.dll`: 15 imports
- `SHLWAPI.dll`: 6 imports
- `urlmon.dll`: 2 imports
- `USER32.dll`: 111 imports

## Delay-load imports

- None recovered.

## Exports

`CreateConsoleTab`, `CreateScriptTab`, `CreateSourceViewer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/jsdbgui.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
