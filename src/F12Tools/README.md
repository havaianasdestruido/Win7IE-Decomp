# F12Tools.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `cad6f7aeb3a63aa1064d8343fb767b9c3e64a2dd59e5e65e52e75ac8eefdecec` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180043610`
- Timestamp field: `Tue Dec 17 00:39:29 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00059d10` | 0x0 | `0x00000000` | 0x59538 |
| `000597d8` | 0x0 | `0x00000000` | 0x59000 |
| `000598c8` | 0x0 | `0x00000000` | 0x590f0 |
| `00059e88` | 0x0 | `0x00000000` | 0x596b0 |
| `00059b08` | 0x0 | `0x00000000` | 0x59330 |
| `00059ba8` | 0x0 | `0x00000000` | 0x593d0 |
| `.text` | 0x51418 | `0x0000000180001000` | 0x400 |
| `.data` | 0x1c00 | `0x0000000180053000` | 0x51a00 |
| `.pdata` | 0x2c64 | `0x0000000180056000` | 0x53600 |
| `.idata` | 0x1d8c | `0x0000000180059000` | 0x56400 |
| `.rsrc` | 0x23f0 | `0x000000018005b000` | 0x58200 |
| `.reloc` | 0x734 | `0x000000018005e000` | 0x5a600 |

## Dependencies

- `ADVAPI32.dll`: 29 named imports
- `COMCTL32.dll`: 2 named imports
- `KERNEL32.dll`: 67 named imports
- `OLEAUT32.dll`: 1 named imports
- `SHELL32.dll`: 1 named imports
- `SHLWAPI.dll`: 4 named imports
- `USER32.dll`: 38 named imports
- `msvcrt.dll`: 46 named imports
- `ole32.dll`: 10 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/F12Tools.dll.objdump.txt`.
