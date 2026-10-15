# Dependencies

Machine-readable edges are in `analysis/report/generated/dependencies.json`.
Symbol names are listed in `api-map.md`. A static or delay-load import records linkage, not a proven runtime call.

## Graph size

- Static import edges: **218**
- Delay-load import edges: **27**
- Distinct static targets: **33**
- Distinct delay-load targets: **19**

## Most-referenced static DLLs

| Imported module | Importers |
|---|---:|
| `KERNEL32.dll` | 28 |
| `msvcrt.dll` | 22 |
| `ole32.dll` | 20 |
| `OLEAUT32.dll` | 20 |
| `USER32.dll` | 20 |
| `ADVAPI32.dll` | 16 |
| `SHLWAPI.dll` | 11 |
| `iertutil.dll` | 10 |
| `urlmon.dll` | 8 |
| `RPCRT4.dll` | 7 |
| `ntdll.dll` | 6 |
| `GDI32.dll` | 5 |
| `OLEACC.dll` | 5 |
| `SHELL32.dll` | 5 |
| `MSIMG32.dll` | 4 |
| `WININET.dll` | 4 |
| `XmlLite.dll` | 3 |
| `api-ms-win-downlevel-advapi32-l1-1-0.dll` | 3 |
| `api-ms-win-downlevel-shlwapi-l1-1-0.dll` | 3 |
| `tdh.dll` | 2 |
| `UxTheme.dll` | 2 |
| `VERSION.dll` | 2 |
| `WindowsCodecs.dll` | 2 |
| `wer.dll` | 1 |
| `COMCTL32.dll` | 1 |
| `WINMM.dll` | 1 |
| `mscoree.dll` | 1 |
| `IEFRAME.dll` | 1 |
| `MSHTML.dll` | 1 |
| `AUTHZ.dll` | 1 |
| `WINTRUST.dll` | 1 |
| `api-ms-win-downlevel-shlwapi-l2-1-0.dll` | 1 |
| `api-ms-win-downlevel-shell32-l1-1-0.dll` | 1 |

## Delay-load targets

| Imported module | Importers |
|---|---:|
| `OLEAUT32.dll` | 3 |
| `ole32.dll` | 3 |
| `api-ms-win-downlevel-ole32-l1-1-0.dll` | 2 |
| `SHELL32.dll` | 2 |
| `USER32.dll` | 2 |
| `VERSION.dll` | 2 |
| `ADVAPI32.dll` | 1 |
| `credui.dll` | 1 |
| `MPR.dll` | 1 |
| `GDI32.dll` | 1 |
| `iertutil.dll` | 1 |
| `PROPSYS.dll` | 1 |
| `IEFRAME.dll` | 1 |
| `WTSAPI32.dll` | 1 |
| `dbghelp.dll` | 1 |
| `Cabinet.dll` | 1 |
| `CRYPT32.dll` | 1 |
| `WINHTTP.dll` | 1 |
| `XmlLite.dll` | 1 |

## Per-image linkage

