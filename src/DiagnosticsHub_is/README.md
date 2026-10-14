# DiagnosticsHub_is.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `7d75d8efc5107b64c2f0acfc6e7a33937ebacb1027b2c3f96bc1876878185da0` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180008eb0`
- Timestamp field: `Tue Dec 17 01:10:36 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0xa06e | `0x0000000180001000` | 0x400 |
| `.data` | 0x400 | `0x000000018000c000` | 0xa600 |
| `.pdata` | 0x738 | `0x000000018000d000` | 0xaa00 |
| `.idata` | 0x79e | `0x000000018000e000` | 0xb200 |
| `.rsrc` | 0x410 | `0x000000018000f000` | 0xba00 |
| `.reloc` | 0x32c | `0x0000000180010000` | 0xc000 |

## Dependencies

- `KERNEL32.dll`: 18 named imports
- `OLEAUT32.dll`: 1 named imports
- `msvcrt.dll`: 25 named imports
- `ole32.dll`: 1 named imports
- `tdh.dll`: 2 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/DiagnosticsHub_is.dll.objdump.txt`.
