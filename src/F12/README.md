# F12.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `efe153059d169ce0ad4f68b8e0c43ca8eb8a86ff4dc234a8529bae0059d602db` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x00000001800ade40`
- Timestamp field: `Tue Dec 17 00:26:19 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0xc556e | `0x0000000180001000` | 0x400 |
| `.data` | 0x8200 | `0x00000001800c7000` | 0xc5a00 |
| `.pdata` | 0x5340 | `0x00000001800d0000` | 0xcdc00 |
| `.idata` | 0x37e0 | `0x00000001800d6000` | 0xd3000 |
| `.rsrc` | 0x834b0 | `0x00000001800da000` | 0xd6800 |
| `.reloc` | 0x11e0 | `0x000000018015e000` | 0x159e00 |

## Dependencies

- `ADVAPI32.dll`: 18 named imports
- `GDI32.dll`: 24 named imports
- `KERNEL32.dll`: 101 named imports
- `MSIMG32.dll`: 1 named imports
- `OLEACC.dll`: 3 named imports
- `OLEAUT32.dll`: 1 named imports
- `SHELL32.dll`: 3 named imports
- `SHLWAPI.dll`: 7 named imports
- `USER32.dll`: 131 named imports
- `UxTheme.dll`: 1 named imports
- `VERSION.dll`: 3 named imports
- `WindowsCodecs.dll`: 1 named imports
- `XmlLite.dll`: 2 named imports
- `iertutil.dll`: 2 named imports
- `msvcrt.dll`: 63 named imports
- `ole32.dll`: 18 named imports
- `urlmon.dll`: 1 named imports
- `wer.dll`: 5 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/F12.dll.objdump.txt`.
