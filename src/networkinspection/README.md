# networkinspection.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `27094ed77aa2c833920c38b27a2dd9806d95680d99179dbb5ff75e09e12c8100` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180053280`
- Timestamp field: `Tue Dec 17 00:26:50 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0x631d9 | `0x0000000180001000` | 0x400 |
| `.data` | 0x800 | `0x0000000180065000` | 0x63600 |
| `.pdata` | 0x3000 | `0x0000000180067000` | 0x63e00 |
| `.idata` | 0x2ba8 | `0x000000018006a000` | 0x66e00 |
| `.rsrc` | 0xbf1e8 | `0x000000018006d000` | 0x69a00 |
| `.reloc` | 0x5f4 | `0x000000018012d000` | 0x128c00 |

## Dependencies

- `ADVAPI32.dll`: 8 named imports
- `GDI32.dll`: 25 named imports
- `KERNEL32.dll`: 89 named imports
- `MSIMG32.dll`: 1 named imports
- `OLEACC.dll`: 2 named imports
- `OLEAUT32.dll`: 1 named imports
- `SHELL32.dll`: 1 named imports
- `SHLWAPI.dll`: 4 named imports
- `USER32.dll`: 97 named imports
- `VERSION.dll`: 3 named imports
- `WININET.dll`: 9 named imports
- `WindowsCodecs.dll`: 1 named imports
- `iertutil.dll`: 2 named imports
- `msvcrt.dll`: 56 named imports
- `ole32.dll`: 5 named imports
- `urlmon.dll`: 2 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/networkinspection.dll.objdump.txt`.
