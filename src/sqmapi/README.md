# sqmapi.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `ab65e97c8405660a881163957ef1fc29df0e1627eef04b282b3f6825eb78e4c2` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x00000001800014d4`
- Timestamp field: `Thu Jul 26 01:32:17 2012` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00044738` | 0x50109e21 | `0x0000001d` | 0x44000 |
| `00044a08` | 0x50109e21 | `0xffffffff` | 0x442d0 |
| `00044a38` | 0x50109e21 | `0x0000002d` | 0x44300 |
| `.text` | 0x3e3d8 | `0x0000000180001000` | 0x400 |
| `.data` | 0xce4 | `0x0000000180040000` | 0x3e800 |
| `.pdata` | 0x21d8 | `0x0000000180041000` | 0x3f600 |
| `.idata` | 0x1b42 | `0x0000000180044000` | 0x41800 |
| `.rsrc` | 0x400 | `0x0000000180046000` | 0x43400 |
| `.reloc` | 0x204 | `0x0000000180047000` | 0x43800 |

## Dependencies

- `ADVAPI32.dll`: 36 named imports
- `KERNEL32.dll`: 97 named imports
- `RPCRT4.dll`: 3 named imports
- `USER32.dll`: 5 named imports
- `msvcrt.dll`: 52 named imports
- `ntdll.dll`: 4 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/sqmapi.dll.objdump.txt`.
