# DiagnosticsHub.ScriptedSandboxPlugin.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `d74c75ced0f3257797edf7050195938cae23765125688f758a8fccb099a69b42` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/DiagnosticsHub.ScriptedSandboxPlugin.dll`
- Bytes: 276,480
- SHA-256: `d74c75ced0f3257797edf7050195938cae23765125688f758a8fccb099a69b42`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180021ce0` (RVA `0x21ce0`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T00:37:56Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `DiagnosticsHub.ScriptedSandboxPlugin.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x3d968 | 0x3da00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x3d38 | 0x1a00 | `0x18003f000` | 0x3de00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x23b8 | 0x2400 | `0x180043000` | 0x3f800 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0xfe8 | 0x1000 | `0x180046000` | 0x41c00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x490 | 0x600 | `0x180047000` | 0x42c00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x518 | 0x600 | `0x180048000` | 0x43200 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0x3e8f0` | RVA | 0x78 |
| `Import` | `0x463c0` | RVA | 0x78 |
| `Resource` | `0x47000` | RVA | 0x490 |
| `Exception` | `0x43000` | RVA | 0x23b8 |
| `BaseReloc` | `0x48000` | RVA | 0x518 |
| `Debug` | `0x1440` | RVA | 0x1c |
| `LoadConfig` | `0x7c80` | RVA | 0x94 |
| `IAT` | `0x46000` | RVA | 0x3b8 |

## Static imports

- `ADVAPI32.dll`: 3 imports
- `KERNEL32.dll`: 88 imports
- `ole32.dll`: 4 imports
- `OLEAUT32.dll`: 8 imports
- `USER32.dll`: 11 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/DiagnosticsHub.ScriptedSandboxPlugin.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
