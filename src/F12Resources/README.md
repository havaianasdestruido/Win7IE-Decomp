# F12Resources.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `150a7ca97018977d0ca28fc217b4e4e3e5fdf3b822381192f4bc0473c48ec010` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/F12Resources.dll`
- Bytes: 10,949,120
- SHA-256: `150a7ca97018977d0ca28fc217b4e4e3e5fdf3b822381192f4bc0473c48ec010`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180001130` (RVA `0x1130`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`, `GUARD_CF`
- Timestamp field: `2019-12-17T01:13:29Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `F12Resources.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x299 | 0x400 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x10 | 0x200 | `0x180002000` | 0x800 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x18 | 0x200 | `0x180003000` | 0xa00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x13a | 0x200 | `0x180004000` | 0xc00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0xa700c8 | 0xa70200 | `0x180005000` | 0xe00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x1c | 0x200 | `0x180a76000` | 0xa71000 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x1260` | 0x39 |
| `Import` | `0x4040` | 0x28 |
| `Resource` | `0x5000` | 0xa700c8 |
| `Exception` | `0x3000` | 0x18 |
| `BaseReloc` | `0xa76000` | 0x1c |
| `Debug` | `0x1010` | 0x1c |
| `LoadConfig` | `0x1050` | 0x94 |
| `IAT` | `0x4000` | 0x38 |

## Static imports

- `KERNEL32.dll`: 6 imports

## Delay-load imports

- None recovered.

## Exports

none recovered

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/F12Resources.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
