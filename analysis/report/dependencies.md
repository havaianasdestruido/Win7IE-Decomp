# Dependencies

Machine-readable edges are in `analysis/report/generated/dependencies.json`; symbols are listed in `api-map.md`.

## Verified patterns

Native modules predominantly import Windows system facilities (`KERNEL32`, `USER32`, `ADVAPI32`, `OLE32`, `OLEAUT32`, `RPCRT4`, `SHLWAPI`) and the Microsoft C runtime. COM-style exports occur throughout the diagnostics/tooling DLL set. Imports of project-adjacent IE components establish candidate runtime edges, but a static import does not prove a call executes.

`iediagcmd.exe` depends on `mscoree.dll!_CorExeMain`, making the CLR a verified runtime prerequisite. The MUI satellites have no named imports recovered and are associated to base modules by filename/locale convention (an inferred deployment relationship).

## Dynamic-resolution caveat

`LoadLibrary*` and `GetProcAddress` imports occur in the corpus, so the static graph is a lower bound. Recovering dynamically constructed module/symbol names requires string cross-references or runtime tracing with a deep provider. Raw import evidence is retained per image.