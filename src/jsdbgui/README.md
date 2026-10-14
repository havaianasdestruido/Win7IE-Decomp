# jsdbgui.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `a786eaf21f6bc5bbd9bf5a2b6d744e8082df267e83170ac0475db1c976ebe26a` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180052c30`
- Timestamp field: `Mon Oct 14 05:39:23 2013` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0x61436 | `0x0000000180001000` | 0x400 |
| `.data` | 0x600 | `0x0000000180063000` | 0x61a00 |
| `.pdata` | 0x3924 | `0x0000000180064000` | 0x62000 |
| `.idata` | 0x27d4 | `0x0000000180068000` | 0x65a00 |
| `.rsrc` | 0x208e8 | `0x000000018006b000` | 0x68200 |
| `.reloc` | 0x1330 | `0x000000018008c000` | 0x88c00 |

## Dependencies

- `ADVAPI32.dll`: 10 named imports
- `GDI32.dll`: 35 named imports
- `KERNEL32.dll`: 63 named imports
- `MSIMG32.dll`: 1 named imports
- `OLEACC.dll`: 2 named imports
- `OLEAUT32.dll`: 1 named imports
- `SHLWAPI.dll`: 6 named imports
- `USER32.dll`: 111 named imports
- `iertutil.dll`: 1 named imports
- `msvcrt.dll`: 50 named imports
- `ole32.dll`: 6 named imports
- `urlmon.dll`: 2 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/jsdbgui.dll.objdump.txt`.
