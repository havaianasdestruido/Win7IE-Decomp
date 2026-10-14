# Module analysis

## Verified portfolio-level findings

The corpus contains 49 PE images: 28 x86-64 code images and 21 i386 resource satellites (`.mui`). All main DLL/EXE images except `iediagcmd.exe` are native PE32+ x86-64. `iediagcmd.exe` is PE32 i386 with a nonzero CLR runtime directory and imports `_CorExeMain` from `mscoree.dll`, verifying a managed entry path. Locale MUI files have entry point zero and no recovered named imports, consistent with resource-only satellites.

The native module set divides by observable names and dependencies into: Internet Explorer launch/setup (`iexplore`, `ieinstal`, `ielowutil`, `ieproxy`, `iedvtool`, `IEShims`); F12 developer tools (`F12`, `F12Tools`, `F12Resources`, diagnostics, timeline, memory, network, JavaScript debugger/profiler); debugging infrastructure (`pdm`, `pdmproxy100`, `msdbg2`); telemetry/performance (`sqmapi`, `perfcore`, `perf_nt`); and the separately shipped Direct3D compiler. These subsystem labels are **inferences from filenames and imported/exported interfaces**, not verified internal designs.

## Entrypoints and interfaces

Exact entry RVAs, sections, dependencies, exports, hashes, and timestamps are in each `src/<module>/README.md` and the generated JSON. `analysis/report/api-map.md` is the consolidated table. COM-style exports such as `DllGetClassObject`, `DllCanUnloadNow`, registration entrypoints, and proxy/stub exports are observable in many DLLs. Signature prototypes have not been asserted because export names alone do not prove parameter types.

`D3DCompiler_47.dll` exposes the recognizable D3D compiler surface (`D3DCompile`, `D3DReflect`, `D3DDisassemble`, and related exports). `sqmapi.dll` has the largest recovered named export set. Resource-only `F12Resources.dll` is the largest input by bytes. These are verified table/size observations.

## Function analysis status

REA/GNU objdump produced complete raw instruction output for `iediagcmd.exe`; this proves instruction coverage, not understood-function or pseudocode coverage. Native binaries are stripped of useful public function symbols in this environment. Assigning signatures, C++ object layouts, or algorithms without a decompiler and cross-reference engine would be speculative, so module ledgers intentionally contain no fabricated declarations.

## Resources and non-PE artifacts

Twenty locale resource images are paired across `en-US` and `pt-BR`. Two EULA RTF files, `Timeline.cpu.xml`, `ie9props.propdesc`, `SIGNUP/install.ins`, an icon, license, and short README were hashed and inventoried. Their semantic schemas and resource payload extraction remain outside current structural coverage; exact paths and identities are in `inventory.md`.