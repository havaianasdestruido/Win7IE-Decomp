# JSProfilerCore.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `a4929d0a664ca0e1ef9d0ab3ec16914e75ddb655cc42490038a8db183b23124e` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x000000018000b70c`
- Timestamp field: `Mon Oct 14 06:00:33 2013` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00011648` | 0x0 | `0x00000000` | 0x11220 |
| `00011428` | 0x0 | `0x00000000` | 0x11000 |
| `00011468` | 0x0 | `0x00000000` | 0x11040 |
| `00000000` | 0x0 | `0x00000000` | 0x0 |
| `.text` | 0xd931 | `0x0000000180001000` | 0x400 |
| `.data` | 0x200 | `0x000000018000f000` | 0xde00 |
| `.pdata` | 0xa2c | `0x0000000180010000` | 0xe000 |
| `.idata` | 0xe32 | `0x0000000180011000` | 0xec00 |
| `.rsrc` | 0x420 | `0x0000000180012000` | 0xfc00 |
| `.reloc` | 0x362 | `0x0000000180013000` | 0x10200 |

## Dependencies

- `ADVAPI32.dll`: 7 named imports
- `KERNEL32.dll`: 41 named imports
- `OLEAUT32.dll`: 1 named imports
- `USER32.dll`: 2 named imports
- `WINMM.dll`: 2 named imports
- `iertutil.dll`: 1 named imports
- `msvcrt.dll`: 36 named imports
- `ole32.dll`: 4 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/JSProfilerCore.dll.objdump.txt`.
