# networkinspection.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `27094ed77aa2c833920c38b27a2dd9806d95680d99179dbb5ff75e09e12c8100` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/networkinspection.dll`
- Bytes: 1,217,024
- SHA-256: `27094ed77aa2c833920c38b27a2dd9806d95680d99179dbb5ff75e09e12c8100`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180053280` (RVA `0x53280`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T00:26:50Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `networkinspection.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x631d9 | 0x63200 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x10d4 | 0x800 | `0x180065000` | 0x63600 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x3000 | 0x3000 | `0x180067000` | 0x63e00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x2ba8 | 0x2c00 | `0x18006a000` | 0x66e00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0xbf1e8 | 0xbf200 | `0x18006d000` | 0x69a00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x5f4 | 0x600 | `0x18012d000` | 0x128c00 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0x64180` | RVA | 0x59 |
| `Import` | `0x6aa88` | RVA | 0x154 |
| `Resource` | `0x6d000` | RVA | 0xbf1e8 |
| `Exception` | `0x67000` | RVA | 0x3000 |
| `BaseReloc` | `0x12d000` | RVA | 0x5f4 |
| `Debug` | `0x1640` | RVA | 0x1c |
| `LoadConfig` | `0x7ad0` | RVA | 0x94 |
| `IAT` | `0x6a000` | RVA | 0xa80 |

## Static imports

- `ADVAPI32.dll`: 8 imports
- `GDI32.dll`: 25 imports
- `iertutil.dll`: 8 imports
- `KERNEL32.dll`: 89 imports
- `MSIMG32.dll`: 1 imports
- `msvcrt.dll`: 56 imports
- `ole32.dll`: 5 imports
- `OLEACC.dll`: 2 imports
- `OLEAUT32.dll`: 9 imports
- `SHELL32.dll`: 1 imports
- `SHLWAPI.dll`: 4 imports
- `urlmon.dll`: 2 imports
- `USER32.dll`: 97 imports
- `VERSION.dll`: 3 imports
- `WindowsCodecs.dll`: 1 imports
- `WININET.dll`: 9 imports

## Delay-load imports

- None recovered.

## Exports

`CreateNetworkTab`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/networkinspection.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
