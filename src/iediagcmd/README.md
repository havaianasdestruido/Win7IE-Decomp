# iediagcmd.exe

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `412df2da4d524e6b78ed6c7bc595224643574510fba194ee940e495d981a6510` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/iediagcmd.exe`
- Bytes: 359,632
- SHA-256: `412df2da4d524e6b78ed6c7bc595224643574510fba194ee940e495d981a6510`
- Format: `PE32`
- Machine: `IMAGE_FILE_MACHINE_I386`
- Entry point: `0x43f81e` (RVA `0x3f81e`)
- ImageBase: `0x400000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `8.0`; OS version: `4.0`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `32BIT_MACHINE`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `NO_SEH`, `TERMINAL_SERVER_AWARE`
- Timestamp field: `2013-10-14T02:52:50Z` (untrusted PE metadata)
- CLR header present: `True`
- CodeView PDB: `IEDiagCmd.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x3d824 | 0x3e000 | `0x402000` | 0x1000 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.rsrc` | 0x13e88 | 0x14000 | `0x440000` | 0x3f000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0xc | 0x1000 | `0x454000` | 0x53000 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Import` | `0x3f7c4` | RVA | 0x57 |
| `Resource` | `0x40000` | RVA | 0x13e88 |
| `Security` | `0x54000` | file offset | 0x3cd0 |
| `BaseReloc` | `0x54000` | RVA | 0xc |
| `Debug` | `0x3f74c` | RVA | 0x1c |
| `IAT` | `0x2000` | RVA | 0x8 |
| `CLR` | `0x2008` | RVA | 0x48 |

## Static imports

- `mscoree.dll`: 1 imports

## Delay-load imports

- None recovered.

## Exports

none recovered

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/iediagcmd.exe.objdump.txt` and `analysis/report/generated/pe-struct.json`.
