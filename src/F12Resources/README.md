# F12Resources.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `150a7ca97018977d0ca28fc217b4e4e3e5fdf3b822381192f4bc0473c48ec010` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180001130`
- Timestamp field: `Tue Dec 17 01:13:29 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00004068` | 0x0 | `0x00000000` | 0x4000 |
| `00000000` | 0x0 | `0x00000000` | 0x0 |
| `.text` | 0x299 | `0x0000000180001000` | 0x400 |
| `.data` | 0x10 | `0x0000000180002000` | 0x800 |
| `.pdata` | 0x18 | `0x0000000180003000` | 0xa00 |
| `.idata` | 0x13a | `0x0000000180004000` | 0xc00 |
| `.rsrc` | 0xa700c8 | `0x0000000180005000` | 0xe00 |
| `.reloc` | 0x1c | `0x0000000180a76000` | 0xa71000 |

## Dependencies

- `KERNEL32.dll`: 6 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/F12Resources.dll.objdump.txt`.
