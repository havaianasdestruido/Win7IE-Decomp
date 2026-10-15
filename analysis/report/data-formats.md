# Data formats and structures

## Verified container facts

All 49 executable/resource images begin with DOS `MZ` and parse as PE/COFF:

| Class | Count | Format | Machine | Typical ImageBase |
|---|---:|---|---|---|
| Native code EXE/DLL | 28 | PE32+ | `IMAGE_FILE_MACHINE_AMD64` | `0x140000000` (EXE) / `0x180000000` (DLL) |
| Managed CLI EXE | 1 | PE32 | `IMAGE_FILE_MACHINE_I386` | `0x400000` |
| MUI resource satellites | 20 | PE32 | `IMAGE_FILE_MACHINE_I386` | resource-only, entry RVA 0 |

Section names, virtual addresses, virtual/raw sizes, file offsets, and characteristics are recorded per module in `src/<module>/README.md` and `generated/pe-struct.json`. Non-empty data directories (export, import, resource, exception `.pdata`, security, reloc, debug, load config, IAT, delay-import, CLR) are listed explicitly. The Security directory `VirtualAddress` field is a **file offset** (certificate table), not an RVA; `iediagcmd.exe` is the canonical example where Security file offset `0x54000` coincides numerically with the BaseReloc RVA.

`iediagcmd.exe` has CLR runtime directory RVA `0x2008`, size `0x48`; its native import table names only `mscoree.dll!_CorExeMain`. This verifies a CLI/CLR bootstrap but does not by itself recover assembly types.

Delay-import directories are present on six images. `iexplore.exe` delay-loads `IEFRAME.dll` by ordinal (5 thunks). Other delay-load targets include `WINHTTP`, `CRYPT32`, `Cabinet`, `dbghelp`, `WTSAPI32`, and additional OLE/shell APIs.

Every one of the 29 code images carries a CodeView `RSDS` debug record (PDB filename, GUID, Age) indexed in `generated/debug-rsds.json`. The 20 `.mui` satellites have no debug directory.

## Non-PE formats

Magic-byte classification of the eight non-PE files:

| Path | Bytes | Kind | Magic |
|---|---:|---|---|
| `bin/Timeline.cpu.xml` | 3,197 | XML | `<?xml` |
| `bin/ie9props.propdesc` | 2,843 | XML | UTF-8 BOM + `<?xml` |
| `bin/SIGNUP/install.ins` | 464 | UTF-16LE text | `FF FE` + `[Branding]` |
| `bin/en-US/eula.rtf` | 118,526 | RTF | `{\rtf1` |
| `bin/pt-BR/eula.rtf` | 116,663 | RTF | `{\rtf1` |
| `bin/images/bing.ico` | 5,430 | ICO | `00 00 01 00` (2 directory entries) |
| `bin/LICENSE` | 1,211 | text | ASCII |
| `bin/README.md` | 8 | text | `# Win7IE` |

Their SHA-256 and sizes are recorded. No proprietary binary container specification has yet been established from cross-referenced parser code, so no guessed layouts, checksums, or structure packing are asserted beyond these container identities.

## Required next evidence

A defensible on-disk format specification for SQM sessions, F12 resource blobs, and MUI payloads requires locating parser functions, tracing every bounds/encoding check, correlating constants with sample offsets, and validating malformed cases. This needs Ghidra/IDA or equivalent and controlled tests; currently available header evidence is insufficient.
