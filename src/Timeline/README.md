# Timeline.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `e8149b60852195407bb0a42cab61d248ac28756b0f3acdf67e982572ff1f2b5b` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x00000001800299e0`
- Timestamp field: `Tue Dec 17 00:34:36 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00035548` | 0x0 | `0x00000000` | 0x35190 |
| `00035538` | 0x0 | `0x00000000` | 0x35180 |
| `000356c8` | 0x0 | `0x00000000` | 0x35310 |
| `000354c8` | 0x0 | `0x00000000` | 0x35110 |
| `.text` | 0x30dae | `0x0000000180001000` | 0x400 |
| `.data` | 0x600 | `0x0000000180032000` | 0x31200 |
| `.pdata` | 0x19f8 | `0x0000000180033000` | 0x31800 |
| `.idata` | 0xcac | `0x0000000180035000` | 0x33200 |
| `.rsrc` | 0x11e0 | `0x0000000180036000` | 0x34000 |
| `.reloc` | 0x4ac | `0x0000000180038000` | 0x35200 |

## Dependencies

- `KERNEL32.dll`: 33 named imports
- `OLEAUT32.dll`: 1 named imports
- `SHLWAPI.dll`: 2 named imports
- `USER32.dll`: 1 named imports
- `msvcrt.dll`: 47 named imports
- `ole32.dll`: 1 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/Timeline.dll.objdump.txt`.
