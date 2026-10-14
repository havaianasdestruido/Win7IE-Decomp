# iexplore.exe

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `cff801d6dc847bb832d0077ce38ddb66ef5b4637ff947bbdbc228eef10494f97` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x00000001400019f0`
- Timestamp field: `Mon Dec 16 23:36:35 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00007510` | 0x0 | `0x00000000` | 0x70e0 |
| `00007650` | 0x0 | `0x00000000` | 0x7220 |
| `00007698` | 0x0 | `0x00000000` | 0x7268 |
| `000076f0` | 0x0 | `0x00000000` | 0x72c0 |
| `00000000` | 0x0 | `0x00000000` | 0x0 |
| `.text` | 0x3c70 | `0x0000000140001000` | 0x400 |
| `.data` | 0x7e8 | `0x0000000140005000` | 0x4200 |
| `.pdata` | 0x4a4 | `0x0000000140006000` | 0x4a00 |
| `.idata` | 0xc58 | `0x0000000140007000` | 0x5000 |
| `.didat` | 0x30 | `0x0000000140008000` | 0x5e00 |
| `.rsrc` | 0xbd848 | `0x0000000140009000` | 0x6000 |
| `.reloc` | 0x60 | `0x00000001400c7000` | 0xc3a00 |

## Dependencies

- `KERNEL32.dll`: 39 named imports
- `USER32.dll`: 6 named imports
- `api-ms-win-downlevel-advapi32-l1-1-0.dll`: 8 named imports
- `api-ms-win-downlevel-shell32-l1-1-0.dll`: 2 named imports
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll`: 1 named imports
- `iertutil.dll`: 1 named imports
- `msvcrt.dll`: 20 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/iexplore.exe.objdump.txt`.
