# jsprofilerui.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `2dce1ffc22f877cb632dda8dc0fd662d1ad0bad08c72420ab0a08f54f7c911bf` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180027260`
- Timestamp field: `Tue Dec 17 00:32:40 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00031fe8` | 0x0 | `0x00000000` | 0x316a8 |
| `00031a28` | 0x0 | `0x00000000` | 0x310e8 |
| `00031cd8` | 0x0 | `0x00000000` | 0x31398 |
| `00031fb0` | 0x0 | `0x00000000` | 0x31670 |
| `00032178` | 0x0 | `0x00000000` | 0x31838 |
| `.text` | 0x2c524 | `0x0000000180001000` | 0x400 |
| `.data` | 0x400 | `0x000000018002e000` | 0x2ca00 |
| `.pdata` | 0x1b9c | `0x000000018002f000` | 0x2ce00 |
| `.idata` | 0x21ac | `0x0000000180031000` | 0x2ea00 |
| `.rsrc` | 0x685f8 | `0x0000000180034000` | 0x30c00 |
| `.reloc` | 0x554 | `0x000000018009d000` | 0x99200 |

## Dependencies

- `ADVAPI32.dll`: 7 named imports
- `GDI32.dll`: 20 named imports
- `KERNEL32.dll`: 69 named imports
- `OLEACC.dll`: 2 named imports
- `OLEAUT32.dll`: 1 named imports
- `SHLWAPI.dll`: 1 named imports
- `USER32.dll`: 90 named imports
- `iertutil.dll`: 2 named imports
- `msvcrt.dll`: 44 named imports
- `ole32.dll`: 4 named imports
- `urlmon.dll`: 1 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/jsprofilerui.dll.objdump.txt`.
