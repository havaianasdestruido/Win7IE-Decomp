# Timeline_is.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `cc3298491463bf23bae8b0d3d45d0899cfb314f3985aec52911223f58941dd49` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180021450`
- Timestamp field: `Tue Dec 17 00:56:45 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0x25dc0 | `0x0000000180001000` | 0x400 |
| `.data` | 0xc00 | `0x0000000180027000` | 0x26200 |
| `.pdata` | 0x171c | `0x0000000180029000` | 0x26e00 |
| `.idata` | 0xbb2 | `0x000000018002b000` | 0x28600 |
| `.rsrc` | 0x408 | `0x000000018002c000` | 0x29200 |
| `.reloc` | 0x5a0 | `0x000000018002d000` | 0x29800 |

## Dependencies

- `KERNEL32.dll`: 30 named imports
- `OLEAUT32.dll`: 1 named imports
- `RPCRT4.dll`: 1 named imports
- `SHLWAPI.dll`: 1 named imports
- `USER32.dll`: 1 named imports
- `XmlLite.dll`: 1 named imports
- `msvcrt.dll`: 36 named imports
- `ole32.dll`: 1 named imports
- `tdh.dll`: 2 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/Timeline_is.dll.objdump.txt`.
