# Data formats and structures

## Verified container facts

All 49 executable/resource images begin with DOS `MZ` and are accepted by GNU BFD as PE/COFF (`pei-x86-64` for native code, `pei-i386` for MUI images and managed `iediagcmd.exe`). Section names, virtual addresses, sizes, and file offsets are recorded per module. Security-directory data, relocations, exception tables, imports, exports, and resources are exposed where present in raw objdump evidence.

`iediagcmd.exe` has CLR runtime directory RVA `0x2008`, size `0x48`; its native import table names only `mscoree.dll!_CorExeMain`. This verifies a CLI/CLR bootstrap but does not by itself recover assembly types.

## Non-PE formats

`Timeline.cpu.xml` and `ie9props.propdesc` are XML-family text; EULAs are RTF; `images/bing.ico` is an icon container; `SIGNUP/install.ins` is installation configuration. Their SHA-256 and sizes are recorded. No proprietary binary container specification has yet been established from cross-referenced parser code, so no guessed layouts, checksums, or structure packing are asserted.

## Required next evidence

A defensible format specification requires locating parser functions, tracing every bounds/encoding check, correlating constants with sample offsets, and validating malformed cases. This needs Ghidra/IDA or equivalent and controlled tests; currently available header evidence is insufficient.