| Image | Static DLLs | Delay-load DLLs | Exports | CLR |
|---|---|---|---:|:---:|
| `bin/D3DCompiler_47.dll` | `ADVAPI32.dll`, `KERNEL32.dll`, `RPCRT4.dll`, `msvcrt.dll` | — | 29 | no |
| `bin/DiagnosticsHub.DataWarehouse.dll` | `KERNEL32.dll`, `OLEAUT32.dll`, `USER32.dll`, `ole32.dll` | — | 1 | no |
| `bin/DiagnosticsHub.ScriptedSandboxPlugin.dll` | `ADVAPI32.dll`, `KERNEL32.dll`, `OLEAUT32.dll`, `USER32.dll`, `ole32.dll` | — | 2 | no |
| `bin/DiagnosticsHub_is.dll` | `KERNEL32.dll`, `OLEAUT32.dll`, `msvcrt.dll`, `ole32.dll`, `tdh.dll` | — | 4 | no |
| `bin/DiagnosticsTap.dll` | `ADVAPI32.dll`, `KERNEL32.dll`, `OLEAUT32.dll`, `SHLWAPI.dll`, `USER32.dll`, `msvcrt.dll`, `ole32.dll`, `urlmon.dll` | — | 5 | no |
| `bin/F12.dll` | `ADVAPI32.dll`, `GDI32.dll`, `KERNEL32.dll`, `MSIMG32.dll`, `OLEACC.dll`, `OLEAUT32.dll`, `SHELL32.dll`, `SHLWAPI.dll`, `USER32.dll`, `UxTheme.dll`, `VERSION.dll`, `WindowsCodecs.dll`, `XmlLite.dll`, `iertutil.dll`, `msvcrt.dll`, `ole32.dll`, `urlmon.dll`, `wer.dll` | — | 5 | no |
| `bin/F12Resources.dll` | `KERNEL32.dll` | — | 0 | no |
| `bin/F12Tools.dll` | `ADVAPI32.dll`, `COMCTL32.dll`, `KERNEL32.dll`, `OLEAUT32.dll`, `SHELL32.dll`, `SHLWAPI.dll`, `USER32.dll`, `msvcrt.dll`, `ole32.dll` | — | 5 | no |
| `bin/IEShims.dll` | `KERNEL32.dll`, `api-ms-win-downlevel-advapi32-l1-1-0.dll`, `api-ms-win-downlevel-shlwapi-l1-1-0.dll`, `iertutil.dll`, `msvcrt.dll`, `ntdll.dll` | `ADVAPI32.dll`, `MPR.dll`, `OLEAUT32.dll`, `SHELL32.dll`, `USER32.dll`, `api-ms-win-downlevel-ole32-l1-1-0.dll`, `credui.dll` | 10 | no |
| `bin/JSProfilerCore.dll` | `ADVAPI32.dll`, `KERNEL32.dll`, `OLEAUT32.dll`, `USER32.dll`, `WINMM.dll`, `iertutil.dll`, `msvcrt.dll`, `ole32.dll` | — | 2 | no |
| `bin/MemoryAnalyzer.dll` | `KERNEL32.dll`, `OLEAUT32.dll`, `USER32.dll`, `msvcrt.dll`, `ole32.dll` | — | 2 | no |
| `bin/Timeline.dll` | `KERNEL32.dll`, `OLEAUT32.dll`, `SHLWAPI.dll`, `USER32.dll`, `msvcrt.dll`, `ole32.dll` | — | 2 | no |
| `bin/Timeline_is.dll` | `KERNEL32.dll`, `OLEAUT32.dll`, `RPCRT4.dll`, `SHLWAPI.dll`, `USER32.dll`, `XmlLite.dll`, `msvcrt.dll`, `ole32.dll`, `tdh.dll` | — | 4 | no |
| `bin/en-US/DiagnosticsTap.dll.mui` | — | — | 0 | no |
| `bin/en-US/F12.dll.mui` | — | — | 0 | no |
| `bin/en-US/F12Resources.dll.mui` | — | — | 0 | no |
| `bin/en-US/F12Tools.dll.mui` | — | — | 0 | no |
| `bin/en-US/iedvtool.dll.mui` | — | — | 0 | no |
| `bin/en-US/ieinstal.exe.mui` | — | — | 0 | no |
| `bin/en-US/iexplore.exe.mui` | — | — | 0 | no |
| `bin/en-US/jsdbgui.dll.mui` | — | — | 0 | no |
| `bin/en-US/jsprofilerui.dll.mui` | — | — | 0 | no |
| `bin/en-US/networkinspection.dll.mui` | — | — | 0 | no |
| `bin/iediagcmd.exe` | `mscoree.dll` | — | 0 | yes |
| `bin/iedvtool.dll` | `ADVAPI32.dll`, `GDI32.dll`, `IEFRAME.dll`, `KERNEL32.dll`, `MSHTML.dll`, `MSIMG32.dll`, `OLEACC.dll`, `OLEAUT32.dll`, `SHELL32.dll`, `SHLWAPI.dll`, `USER32.dll`, `UxTheme.dll`, `WININET.dll`, `iertutil.dll`, `msvcrt.dll`, `ole32.dll`, `urlmon.dll` | — | 4 | no |
| `bin/ieinstal.exe` | `ADVAPI32.dll`, `AUTHZ.dll`, `KERNEL32.dll`, `OLEAUT32.dll`, `RPCRT4.dll`, `USER32.dll`, `WINTRUST.dll`, `iertutil.dll`, `msvcrt.dll`, `ntdll.dll`, `ole32.dll`, `urlmon.dll` | — | 0 | no |
| `bin/ielowutil.exe` | `KERNEL32.dll`, `USER32.dll`, `WININET.dll`, `iertutil.dll`, `msvcrt.dll`, `ntdll.dll`, `ole32.dll` | — | 0 | no |
| `bin/ieproxy.dll` | `KERNEL32.dll`, `RPCRT4.dll`, `api-ms-win-downlevel-advapi32-l1-1-0.dll`, `api-ms-win-downlevel-shlwapi-l1-1-0.dll`, `api-ms-win-downlevel-shlwapi-l2-1-0.dll`, `msvcrt.dll` | `GDI32.dll`, `OLEAUT32.dll`, `PROPSYS.dll`, `SHELL32.dll`, `USER32.dll`, `api-ms-win-downlevel-ole32-l1-1-0.dll`, `iertutil.dll`, `ole32.dll` | 5 | no |
| `bin/iexplore.exe` | `KERNEL32.dll`, `USER32.dll`, `api-ms-win-downlevel-advapi32-l1-1-0.dll`, `api-ms-win-downlevel-shell32-l1-1-0.dll`, `api-ms-win-downlevel-shlwapi-l1-1-0.dll`, `iertutil.dll`, `msvcrt.dll` | `IEFRAME.dll` | 0 | no |
| `bin/jsdbgui.dll` | `ADVAPI32.dll`, `GDI32.dll`, `KERNEL32.dll`, `MSIMG32.dll`, `OLEACC.dll`, `OLEAUT32.dll`, `SHLWAPI.dll`, `USER32.dll`, `iertutil.dll`, `msvcrt.dll`, `ole32.dll`, `urlmon.dll` | — | 3 | no |
| `bin/jsdebuggeride.dll` | `ADVAPI32.dll`, `KERNEL32.dll`, `OLEAUT32.dll`, `SHLWAPI.dll`, `USER32.dll`, `WININET.dll`, `msvcrt.dll`, `ole32.dll`, `urlmon.dll` | — | 2 | no |
| `bin/jsprofilerui.dll` | `ADVAPI32.dll`, `GDI32.dll`, `KERNEL32.dll`, `OLEACC.dll`, `OLEAUT32.dll`, `SHLWAPI.dll`, `USER32.dll`, `iertutil.dll`, `msvcrt.dll`, `ole32.dll`, `urlmon.dll` | — | 1 | no |
| `bin/msdbg2.dll` | `KERNEL32.dll`, `OLEAUT32.dll`, `RPCRT4.dll`, `ole32.dll` | — | 4 | no |
| `bin/networkinspection.dll` | `ADVAPI32.dll`, `GDI32.dll`, `KERNEL32.dll`, `MSIMG32.dll`, `OLEACC.dll`, `OLEAUT32.dll`, `SHELL32.dll`, `SHLWAPI.dll`, `USER32.dll`, `VERSION.dll`, `WININET.dll`, `WindowsCodecs.dll`, `iertutil.dll`, `msvcrt.dll`, `ole32.dll`, `urlmon.dll` | — | 1 | no |
| `bin/pdm.dll` | `ADVAPI32.dll`, `KERNEL32.dll`, `OLEAUT32.dll`, `USER32.dll`, `ole32.dll` | `VERSION.dll`, `WTSAPI32.dll` | 4 | no |
| `bin/pdmproxy100.dll` | `KERNEL32.dll`, `OLEAUT32.dll`, `RPCRT4.dll` | — | 4 | no |
| `bin/perf_nt.dll` | `ADVAPI32.dll`, `KERNEL32.dll`, `SHELL32.dll`, `SHLWAPI.dll`, `USER32.dll`, `XmlLite.dll`, `msvcrt.dll`, `ntdll.dll` | `OLEAUT32.dll`, `VERSION.dll`, `dbghelp.dll`, `ole32.dll` | 4 | no |
| `bin/perfcore.dll` | `ADVAPI32.dll`, `KERNEL32.dll`, `OLEAUT32.dll`, `msvcrt.dll`, `ntdll.dll`, `ole32.dll` | — | 4 | no |
| `bin/pt-BR/DiagnosticsTap.dll.mui` | — | — | 0 | no |
| `bin/pt-BR/F12.dll.mui` | — | — | 0 | no |
| `bin/pt-BR/F12Resources.dll.mui` | — | — | 0 | no |
| `bin/pt-BR/F12Tools.dll.mui` | — | — | 0 | no |
| `bin/pt-BR/iedvtool.dll.mui` | — | — | 0 | no |
| `bin/pt-BR/ieinstal.exe.mui` | — | — | 0 | no |
| `bin/pt-BR/iexplore.exe.mui` | — | — | 0 | no |
| `bin/pt-BR/jsdbgui.dll.mui` | — | — | 0 | no |
| `bin/pt-BR/jsprofilerui.dll.mui` | — | — | 0 | no |
| `bin/pt-BR/networkinspection.dll.mui` | — | — | 0 | no |
| `bin/sqmapi.dll` | `ADVAPI32.dll`, `KERNEL32.dll`, `RPCRT4.dll`, `USER32.dll`, `msvcrt.dll`, `ntdll.dll` | `CRYPT32.dll`, `Cabinet.dll`, `WINHTTP.dll`, `XmlLite.dll`, `ole32.dll` | 63 | no |

## Verified patterns

Native modules predominantly import Windows system facilities (`KERNEL32`, `USER32`, `ADVAPI32`, `OLE32`, `OLEAUT32`, `RPCRT4`, `SHLWAPI`) and the Microsoft C runtime. COM-style exports (`DllGetClassObject`, `DllCanUnloadNow`, registration entrypoints) occur throughout the diagnostics/tooling DLL set.

`iediagcmd.exe` depends on `mscoree.dll!_CorExeMain`, making the CLR a verified runtime prerequisite. The MUI satellites have empty import tables and are associated to base modules by filename/locale convention (an inferred deployment relationship).

Delay-load descriptors are present on `iexplore.exe` (`IEFRAME.dll`, ordinal-only), `IEShims.dll`, `ieproxy.dll`, `pdm.dll`, `perf_nt.dll`, and `sqmapi.dll`. Those edges were missing from the previous objdump-regex graph.

## Dynamic-resolution caveat

`LoadLibrary*` and `GetProcAddress` imports occur in the corpus, so the static plus delay-load graph is still a lower bound. Recovering dynamically constructed module/symbol names requires string cross-references or runtime tracing and is out of scope for Phase 0.
