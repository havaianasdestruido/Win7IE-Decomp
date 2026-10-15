# ieinstal.exe.mui

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `7c689bc49a601adacc3d0d7d6c907137a0c59f61db39b608eabc90ab4d0dd331` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/en-US/ieinstal.exe.mui`
- Bytes: 2,048
- SHA-256: `7c689bc49a601adacc3d0d7d6c907137a0c59f61db39b608eabc90ab4d0dd331`
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
| `.rsrc` | 0x1000 | 0x600 | `0x10001000` | 0x200 | CNT_INITIALIZED_DATA, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Resource` | `0x1000` | 0x5a8 |

## Static imports

- None recovered.

## Delay-load imports

- None recovered.

## Exports

none recovered

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/en-US__ieinstal.exe.mui.objdump.txt` and `analysis/report/generated/pe-struct.json`.
