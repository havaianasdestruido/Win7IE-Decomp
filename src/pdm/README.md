# pdm.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `ca795fedc2b655890a19f868f145cc6db0aae797e1d6faf7b2b8ed7ac75723a5` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180036a54`
- Timestamp field: `Fri Jul 12 03:42:28 2013` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0x51cdf | `0x0000000180001000` | 0x400 |
| `.rdata` | 0x252f2 | `0x0000000180053000` | 0x52200 |
| `.data` | 0x1c00 | `0x0000000180079000` | 0x77600 |
| `.pdata` | 0x4800 | `0x000000018007e000` | 0x79200 |
| `.rsrc` | 0x1750 | `0x0000000180083000` | 0x7da00 |
| `.reloc` | 0x1474 | `0x0000000180085000` | 0x7f200 |

## Dependencies

- `ADVAPI32.dll`: 33 named imports
- `KERNEL32.dll`: 120 named imports
- `OLEAUT32.dll`: 1 named imports
- `USER32.dll`: 17 named imports
- `ole32.dll`: 18 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/pdm.dll.objdump.txt`.
