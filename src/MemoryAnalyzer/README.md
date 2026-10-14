# MemoryAnalyzer.dll

> Evidence status: header, section, and import/export facts below are verified against SHA-256 `eeff728c1f190f8febe04ad5312d7bdec285b7fe1bdd1f77684320d51202de3a` using GNU objdump. Function types and behavior have not been guessed.

## Image

- Format: `pei-x86-64`
- Architecture: `i386:x86-64`
- Entry point: `0x00000001801b2700`
- Timestamp field: `Tue Dec 17 00:50:49 2019` (untrusted PE metadata)
- CLR header present: `False`

## Sections

| Name | Size | VMA | File offset |
|---|---:|---:|---:|
| `.text` | 0x1be3d4 | `0x0000000180001000` | 0x400 |
| `.data` | 0x2200 | `0x00000001801c0000` | 0x1be800 |
| `.pdata` | 0x2cc4 | `0x00000001801c3000` | 0x1c0a00 |
| `.idata` | 0x1102 | `0x00000001801c6000` | 0x1c3800 |
| `.rsrc` | 0x17b8 | `0x00000001801c8000` | 0x1c4a00 |
| `.reloc` | 0x60c | `0x00000001801ca000` | 0x1c6200 |

## Dependencies

- `KERNEL32.dll`: 57 named imports
- `OLEAUT32.dll`: 1 named imports
- `USER32.dll`: 11 named imports
- `msvcrt.dll`: 47 named imports
- `ole32.dll`: 1 named imports

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/MemoryAnalyzer.dll.objdump.txt`.
