# iedvtool.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `f188b636065cfa5bdae6c6c4b2ae3fe1df7ff2b700c2144b1291dee7f5f9f912` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180099490`
- Timestamp field: `Tue Dec 17 02:39:52 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0xae4c5 | `0x0000000180001000` | 0x400 |
| `.data` | 0x600 | `0x00000001800b0000` | 0xaea00 |
| `.pdata` | 0x55ec | `0x00000001800b1000` | 0xaf000 |
| `.idata` | 0x398a | `0x00000001800b7000` | 0xb4600 |
| `.rsrc` | 0x2e8e0 | `0x00000001800bb000` | 0xb8000 |
| `.reloc` | 0x1770 | `0x00000001800ea000` | 0xe6a00 |

## Dependencies

- `ADVAPI32.dll`: 10 named imports
- `GDI32.dll`: 36 named imports
- `IEFRAME.dll`: 7 named imports
- `KERNEL32.dll`: 95 named imports
- `MSHTML.dll`: 1 named imports
- `MSIMG32.dll`: 2 named imports
- `OLEACC.dll`: 2 named imports
- `OLEAUT32.dll`: 1 named imports
- `SHELL32.dll`: 3 named imports
- `SHLWAPI.dll`: 16 named imports
- `USER32.dll`: 140 named imports
- `UxTheme.dll`: 1 named imports
- `WININET.dll`: 14 named imports
- `iertutil.dll`: 1 named imports
- `msvcrt.dll`: 55 named imports
- `ole32.dll`: 12 named imports
- `urlmon.dll`: 7 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/iedvtool.dll.objdump.txt`.
