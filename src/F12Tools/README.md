# F12Tools.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `cad6f7aeb3a63aa1064d8343fb767b9c3e64a2dd59e5e65e52e75ac8eefdecec` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/F12Tools.dll`
- Bytes: 372,224
- SHA-256: `cad6f7aeb3a63aa1064d8343fb767b9c3e64a2dd59e5e65e52e75ac8eefdecec`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180043610` (RVA `0x43610`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T00:39:29Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `F12Tools.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x51418 | 0x51600 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x23f8 | 0x1c00 | `0x180053000` | 0x51a00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x2c64 | 0x2e00 | `0x180056000` | 0x53600 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x1d8c | 0x1e00 | `0x180059000` | 0x56400 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x23f0 | 0x2400 | `0x18005b000` | 0x58200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x734 | 0x800 | `0x18005e000` | 0x5a600 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0x52360` | RVA | 0xb8 |
| `Import` | `0x59710` | RVA | 0xc8 |
| `Resource` | `0x5b000` | RVA | 0x23f0 |
| `Exception` | `0x56000` | RVA | 0x2c64 |
| `BaseReloc` | `0x5e000` | RVA | 0x734 |
| `Debug` | `0x16b0` | RVA | 0x1c |
| `LoadConfig` | `0x8450` | RVA | 0x94 |
| `IAT` | `0x59000` | RVA | 0x708 |

## Static imports

- `ADVAPI32.dll`: 29 imports
- `COMCTL32.dll`: 3 imports
- `KERNEL32.dll`: 67 imports
- `msvcrt.dll`: 46 imports
- `ole32.dll`: 10 imports
- `OLEAUT32.dll`: 17 imports
- `SHELL32.dll`: 1 imports
- `SHLWAPI.dll`: 5 imports
- `USER32.dll`: 38 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllInstall`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/F12Tools.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
