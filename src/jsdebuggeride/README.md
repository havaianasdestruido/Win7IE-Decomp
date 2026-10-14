# jsdebuggeride.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `a4ad21edbb7891e1e89c056b970a67955c2eb1c10aaaf90bc1062869a52b722e` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180019d70`
- Timestamp field: `Mon Oct 14 05:42:51 2013` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `000237e0` | 0x0 | `0x00000000` | 0x232a8 |
| `00023580` | 0x0 | `0x00000000` | 0x23048 |
| `00023768` | 0x0 | `0x00000000` | 0x23230 |
| `00023758` | 0x0 | `0x00000000` | 0x23220 |
| `00000000` | 0x0 | `0x00000000` | 0x0 |
| `.text` | 0x1e830 | `0x0000000180001000` | 0x400 |
| `.data` | 0x400 | `0x0000000180020000` | 0x1ee00 |
| `.pdata` | 0x1650 | `0x0000000180021000` | 0x1f200 |
| `.idata` | 0x1232 | `0x0000000180023000` | 0x20a00 |
| `.rsrc` | 0x418 | `0x0000000180025000` | 0x21e00 |
| `.reloc` | 0x7d0 | `0x0000000180026000` | 0x22400 |

## Dependencies

- `ADVAPI32.dll`: 8 named imports
- `KERNEL32.dll`: 43 named imports
- `OLEAUT32.dll`: 1 named imports
- `SHLWAPI.dll`: 1 named imports
- `USER32.dll`: 6 named imports
- `WININET.dll`: 7 named imports
- `msvcrt.dll`: 45 named imports
- `ole32.dll`: 7 named imports
- `urlmon.dll`: 2 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/jsdebuggeride.dll.objdump.txt`.
