# F12.dll.mui

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `3d3ed24c2e1a4cbb77dfc2e0353167437c3e0b1731c75bdc32492b88f5f18d82` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/pt-BR/F12.dll.mui`
- Bytes: 4,096
- SHA-256: `3d3ed24c2e1a4cbb77dfc2e0353167437c3e0b1731c75bdc32492b88f5f18d82`
- Format: `PE32`
- Machine: `IMAGE_FILE_MACHINE_I386`
- Entry point: `0x10000000` (RVA `0x0`)
- ImageBase: `0x10000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `32BIT_MACHINE`, `DLL`
- DllCharacteristics: `DYNAMIC_BASE`, `NX_COMPAT`, `NO_SEH`
- Timestamp field: `1970-01-01T00:00:00Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: none recovered

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.rsrc` | 0x1000 | 0xe00 | `0x10001000` | 0x200 | CNT_INITIALIZED_DATA, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Resource` | `0x1000` | 0xd6c |

## Static imports

- None recovered.

## Delay-load imports

- None recovered.

## Exports

none recovered

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/pt-BR__F12.dll.mui.objdump.txt` and `analysis/report/generated/pe-struct.json`.
