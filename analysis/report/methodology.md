# Methodology and reproducibility

## Scope and evidence policy

`bin/` is read-only. Findings labelled **verified** derive from hashes, PE fields, import/export tables, strings, or instructions and cite generated evidence. Inferences are explicitly labelled. Decompiled output is not original source. No binary was executed: these Windows 6.x components have broad OS integration and this Linux host lacks a controlled matching Windows VM.

## Environment

Analysis host: Debian 12 x86-64, Linux 6.1. GNU Binutils `objdump`/`strings` 2.40, Python 3.11.2, Node 22.22.3, npm 10.9.8. Ghidra, IDA, Rizin, Radare2, Wine, and a Windows debugger were not installed. This prevents trustworthy high-level native decompilation and dynamic validation; GNU objdump supplies PE structure and disassembly but no typed pseudocode.

## Structural parser

Phase 0 no longer depends on regex over GNU objdump text for section, import, export, or delay-load tables. `analysis/tools/pe.py` reads PE32/PE32+ bytes with the Python standard library and extracts:

- COFF and optional headers (ImageBase, subsystem, characteristics, linker/OS versions)
- Section table (virtual size, raw size, VMA, file offset, characteristics)
- Data directories, including CLR, delay-import, and debug
- Static IAT and delay-load IAT, including ordinal-only thunks
- Export Address Table names, ordinals, and forwarders
- CodeView `RSDS` PDB filename, GUID, and Age

GNU `objdump -x` output is still retained under `analysis/report/generated/*.objdump.txt` as the independent textual audit trail. When a parsed field and objdump text disagree, the raw objdump bytes-on-disk dump is the authority for GNU's view; the PE parser is the authority for in-file structure.

## REA assessment and actual use

REA repository `morluto/rea` was inspected at commit `fffb0741936067530d1ce9777461cd53e87398c2` (2026-10-14 checkout). README, `docs/cli.md`, `docs/reverse-engineering-tools.md`, `src/objdump/ObjdumpCommand.ts`, and the input schema were reviewed. REA 6.5.0 requires Node >=22.19 and supports native pseudocode only through a configured Hopper/Ghidra/IDA provider. Its caller-supplied GNU objdump adapter supports `file_headers`, `section_headers`, `symbols`, `relocations`, `dwarf`, `disassemble`, and `disassemble_all`; it preserves raw output and explicitly does not normalize a version-independent schema.

REA was executed, rather than merely cited:

```sh
python3 analysis/tools/rea_baseline.py
# equivalent:
npx -y rea-agents@6.5.0 --version
npx -y rea-agents@6.5.0 inspect-with-objdump "$PWD/bin/iexplore.exe" file_headers --json \
  > analysis/report/rea/iexplore-file-headers.json
npx -y rea-agents@6.5.0 inspect-with-objdump "$PWD/bin/iediagcmd.exe" disassemble --json \
  > analysis/report/rea/iediagcmd-disassembly.json
```

REA bound pre/post SHA-256 identity and captured GNU objdump evidence. The `iexplore.exe` result independently agrees with direct objdump and `pe.py`: PEI x86-64 / PE32+ and entry `0x1400019f0`. Re-running `file_headers` still reports digest `cff801d6dc847bb832d0077ce38ddb66ef5b4637ff947bbdbc228eef10494f97` and `artifact_changed: false`. The managed `iediagcmd.exe` disassembly was selected as a bounded representative full-image run. `analysis/report/rea/iexplore-headers.json` intentionally retains the failed trial using unsupported operation `headers`; its validation error demonstrates that operation names were verified, not invented.

REA did **not** decompile these PE files because no supported deep native provider is available. Its built-in managed parser is applicable to `iediagcmd.exe`, but comprehensive CIL semantic extraction remains pending; the current evidence confirms a CLR header (`RVA 0x2008`, size `0x48`) and `_CorExeMain`. REA's Go/Rust/ELF diagnostics are not applicable to the observed Windows PE set.

## Automated procedure

```sh
python3 analysis/tools/test_pe.py
python3 analysis/tools/inventory.py
python3 analysis/tools/verify_phase0.py
```

`inventory.py` recursively hashes all inputs, classifies files by magic bytes, invokes `objdump -x` without a shell, parses PE images with `pe.py`, retains raw output in `analysis/report/generated/`, and generates inventory/API JSON and Markdown plus per-image evidence ledgers in `src/`. The script refuses to write inside `bin/`.

## Limitations

PE timestamps are untrusted metadata. Imported names establish linkage, not signatures or runtime invocation. Absence from static imports does not exclude delay-loading or `GetProcAddress`; delay-load descriptors are now recovered, but `GetProcAddress` targets are not. Resource directory presence does not decode every resource payload. Function-level coverage cannot be claimed from section-wide disassembly. Dynamic behavior requires an isolated, licensed Windows 7/8.1-compatible VM with matching dependencies and debugger instrumentation.
