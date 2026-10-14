# DiagnosticsHub.ScriptedSandboxPlugin.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `d74c75ced0f3257797edf7050195938cae23765125688f758a8fccb099a69b42` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x0000000180021ce0`
- Timestamp field: `Tue Dec 17 00:37:56 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `00046768` | 0x0 | `0x00000000` | 0x46330 |
| `00000000` | 0x0 | `0x00000000` | 0x0 |
| `.text` | 0x3d968 | `0x0000000180001000` | 0x400 |
| `.data` | 0x1a00 | `0x000000018003f000` | 0x3de00 |
| `.pdata` | 0x23b8 | `0x0000000180043000` | 0x3f800 |
| `.idata` | 0xfe8 | `0x0000000180046000` | 0x41c00 |
| `.rsrc` | 0x490 | `0x0000000180047000` | 0x42c00 |
| `.reloc` | 0x518 | `0x0000000180048000` | 0x43200 |

## Dependencies

- `ADVAPI32.dll`: 3 named imports
- `KERNEL32.dll`: 88 named imports
- `OLEAUT32.dll`: 1 named imports
- `USER32.dll`: 11 named imports
- `ole32.dll`: 4 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/DiagnosticsHub.ScriptedSandboxPlugin.dll.objdump.txt`.
