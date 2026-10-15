# F12Resources.dll.mui

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `cc10f91770ed7912ba4bee7e0bdd9baf4457d712d0e588124e1369882f63ec2c` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/en-US/F12Resources.dll.mui`
- Bytes: 61,440
- SHA-256: `cc10f91770ed7912ba4bee7e0bdd9baf4457d712d0e588124e1369882f63ec2c`
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
| `.rsrc` | 0xf000 | 0xee00 | `0x10001000` | 0x200 | CNT_INITIALIZED_DATA, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Resource` | `0x1000` | 0xed08 |

## Static imports

- None recovered.

## Delay-load imports

- None recovered.

## Exports

none recovered

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/en-US__F12Resources.dll.mui.objdump.txt` and `analysis/report/generated/pe-struct.json`.
