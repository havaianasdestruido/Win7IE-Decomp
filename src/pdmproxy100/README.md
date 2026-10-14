# pdmproxy100.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `a3e0fd851f31be04f0bf268038501f26c5a552311967e42fc4ec7f8a4761fe3e` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180001210`
- Timestamp field: `Fri Jul 12 02:40:34 2013` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0xaca4 | `0x0000000180001000` | 0x400 |
| `.orpc` | 0x105 | `0x000000018000c000` | 0xb200 |
| `.rdata` | 0x7772 | `0x000000018000d000` | 0xb400 |
| `.data` | 0x1a00 | `0x0000000180015000` | 0x12c00 |
| `.pdata` | 0x8d0 | `0x0000000180019000` | 0x14600 |
| `.rsrc` | 0x428 | `0x000000018001a000` | 0x15000 |
| `.reloc` | 0x6bc | `0x000000018001b000` | 0x15600 |

## Dependencies

- `KERNEL32.dll`: 64 named imports
- `OLEAUT32.dll`: 1 named imports
- `RPCRT4.dll`: 22 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/pdmproxy100.dll.objdump.txt`.
