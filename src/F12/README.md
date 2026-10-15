# F12.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `efe153059d169ce0ad4f68b8e0c43ca8eb8a86ff4dc234a8529bae0059d602db` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/F12.dll`
- Bytes: 1,421,312
- SHA-256: `efe153059d169ce0ad4f68b8e0c43ca8eb8a86ff4dc234a8529bae0059d602db`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x1800ade40` (RVA `0xade40`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T00:26:19Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `F12.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0xc556e | 0xc5600 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x8bcc | 0x8200 | `0x1800c7000` | 0xc5a00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x5340 | 0x5400 | `0x1800d0000` | 0xcdc00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x37e0 | 0x3800 | `0x1800d6000` | 0xd3000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x834b0 | 0x83600 | `0x1800da000` | 0xd6800 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x11e0 | 0x1200 | `0x18015e000` | 0x159e00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0xc64c0` | 0xae |
| `Import` | `0xd6de0` | 0x17c |
| `Resource` | `0xda000` | 0x834b0 |
| `Exception` | `0xd0000` | 0x5340 |
| `BaseReloc` | `0x15e000` | 0x11e0 |
| `Debug` | `0x1f10` | 0x1c |
| `LoadConfig` | `0x17a70` | 0x94 |
| `IAT` | `0xd6000` | 0xdd8 |

## Static imports

- `ADVAPI32.dll`: 18 imports
- `GDI32.dll`: 24 imports
- `iertutil.dll`: 10 imports
- `KERNEL32.dll`: 101 imports
- `MSIMG32.dll`: 1 imports
- `msvcrt.dll`: 63 imports
- `ole32.dll`: 18 imports
- `OLEACC.dll`: 3 imports
- `OLEAUT32.dll`: 31 imports
- `SHELL32.dll`: 3 imports
- `SHLWAPI.dll`: 8 imports
- `urlmon.dll`: 2 imports
- `USER32.dll`: 131 imports
- `UxTheme.dll`: 1 imports
- `VERSION.dll`: 3 imports
- `wer.dll`: 5 imports
- `WindowsCodecs.dll`: 1 imports
- `XmlLite.dll`: 2 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllRegisterServer`, `DllUnregisterServer`, `ShowChooser`, `ShowTools`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/F12.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
