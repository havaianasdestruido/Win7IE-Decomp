# ielowutil.exe

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `7099cea38e986d13f1a882a9ccd0ecf5666ff1c6d807abdc4bbe90ab90963769` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000140002940`
- Timestamp field: `Tue Dec 17 00:55:29 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `000064d0` | 0x0 | `0x00000000` | 0x6188 |
| `00000000` | 0x0 | `0x00000000` | 0x0 |
| `.text` | 0x20ec | `0x0000000140001000` | 0x400 |
| `.data` | 0x200 | `0x0000000140004000` | 0x2600 |
| `.pdata` | 0x1c8 | `0x0000000140005000` | 0x2800 |
| `.idata` | 0xb6c | `0x0000000140006000` | 0x2a00 |
| `.rsrc` | 0x32cb0 | `0x0000000140007000` | 0x3600 |
| `.reloc` | 0x30 | `0x000000014003a000` | 0x36400 |

## Dependencies

- `KERNEL32.dll`: 39 named imports
- `USER32.dll`: 5 named imports
- `WININET.dll`: 2 named imports
- `iertutil.dll`: 1 named imports
- `msvcrt.dll`: 20 named imports
- `ntdll.dll`: 3 named imports
- `ole32.dll`: 7 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/ielowutil.exe.objdump.txt`.
