# ieproxy.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `7bfc8614acfacf4f06887e8e518a5647749a066b0a9832e2edb489022091866c` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180001ce0`
- Timestamp field: `Mon Dec 16 23:37:15 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0xaad34 | `0x0000000180001000` | 0x400 |
| `.orpc` | 0x3897 | `0x00000001800ac000` | 0xab200 |
| `.data` | 0x4200 | `0x00000001800b0000` | 0xaec00 |
| `.pdata` | 0x1788 | `0x00000001800b5000` | 0xb2e00 |
| `.idata` | 0xf34 | `0x00000001800b7000` | 0xb4600 |
| `.didat` | 0x498 | `0x00000001800b8000` | 0xb5600 |
| `.rsrc` | 0x438 | `0x00000001800b9000` | 0xb5c00 |
| `.reloc` | 0xe6d0 | `0x00000001800ba000` | 0xb6200 |

## Dependencies

- `KERNEL32.dll`: 39 named imports
- `RPCRT4.dll`: 25 named imports
- `api-ms-win-downlevel-advapi32-l1-1-0.dll`: 6 named imports
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll`: 7 named imports
- `api-ms-win-downlevel-shlwapi-l2-1-0.dll`: 2 named imports
- `msvcrt.dll`: 18 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/ieproxy.dll.objdump.txt`.
