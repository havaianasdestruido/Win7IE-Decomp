# Progress and coverage

Updated: 2026-10-15.

| Work item | Coverage | Status / blocker |
|---|---:|---|
| Recursive inventory and SHA-256 | 57/57 files | Complete and reproducible (`hashes.json`) |
| Non-PE magic-byte classification | 8/8 files | RTF, ICO, UTF-16LE INI, XML, text |
| PE classification and architecture | 49/49 PE images | 28 PE32+ x86-64, 1 PE32 i386 CLR, 20 PE32 i386 MUI |
| Header/section/import/export extraction | 49/49 PE images | Stdlib PE parser + retained GNU objdump `-x` |
| Delay-load IAT extraction | 6/6 images with `.didat` / delay directory | `iexplore`, `IEShims`, `ieproxy`, `pdm`, `perf_nt`, `sqmapi` |
| Ordinal-only IAT numbers | 321 ordinal thunks | No longer recorded as name-unavailable |
| CodeView RSDS identity | 29/29 code images | PDB name/GUID/Age in `debug-rsds.json`; files not downloaded |
| REA repository/capability assessment | 1/1 requested tool | Complete at upstream commit and REA 6.5.0 |
| Actual REA execution | 2 representative valid runs + 1 validation failure | Complete; evidence retained; version re-checked 6.5.0 |
| Per-image source/evidence directories | 49/49 PE images | Complete; export names commented, no fabricated code |
| Native function disassembly | 1/29 code images | `iediagcmd.exe` captured through REA; remaining 28 require large batch artifacts |
| Managed metadata/CIL semantics | 0 understood methods | CLR bootstrap identified; run REA managed member workflows next |
| Native typed decompilation | 0 verified functions | Blocked: no Ghidra/IDA/Hopper provider installed |
| Dynamic behavior | 0 modules | Blocked: no controlled matching Windows VM/debugger |
| Resource payload decoding | 0/20 MUI payload sets | Directory-level PE structure only |
| Compatibility implementations/builds | 0 modules | Insufficient behavior evidence; CMake targets would be meaningless |

## Exact unresolved work

1. Install/configure a REA-supported Ghidra provider, import each of 28 native code images, retain provider/version/options, enumerate functions, and decompile by subsystem priority.
2. Query the Microsoft Public Symbol Server with the recovered RSDS GUID+Age tuples and parse the returned PDBs.
3. Run `inspect-managed-artifact` and `inspect-managed-members` on `iediagcmd.exe`, then map CIL methods and strings.
4. Decode PE resources from base and MUI modules and correlate resource IDs across locales.
5. Find `LoadLibrary`/`GetProcAddress` cross-references to extend the dependency graph beyond static + delay-load.
6. Establish an isolated Windows test image with matching IE dependencies; capture registry, filesystem, COM, process, and network effects without exposing production systems.
7. Only after signatures/behavior are validated, create clean-room compatibility targets and CMake builds.

No module is marked fully decompiled or behaviorally validated. For the complete, phase-divided checklist required for a faithful 1:1 decompilation and clean-room reconstruction across all 57 corpus artifacts, see [`TODO.md`](../../TODO.md) (cited in the root [`README.md`](../../README.md)).
