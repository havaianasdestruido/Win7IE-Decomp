# ieinstal.exe

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `2cf44880a0da18c284d20ce9049bd76007ae5eaf046cf2ddfdadf7ff5f7a649c` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x000000014000fa70`
- Timestamp field: `Tue Dec 17 00:29:22 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00013b90` | 0x0 | `0x00000000` | 0x133e0 |
| `00013bd0` | 0x0 | `0x00000000` | 0x13420 |
| `00013e18` | 0x0 | `0x00000000` | 0x13668 |
| `000138f8` | 0x0 | `0x00000000` | 0x13148 |
| `00013c38` | 0x0 | `0x00000000` | 0x13488 |
| `00000000` | 0x0 | `0x00000000` | 0x0 |
| `.text` | 0xfb94 | `0x0000000140001000` | 0x400 |
| `.data` | 0x200 | `0x0000000140011000` | 0x10000 |
| `.pdata` | 0x8ac | `0x0000000140012000` | 0x10200 |
| `.idata` | 0x1c26 | `0x0000000140013000` | 0x10c00 |
| `.rsrc` | 0x650e0 | `0x0000000140015000` | 0x12a00 |
| `.reloc` | 0x49c | `0x000000014007b000` | 0x77c00 |

## Dependencies

- `ADVAPI32.dll`: 40 named imports
- `AUTHZ.dll`: 5 named imports
- `KERNEL32.dll`: 76 named imports
- `OLEAUT32.dll`: 1 named imports
- `RPCRT4.dll`: 3 named imports
- `USER32.dll`: 3 named imports
- `WINTRUST.dll`: 4 named imports
- `iertutil.dll`: 1 named imports
- `msvcrt.dll`: 32 named imports
- `ntdll.dll`: 4 named imports
- `ole32.dll`: 14 named imports
- `urlmon.dll`: 5 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/ieinstal.exe.objdump.txt`.
