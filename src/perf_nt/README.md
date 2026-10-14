# perf_nt.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `bfe21d6f04d75fe22185d544dd1af570365b0d026886c20a6a2cbc069509079d` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180112bd8`
- Timestamp field: `Mon Oct 14 06:21:19 2013` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00165a48` | 0x0 | `0x00000000` | 0x165320 |
| `00165a20` | 0x0 | `0x00000000` | 0x1652f8 |
| `00165d70` | 0x0 | `0x00000000` | 0x165648 |
| `00000000` | 0x0 | `0x00000000` | 0x0 |
| `.text` | 0x152b00 | `0x0000000180001000` | 0x400 |
| `.data` | 0x4a00 | `0x0000000180154000` | 0x153000 |
| `.pdata` | 0xad64 | `0x000000018015a000` | 0x157a00 |
| `.idata` | 0x1a60 | `0x0000000180165000` | 0x162800 |
| `.rsrc` | 0x420 | `0x0000000180167000` | 0x164400 |
| `.reloc` | 0x3eb4 | `0x0000000180168000` | 0x164a00 |

## Dependencies

- `ADVAPI32.dll`: 9 named imports
- `KERNEL32.dll`: 71 named imports
- `SHELL32.dll`: 1 named imports
- `SHLWAPI.dll`: 10 named imports
- `USER32.dll`: 2 named imports
- `XmlLite.dll`: 1 named imports
- `msvcrt.dll`: 100 named imports
- `ntdll.dll`: 4 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/perf_nt.dll.objdump.txt`.
