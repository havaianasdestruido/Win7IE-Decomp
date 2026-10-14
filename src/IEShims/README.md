# IEShims.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `e9b0cfa86136da976a12c4ca981e1be1e9d6e6ec43250c0b4939ddd59732638e` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x00000001800010e0`
- Timestamp field: `Mon Dec 16 23:45:34 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0x559e0 | `0x0000000180001000` | 0x400 |
| `.data` | 0x1c00 | `0x0000000180057000` | 0x55e00 |
| `.pdata` | 0x42cc | `0x0000000180059000` | 0x57a00 |
| `.idata` | 0x15f6 | `0x000000018005e000` | 0x5be00 |
| `.didat` | 0x138 | `0x0000000180060000` | 0x5d400 |
| `.rsrc` | 0x430 | `0x0000000180061000` | 0x5d600 |
| `.reloc` | 0x8d4 | `0x0000000180062000` | 0x5dc00 |

## Dependencies

- `KERNEL32.dll`: 90 named imports
- `api-ms-win-downlevel-advapi32-l1-1-0.dll`: 9 named imports
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll`: 11 named imports
- `iertutil.dll`: 1 named imports
- `msvcrt.dll`: 41 named imports
- `ntdll.dll`: 2 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/IEShims.dll.objdump.txt`.
