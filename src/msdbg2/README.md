# msdbg2.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `ee4065d7ddfb9e588a81fa1e2a760c01f6e8275581d46381a1ee5e168c38a8d0` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x000000018000164c`
- Timestamp field: `Fri Jul 12 02:40:34 2013` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0xb11b | `0x0000000180001000` | 0x400 |
| `.orpc` | 0x1995 | `0x000000018000d000` | 0xb600 |
| `.rdata` | 0x3ee78 | `0x000000018000f000` | 0xd000 |
| `.data` | 0xa800 | `0x000000018004e000` | 0x4c000 |
| `.pdata` | 0xb04 | `0x000000018005b000` | 0x56800 |
| `.rsrc` | 0x418 | `0x000000018005c000` | 0x57400 |
| `.reloc` | 0x6440 | `0x000000018005d000` | 0x57a00 |

## Dependencies

- `KERNEL32.dll`: 64 named imports
- `OLEAUT32.dll`: 1 named imports
- `RPCRT4.dll`: 23 named imports
- `ole32.dll`: 4 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/msdbg2.dll.objdump.txt`.
