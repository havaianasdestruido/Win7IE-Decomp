# perfcore.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `b41c4d0cb9e42d7d9020184944f05fa23873ad039454a53247691f4b0a0daf7a` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x000000018001a5ac`
- Timestamp field: `Mon Oct 14 06:41:35 2013` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00024458` | 0x0 | `0x00000000` | 0x24140 |
| `00000000` | 0x0 | `0x00000000` | 0x0 |
| `.text` | 0x1f280 | `0x0000000180001000` | 0x400 |
| `.data` | 0x600 | `0x0000000180021000` | 0x1f800 |
| `.pdata` | 0x1434 | `0x0000000180022000` | 0x1fe00 |
| `.idata` | 0xabe | `0x0000000180024000` | 0x21400 |
| `.rsrc` | 0x4d10 | `0x0000000180025000` | 0x22000 |
| `.reloc` | 0x652 | `0x000000018002a000` | 0x26e00 |

## Dependencies

- `ADVAPI32.dll`: 5 named imports
- `KERNEL32.dll`: 28 named imports
- `OLEAUT32.dll`: 1 named imports
- `msvcrt.dll`: 34 named imports
- `ntdll.dll`: 3 named imports
- `ole32.dll`: 1 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/perfcore.dll.objdump.txt`.
