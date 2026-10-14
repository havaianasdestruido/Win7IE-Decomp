# DiagnosticsTap.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `92ca2180dc18f21bb9b394bbb3bbff040d90564e3d984b13bd6d7a3f24b359eb` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x000000018002b460`
- Timestamp field: `Tue Dec 17 00:40:47 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0x341b0 | `0x0000000180001000` | 0x400 |
| `.data` | 0xa00 | `0x0000000180036000` | 0x34600 |
| `.pdata` | 0x2094 | `0x0000000180038000` | 0x35000 |
| `.idata` | 0x1948 | `0x000000018003b000` | 0x37200 |
| `.rsrc` | 0x27a8 | `0x000000018003d000` | 0x38c00 |
| `.reloc` | 0x5d0 | `0x0000000180040000` | 0x3b400 |

## Dependencies

- `ADVAPI32.dll`: 28 named imports
- `KERNEL32.dll`: 68 named imports
- `OLEAUT32.dll`: 1 named imports
- `SHLWAPI.dll`: 2 named imports
- `USER32.dll`: 20 named imports
- `msvcrt.dll`: 46 named imports
- `ole32.dll`: 5 named imports
- `urlmon.dll`: 2 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/DiagnosticsTap.dll.objdump.txt`.
