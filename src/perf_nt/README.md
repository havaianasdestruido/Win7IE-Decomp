# perf_nt.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `bfe21d6f04d75fe22185d544dd1af570365b0d026886c20a6a2cbc069509079d` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/perf_nt.dll`
- Bytes: 1,477,120
- SHA-256: `bfe21d6f04d75fe22185d544dd1af570365b0d026886c20a6a2cbc069509079d`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180112bd8` (RVA `0x112bd8`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2013-10-14T06:21:19Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `perf_nt.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x152b00 | 0x152c00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x53d0 | 0x4a00 | `0x180154000` | 0x153000 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0xad64 | 0xae00 | `0x18015a000` | 0x157a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x1a60 | 0x1c00 | `0x180165000` | 0x162800 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x420 | 0x600 | `0x180167000` | 0x164400 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x3eb4 | 0x4000 | `0x180168000` | 0x164a00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0x153a60` | RVA | 0xa0 |
| `Import` | `0x165670` | RVA | 0xb4 |
| `Resource` | `0x167000` | RVA | 0x420 |
| `Exception` | `0x15a000` | RVA | 0xad64 |
| `BaseReloc` | `0x168000` | RVA | 0x2d9c |
| `Debug` | `0x1090` | RVA | 0x1c |
| `LoadConfig` | `0x2be70` | RVA | 0x94 |
| `IAT` | `0x165000` | RVA | 0x670 |
| `DelayImport` | `0x153680` | RVA | 0xa0 |

## Static imports

- `ADVAPI32.dll`: 9 imports
- `KERNEL32.dll`: 71 imports
- `msvcrt.dll`: 100 imports
- `ntdll.dll`: 4 imports
- `SHELL32.dll`: 1 imports
- `SHLWAPI.dll`: 10 imports
- `USER32.dll`: 2 imports
- `XmlLite.dll`: 1 imports

## Delay-load imports

- `dbghelp.dll`: 14 delay-load imports
- `ole32.dll`: 3 delay-load imports
- `OLEAUT32.dll`: 2 delay-load imports
- `VERSION.dll`: 3 delay-load imports

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/perf_nt.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
