# Clean-Room 1:1 Decompilation & Reconstruction Roadmap (`TODO.md`)

This document defines the complete, phase-divided engineering roadmap required to achieve a **faithful 1:1 decompilation and clean-room reconstruction** of the Windows 7 Internet Explorer 11 (`11.00.9600.19597`) application, F12 Developer Tools suite, Process Debug Manager (PDM), Diagnostics Hub, Direct3D Shader Compiler, and SQM/ETW telemetry services contained in `bin/`.

> **Read-Only Corpus Policy:** All 57 original artifacts in `bin/` (30,617,822 bytes; 49 PE/COFF images and 8 configuration/schema/resource files) are immutable reference inputs locked by SHA-256 in [`analysis/report/inventory.md`](./analysis/report/inventory.md). No file in `bin/` may be modified.

---

## Clean-Room Governance & Methodology

To guarantee legal and technical defensibility while achieving 1:1 behavioral and ABI fidelity, work is separated into two strictly isolated workflows:

1. **Dirty-Room (Reverse Engineering & Formal Specification — `analysis/`):**
   - Inspects original binaries in `bin/` using static disassemblers/decompilers (`objdump`, REA, Ghidra, IDA, ILSpy) and controlled dynamic instrumentation (WinDbg, ETW, API Monitor in an isolated Windows 7 SP1 x64 VM).
   - Produces **implementation-independent technical specifications**: exact function prototypes, calling conventions, COM interface definitions (`.idl`), vftable layouts, data structures, state machines, algorithms, error-handling contracts (`HRESULT`/SEH), and black-box test vectors.
   - Never copies raw decompiler pseudocode or copyrighted assembly directly into `src/`.

2. **Clean-Room (Implementation & Verification — `src/`):**
   - Implements compilable C, C++, C#, IDL, and Resource Script (`.rc`) source code in `src/<module>/` strictly from the validated specifications and public Windows SDK documentation.
   - Compiles and links artifacts against target toolchains and validates 1:1 structural, ABI, and behavioral equivalence against the reference corpus.

---

## Phase Overview & Progress Summary

| Phase | Title | Scope | Status |
| :--- | :--- | :--- | :--- |
| **Phase 0** | **Corpus Inventory, Cryptographic Locking & Structural Baseline** | 57/57 files hashed; 49/49 PE headers, sections, static imports/exports extracted; module ledgers created | **Complete** |
| **Phase 1** | **Deep Decompilation Toolchain, Symbol/PDB Recovery & Unwind/RTTI Mapping** | Ghidra/REA native provider setup, Microsoft Symbol Server PDB harvesting, `.pdata`/`.xdata` function bounds, C++ RTTI/vtable recovery | **Pending** (1/29 code images disassembled) |
| **Phase 2** | **Non-PE Schemas, Configurations & PE Resource (`.rsrc` / `.mui`) Extraction** | 8 non-PE files, 20 locale `.mui` satellites (`en-US`, `pt-BR`), `F12Resources.dll` (10.95 MB), and embedded `.rsrc` trees -> `.rc` scripts | **Pending** (Directory-level only) |
| **Phase 3** | **Managed (.NET / CLR) Decompilation & Clean-Room Reconstruction** | `bin/iediagcmd.exe` (PE32 i386 CLR binary): CIL metadata/method recovery, specification, and clean-room C# implementation | **Pending** (Bootstrap & raw disassembly captured) |
| **Phase 4** | **COM, RPC/NDR Proxy-Stub, Delay-Load & Ordinal Interface Recovery** | Resolve ordinal imports, `.didat` delay-loads, `GetProcAddress` edges, and reconstruct `.idl` files for 19 COM servers & 3 RPC proxies | **Pending** |
| **Phase 5** | **Native x86-64 Decompilation & Formal Specification (28 PE32+ Modules)** | Function-level decompilation, type recovery, and clean-room specs across all 6 native subsystems (5A–5F) | **Pending** |
| **Phase 6** | **Clean-Room Source Reconstruction & Reproducible Build System** | C/C++/C#/IDL/RC implementation under `src/<module>/`, `.def` export maps, and CMake/MSVC build pipeline | **Pending** |
| **Phase 7** | **Dynamic Tracing, Behavioral Parity & 1:1 Verification Harness** | Isolated Win7 SP1 x64 VM dynamic validation, ABI/COM contract tests, UI/ETW/IPC parity, and binary diffing | **Pending** |

---

## Phase 0: Corpus Inventory, Cryptographic Locking & Structural Baseline (Completed)

**Objective:** Establish a deterministic, auditable inventory of every input artifact and extract baseline PE/COFF structural evidence without fabricating unverified code.

- [x] **0.1 Recursive Cryptographic Inventory:** Hash all 57 files (30,617,822 bytes) in `bin/` using SHA-256 and record sizes, magic bytes, and file classifications in `analysis/report/inventory.md` and `analysis/report/generated/inventory.json` via `analysis/tools/inventory.py`.
- [x] **0.2 PE/COFF Structural Extraction:** Parse all 49 PE images (28 x86-64 native code images, 1 i386 CLR image, 20 i386 `.mui` resource satellites) with GNU `objdump -x` and retain authoritative raw outputs in `analysis/report/generated/*.objdump.txt`.
- [x] **0.3 Static API & Dependency Mapping:** Extract static Import Address Tables (IAT) and Export Address Tables (EAT) across all 49 PE images into `analysis/report/api-map.md`, `analysis/report/dependencies.md`, and `analysis/report/generated/dependencies.json`.
- [x] **0.4 Reverse Engineering Assistant (REA) Integration Baseline:** Validate `rea-agents@6.5.0` adapter workflows, capture verified PE header evidence for `bin/iexplore.exe` (`analysis/report/rea/iexplore-file-headers.json`), and capture complete instruction disassembly for `bin/iediagcmd.exe` (`analysis/report/rea/iediagcmd-disassembly.json`).
- [x] **0.5 Per-Module Evidence Ledgers:** Initialize all 49 module directories under `src/<module>/` with `README.md` (verified image metadata, sections, imports/exports) and placeholder `interfaces.h`.

**Exit Criteria (Met):** 100% file hash coverage, 100% PE header/section/static-table extraction, zero modified bytes in `bin/`.

---

## Phase 1: Deep Decompilation Toolchain, Symbol/PDB Recovery & Unwind/RTTI Mapping

**Objective:** Provision deep static analysis backends and extract deterministic function boundaries, debug symbols, exception handling scopes, and C++ object layouts across all 28 native x86-64 binaries and 1 managed binary.

### 1.1 Decompiler & Analysis Backend Provisioning
- [ ] Configure a headless native decompiler provider (Ghidra >= 11.x or IDA Pro / Rizin with Ghidra decompiler plugin) and bind it to `rea-agents` so typed pseudocode and control-flow graphs (CFGs) can be exported deterministically.
- [ ] Provision a .NET/CIL metadata and decompilation toolkit (`ilspycmd`, `dnSpy`, `ildasm`, or `dotnet-ilverify`) for managed inspection of `bin/iediagcmd.exe`.
- [ ] Provision PE resource and manifest extraction utilities (`wrestool`, `icoutils`, `python-pefile`, `LIEF`, and Windows SDK `rc.exe` / `llvm-rc`).

### 1.2 Debug Directory (`IMAGE_DIRECTORY_ENTRY_DEBUG`) & Public PDB Recovery
- [ ] Write an automated script (`analysis/tools/extract_debug_info.py`) to parse the PE Debug Directory of all 49 PE images and extract CodeView `RSDS` records (PDB filename, GUID, Age, timestamp).
- [ ] Query the Microsoft Public Symbol Server (`https://msdl.microsoft.com/download/symbols`) using the extracted `RSDS` GUID+Age tuples to retrieve official public `.pdb` files (e.g., `iexplore.pdb`, `iedvtool.pdb`, `f12.pdb`, `f12tools.pdb`, `pdm.pdb`, `msdbg2.pdb`, `sqmapi.pdb`, `d3dcompiler_47.pdb`, etc.).
- [ ] Parse retrieved PDB streams (Public Symbols, Global Symbols, Module Info, Frame Pointer Omission / Unwind data, and any exposed Type Info `TPI`/`IPI` streams) into machine-readable JSON under `analysis/report/generated/symbols/`.

### 1.3 Deterministic Function Enumeration via `.pdata` & `.xdata`
- [ ] Parse the x86-64 Exception Directory (`.pdata` `RUNTIME_FUNCTION` arrays: `BeginAddress`, `EndAddress`, `UnwindInfoAddress`) across all 28 PE32+ images to build an exact, non-speculative catalog of every non-leaf function.
- [ ] Parse `.xdata` `UNWIND_INFO` structures, prologue stack allocations (`UWOP_ALLOC_SMALL`, `UWOP_ALLOC_LARGE`, `UWOP_PUSH_NONVOL`), and language-specific exception handlers (`__C_specific_handler`, `__CxxFrameHandler3`, `__CxxFrameHandler`, `_XcptFilter`).
- [ ] Recover C++ `FuncInfo` (`_s_FuncInfo`), `TryBlockMapEntry`, `HandlerType`, and `UnwindMapEntry` tables for every function using `__CxxFrameHandler3` to map exact `try`/`catch` scopes and automatic local object destructors (RAII).
- [ ] Identify leaf functions and thunks in `.text` gaps between `.pdata` entries via call-target (`E8`/`FF 15`) and jump-table cross-references.

### 1.4 C++ RTTI, Virtual Tables & CRT Startup Recovery
- [ ] Scan `.rdata` / `.data` across all C++ modules for MSVC 64-bit RTTI structures (`_RTTICompleteObjectLocator` with signature `1`, `_RTTITypeDescriptor`, `_RTTIClassHierarchyDescriptor`, `_RTTIBaseClassArray`, `_RTTIBaseClassDescriptor`).
- [ ] Demangle all RTTI class names and `msvcrt.dll` C++ imports (`__unDName` / `llvm-undname`) and map every virtual function table (`vftable`) to its owning C++ class and inheritance tree (including multiple/virtual inheritance offsets).
- [ ] Isolate standard Visual C++ CRT startup/initialization boilerplate (`_CRT_INIT`, `_DllMainCRTStartup`, `__tmainCRTStartup`, `_initterm`, `__dllonexit`, `/GS` security cookie `__security_init_cookie` & `__security_check_cookie`) from user/application functions in every binary.

**Exit Criteria:** Complete function inventory (with exact start/end RVAs and symbol names where PDBs exist) and full vtable/RTTI class catalogs generated for all 29 code images.

---

## Phase 2: Non-PE Schemas, Configurations & PE Resource (`.rsrc` / `.mui`) Extraction

**Objective:** Fully decode, document, and reconstruct all non-code files, embedded PE resource trees, and localized MUI satellite payloads required for 1:1 asset and UI parity.

### 2.1 Non-PE Support & Configuration Files (8 Files)
- [ ] **`bin/Timeline.cpu.xml` (3,197 bytes):** Document the `<TimelineTags>` XML schema, ETW provider `Microsoft-IE` (`{9e3b3947-ca5d-4614-91a2-7b624e0e7244}`), and all 6 category tag definitions (`Loading_Category`, `Scripting_Category`, `GC_Category`, `Styling_Category`, `Rendering_Category`, `ImageDecoding_Category`) along with their start/stop event IDs and tasks consumed by `Timeline_is.dll`.
- [ ] **`bin/ie9props.propdesc` (2,843 bytes):** Document the Windows Property Description schema (`http://schemas.microsoft.com/windows/2006/propertydescription`) defining `Microsoft.IE.FeedItemLocalId` (`{E32596B0-1163-4E02-867A-12132DB4BA06}`) and `Microsoft.IE.SelectionCount`, `TargetUrl`, `TargetUrlHostName`, `TargetUrlPath`, `Title`, `VisitCount` (`{1CE0D6BC-536C-4600-B0DD-7E0C66B350D5}` propIDs 2–7) registered via `PSRegisterPropertySchema()`.
- [ ] **`bin/SIGNUP/install.ins` (464 bytes, UTF-16LE):** Document the `[Branding]` INI structure (`CompanyName=Microsoft Corporation`, `Wizard_Version=11.00.9600.19597`, `Custom_Key=MICROSO`, `GUID={7211FFE6-C149-11D0-AFF0-00AA003758BB}`, etc.) and trace which setup/initialization routines consume it.
- [ ] **`bin/en-US/eula.rtf` (118,526 bytes) & `bin/pt-BR/eula.rtf` (116,663 bytes):** Verify character encoding, RTF control structures, and installer/about-box references.
- [ ] **`bin/images/bing.ico` (5,430 bytes), `bin/LICENSE` (1,211 bytes), `bin/README.md` (8 bytes):** Document icon directory entries (resolutions, bit depths, PNG/BMP frames) and static packaging rules.

### 2.2 Base PE `.rsrc` Section Extraction & Analysis
- [ ] Build an automated PE resource extractor (`analysis/tools/extract_resources.py`) to dump and catalog all resource types (`RT_CURSOR`, `RT_BITMAP`, `RT_ICON`, `RT_MENU`, `RT_DIALOG`, `RT_STRING`, `RT_ACCELERATOR`, `RT_RCDATA`, `RT_MESSAGETABLE`, `RT_GROUP_CURSOR`, `RT_GROUP_ICON`, `RT_VERSION`, `RT_MANIFEST`, `RT_HTML`, `TYPELIB`, `REGISTRY`, and custom named types) from all 49 PE images.
- [ ] **Deconstruct `bin/F12Resources.dll` (10,949,120 bytes):** Extract all embedded F12 Developer Tools HTML/CSS/JavaScript UI bundles, localized string hooks, SVG/PNG/BMP icons, and layout templates that power the IE11 F12 UI (`F12.dll`, `MemoryAnalyzer.dll`, `Timeline.dll`, `DiagnosticsTap.dll`).
- [ ] Extract and parse all embedded SxS Application/Assembly Manifests (`RT_MANIFEST`) to document DPI awareness, Common Controls v6 (`Microsoft.Windows.Common-Controls`) dependencies, and UAC `requestedExecutionLevel` settings (`asInvoker` vs. `requireAdministrator`).
- [ ] Extract all `RT_VERSION` (`VS_VERSION_INFO`) structures (`FileVersion`, `ProductVersion`, `OriginalFilename`, `InternalName`, `Translation` tables) for 1:1 version resource reproduction.
- [ ] Extract all embedded ATL/COM registry scripts (`REGISTRY` / `.rgs` resources) and embedded TypeLibraries (`TYPELIB` / `MSFT` resources) used by `DllRegisterServer` / `DllInstall`.

### 2.3 Multilingual User Interface (MUI) Satellite Reconstruction (20 PE32 Images)
- [ ] Extract and cross-correlate resource IDs across all 10 paired `en-US` and `pt-BR` `.mui` satellite images:
  - [ ] `bin/en-US/DiagnosticsTap.dll.mui` & `bin/pt-BR/DiagnosticsTap.dll.mui`
  - [ ] `bin/en-US/F12.dll.mui` & `bin/pt-BR/F12.dll.mui`
  - [ ] `bin/en-US/F12Resources.dll.mui` & `bin/pt-BR/F12Resources.dll.mui`
  - [ ] `bin/en-US/F12Tools.dll.mui` & `bin/pt-BR/F12Tools.dll.mui`
  - [ ] `bin/en-US/iedvtool.dll.mui` & `bin/pt-BR/iedvtool.dll.mui`
  - [ ] `bin/en-US/ieinstal.exe.mui` & `bin/pt-BR/ieinstal.exe.mui`
  - [ ] `bin/en-US/iexplore.exe.mui` & `bin/pt-BR/iexplore.exe.mui`
  - [ ] `bin/en-US/jsdbgui.dll.mui` & `bin/pt-BR/jsdbgui.dll.mui`
  - [ ] `bin/en-US/jsprofilerui.dll.mui` & `bin/pt-BR/jsprofilerui.dll.mui`
  - [ ] `bin/en-US/networkinspection.dll.mui` & `bin/pt-BR/networkinspection.dll.mui`
- [ ] Decode the `MUI` resource configuration block (RCConfig magic `0xFECDFECD`, language-neutral checksum linkage to parent PE image, ultimate fallback location) in both parent binaries and `.mui` satellites.
- [ ] Generate clean-room `.rc` resource scripts under each `src/<module>/` and `src/<locale>_<module>_mui/` directory that compile back into matching `.rsrc` sections.

**Exit Criteria:** Every resource payload in all 49 PE images and all 20 `.mui` satellites is extracted, indexed by ID, mapped to call sites (`LoadStringW`, `FindResourceExW`, `CreateDialogParamW`, `LoadMenuW`, `LoadAcceleratorsW`), and convertible to compilable `.rc` sources.

---

## Phase 3: Managed (.NET / CLR) Decompilation & Clean-Room Reconstruction (`iediagcmd.exe`)

**Objective:** Complete 1:1 semantic recovery, specification, and clean-room C# reconstruction of the sole managed executable in the corpus (`bin/iediagcmd.exe`, 359,632 bytes, SHA-256 `412df2da4d524e6b78ed6c7bc595224643574510fba194ee940e495d981a6510`).

- [ ] **3.1 CLR Metadata & Stream Parsing:**
  - Parse the CLI Header (`IMAGE_COR20_HEADER` at RVA `0x2008`, size `0x48`), Metadata Root, and all metadata tables (`Module`, `TypeRef`, `TypeDef`, `Field`, `MethodDef`, `Param`, `InterfaceImpl`, `MemberRef`, `Constant`, `CustomAttribute`, `StandAloneSig`, `Property`, `Event`, `Assembly`, `AssemblyRef`, `ManifestResource`, `ImplMap`).
  - Run REA managed workflows (`inspect-managed-artifact` and `inspect-managed-members`) and export complete type/method inventories to `analysis/report/rea/iediagcmd-managed.json`.
- [ ] **3.2 Native Interop & Embedded Payload Recovery:**
  - Catalog every `ImplMap` P/Invoke declaration (`DllImport`), marshaling attribute (`MarshalAs`), `StructLayout`, and COM interop interface used by `iediagcmd.exe`.
  - Extract all `.resources` / `ManifestResource` streams embedded inside `iediagcmd.exe`.
- [ ] **3.3 Clean-Room Specification of `iediagcmd.exe`:**
  - Document the command-line syntax, exit codes, diagnostic data collectors (registry keys, system info, IE settings, crash logs, network/proxy state, DXDiag/ETW traces), output archive generation (`.cab`/`.zip`), and exception handling behavior.
- [ ] **3.4 Clean-Room C# Implementation:**
  - Reconstruct the C# source tree and `.csproj` under `src/iediagcmd/` targeting x86 (`PlatformTarget: x86`) and matching CLR runtime version.
  - Validate that the compiled assembly matches the original type/method signatures, CLI flags, and runtime diagnostic output.

**Exit Criteria:** `src/iediagcmd/` compiles cleanly into a standalone managed executable with verified 1:1 behavioral equivalence to `bin/iediagcmd.exe`.

---

## Phase 4: COM, RPC/NDR Proxy-Stub, Delay-Load & Ordinal Interface Recovery

**Objective:** Reconstruct all inter-module and OS-boundary contracts, including unnamed ordinal imports, delay-loaded dependencies, dynamic `GetProcAddress` lookups, COM class factories, and MIDL proxy/stub wire specifications.

### 4.1 Ordinal-Only Import Resolution
- [ ] Resolve all ordinal-only imports currently recorded as `(ordinal-only import; name unavailable)` in `analysis/report/api-map.md` against Windows 7 SP1 / IE11 export definitions (`.def` / `.lib` from Windows SDK & Win7 system DLLs):
  - [ ] **`OLEAUT32.dll` (1 ordinal across 21 modules):** Map exact ordinal numbers (e.g., `SysAllocString`, `SysFreeString`, `VariantInit`, `VariantClear`, `SafeArray*`, `SysStringLen`) per module import table in raw objdump/PE IAT.
  - [ ] **`SHLWAPI.dll` (ordinals in `F12.dll`, `F12Tools.dll`, `iedvtool.dll`, `jsdbgui.dll`, `jsdebuggeride.dll`, `jsprofilerui.dll`, `networkinspection.dll`, `perf_nt.dll`):** Resolve internal Shell Lightweight API ordinals against Windows 7 `shlwapi.dll`.
  - [ ] **`iertutil.dll` (ordinals in `F12.dll`, `IEShims.dll`, `iedvtool.dll`, `ieinstal.exe`, `ielowutil.exe`, `iexplore.exe`, `jsdbgui.dll`, `jsprofilerui.dll`, `networkinspection.dll`):** Resolve IE RunTime Utility ordinal exports (e.g., ISO/LCIE messaging, setting store, string/URI helpers).
  - [ ] **`urlmon.dll` (ordinals in `F12.dll`, `iedvtool.dll`, `ieinstal.exe`, `jsdbgui.dll`, `jsprofilerui.dll`):** Resolve URL Moniker ordinal exports.
  - [ ] **`IEFRAME.dll` & `MSHTML.dll` (ordinals in `iedvtool.dll`):** Resolve browser frame and Trident MSHTML private ordinal entrypoints.
  - [ ] **`SHELL32.dll` (ordinal in `iedvtool.dll`) & `COMCTL32.dll` (ordinal in `F12Tools.dll`):** Resolve Shell and Common Controls ordinals.

### 4.2 Delay-Load (`.didat`) & Dynamic Symbol Resolution (`LoadLibrary*` / `GetProcAddress`)
- [ ] Parse the Delay-Load Import Directory (`IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT` / `.didat` section) in `iexplore.exe`, `IEShims.dll`, `ieproxy.dll`, `sqmapi.dll`, and any other module with non-zero delay-load descriptors.
- [ ] Perform static data-flow slicing across all 28 native binaries for every call to `LoadLibraryA`, `LoadLibraryW`, `LoadLibraryExA`, `LoadLibraryExW`, `GetModuleHandleA`, `GetModuleHandleW`, `GetModuleHandleExW`, and `GetProcAddress` to recover dynamically resolved DLL and function names.
- [ ] Update `analysis/report/dependencies.md` and `analysis/report/generated/dependencies.json` with a complete static + delay-load + dynamic dependency graph.

### 4.3 COM Server Catalog & MIDL / RPC Proxy-Stub Reconstruction
- [ ] Extract all `CLSID`, `IID`, `LIBID`, and `CATID` 16-byte GUID structures from `.rdata`/`.data` and cross-reference them with `DllGetClassObject`, `CoCreateInstance`, `QISearch`, and ATL `OBJECT_ENTRY` tables across all 19 COM server DLLs.
- [ ] **Decompile RPC/NDR Proxy-Stub DLLs into Compilable `.idl` Files:**
  - [ ] **`bin/ieproxy.dll`:** Parse `GetProxyDllInfo` (`ProxyFileInfo **pProxyFileList, const CLSID **pclsid`), extract all `CInterfaceProxyVtbl` and `CInterfaceStubVtbl` structures, `IID` tables, interface names, method counts, and NDR64/NDR format strings (`NdrClientCall3`, `NdrStubCall3`), and reconstruct the clean-room IDL definitions.
  - [ ] **`bin/pdmproxy100.dll`:** Extract `ProxyFileInfo`, stub/proxy vtables, and `NdrStubCall2` format strings for Process Debug Manager v10.0 interfaces and reconstruct `pdmproxy100.idl`.
  - [ ] **`bin/msdbg2.dll`:** Extract `ProxyFileInfo`, `NdrClientCall2`/`NdrStubCall2` descriptors, and `HWND` user-marshal routines (`HWND_UserSize`, `HWND_UserMarshal`, `HWND_UserUnmarshal`, `HWND_UserFree`) and reconstruct `msdbg2.idl`.
- [ ] Document every custom COM vtable layout (method order, parameter types, `HRESULT` return codes, apartment threading model, and marshaling requirements) in the corresponding `src/<module>/interfaces.h`.

**Exit Criteria:** Zero unresolved ordinal imports; 100% of COM CLSIDs/IIDs and RPC proxy/stub tables documented in compilable `.idl` and `.h` headers.

---

## Phase 5: Native x86-64 Decompilation & Formal Specification by Subsystem (28 PE32+ Modules)

**Objective:** Systematically decompile every function across all 28 native x86-64 binaries, recover internal data structures and state machines, and author clean-room specifications for each subsystem.

### Subsystem 5A: Core Browser Host, Integrity Broker, Setup & Compatibility Shims (5 Modules)

- [ ] **5A.1 `bin/iexplore.exe` (810,376 bytes; Entry `0x1400019f0`):**
  - Decompile `wWinMain` / entrypoint `0x1400019f0` and all functions in `.text` (`0x3c70` bytes).
  - Specify command-line parsing (`CommandLineToArgvW`), `SetCurrentProcessExplicitAppUserModelID`, DLL directory hardening (`SetDllDirectoryW`), heap mitigation setup (`HeapSetInformation`), ETW provider registration (`EventRegister`/`EventWrite`), existing window discovery (`FindWindowExW`, `SendMessageTimeoutW`), and dynamic loading of `ieframe.dll` (`IEllMain` / `wWinMain` handoff).
- [ ] **5A.2 `bin/ielowutil.exe` (222,720 bytes; Entry `0x140002940`):**
  - Decompile all functions in `.text` (`0x3600` bytes).
  - Specify the Protected Mode Low-Integrity (MIC) broker lifecycle, command-line switches, COM class registration (`CoRegisterClassObject`, `CoInitializeSecurity`), shared memory / named event IPC (`OpenFileMappingW`, `MapViewOfFile`, `OpenEventW`), and WinInet cookie broker operations (`InternetGetCookieExW`, `InternetSetCookieExW`).
- [ ] **5A.3 `bin/ieinstal.exe` (492,032 bytes; Entry `0x14000fa70`):**
  - Decompile all functions in `.text` (`0xfb00` bytes).
  - Specify the UAC elevation broker for ActiveX control / add-on installation, `AUTHZ.dll` access checks (`AuthzInitializeResourceManager`, `AuthzAccessCheck`), mandatory integrity label verification (`AddMandatoryAce`, `CheckTokenMembership`), WinTrust catalog verification (`CryptCATAdmin*`), `urlmon.dll!Extract` CAB unpacking, and COM impersonation (`CoImpersonateClient`, `CoRevertToSelf`).
- [ ] **5A.4 `bin/IEShims.dll` (386,560 bytes; Entry `0x1800010e0`):**
  - Decompile all 10 exported functions (`AcRedirNotify`, `AcRedirNotifySetEnabled`, `AcRedirSetEnabled`, `IEShims_AdminCheckAndLaunch`, `IEShims_CreateWindowEx`, `IEShims_GetOriginatingThreadId`, `IEShims_InDllMainContext`, `IEShims_Initialize`, `IEShims_SetRedirectRegistryForThread`, `IEShims_Uninitialize`) and internal IAT/API hook engines.
  - Specify how `IEShims.dll` intercepts file system, registry, process creation, and window creation APIs for Protected Mode / AppCompat redirection.
- [ ] **5A.5 `bin/ieproxy.dll` (805,376 bytes; Entry `0x180001ce0`):**
  - Decompile custom `IUnknown` / `IMarshal` user-marshal routines (`NdrGetUserMarshalInfo`), security descriptor validation helpers, URL/path canonicalization helpers, and all MIDL-generated proxy/stub tables.

### Subsystem 5B: Telemetry, SQM & Performance Tracing Infrastructure (3 Modules)

- [ ] **5B.1 `bin/sqmapi.dll` (286,088 bytes; Entry `0x1800014d4`):**
  - Decompile all **63 exported `Sqm*` functions** (`SqmStartSession`, `SqmEndSession`, `SqmEndSessionEx`, `SqmFlushSession`, `SqmSet`, `SqmSetDWord64`, `SqmSetString`, `SqmSetBool`, `SqmSetBits`, `SqmSetIfMax`, `SqmSetIfMin`, `SqmIncrement`, `SqmAddToAverage`, `SqmAddToStream*`, `SqmTimer*`, `SqmStartUpload*`, `SqmLoadEscalationManifest`, `SqmCheckEscalation*`, `SqmReadSharedMachineId`, `SqmWriteSharedMachineId`, `SqmSysprep*`, etc.).
  - Specify the binary `.sqm` session file format (headers, datapoints, stream entries, CRC/crypto hashes via `CryptAcquireContextW`/`CryptGenRandom`), shared machine/user GUID storage in the registry, and background upload state machine.
- [ ] **5B.2 `bin/perfcore.dll` (161,280 bytes; Entry `0x18001a5ac`):**
  - Decompile `DllGetClassObject`, `DllCanUnloadNow`, `DllRegisterServer`, `DllUnregisterServer`, and internal ETW trace processing classes (`OpenTraceW`, `ProcessTrace`, `CloseTrace`, `EventRegister`).
  - Specify the COM interfaces exposed to `perf_nt.dll` and F12 performance tools.
- [ ] **5B.3 `bin/perf_nt.dll` (1,477,120 bytes; Entry `0x180112bd8`):**
  - Decompile COM class factories, ETW session controllers, NT performance counter collectors, XML configuration parsers (`XmlLite!CreateXmlReader`), and symbol/module address resolvers.

### Subsystem 5C: Process Debug Manager (PDM) & Script Debugging Engine (3 Modules)

- [ ] **5C.1 `bin/pdm.dll` (542,272 bytes; Entry `0x180036a54`):**
  - Decompile the Process Debug Manager COM server (`IDebugApplication`, `IDebugManager`, `IMachineDebugManager`, `IDebugDocumentHelper`, `IRemoteDebugApplication`, etc.).
  - Specify thread synchronization, cross-process debug attachment, security descriptor/ACL setup for debug objects, breakpoint dispatch, and JIT debugger launch logic.
- [ ] **5C.2 `bin/pdmproxy100.dll` (105,568 bytes; Entry `0x180001210`):**
  - Finalize 1:1 specification of all marshaled PDM v10.0 interfaces and proxy/stub registration routines.
- [ ] **5C.3 `bin/msdbg2.dll` (400,968 bytes; Entry `0x18000164c`):**
  - Finalize 1:1 specification of all Active Script / Visual Studio debug interfaces (`IDebugProgram2`, `IDebugEngine2`, `IDebugThread2`, `IDebugProperty2`, etc.) and custom `HWND` marshalers.

### Subsystem 5D: Diagnostics Hub & Tap Framework (4 Modules)

- [ ] **5D.1 `bin/DiagnosticsTap.dll` (244,224 bytes; Entry `0x18002b460`):**
  - Decompile `DllGetClassObject`, `DllInstall`, `DllRegisterServer`, `DllUnregisterServer`, and internal DOM/runtime tap classes (`IDiagnosticsTap`, pipe/window IPC channels, DACL/SACL security descriptor builders, `urlmon` URI handlers).
- [ ] **5D.2 `bin/DiagnosticsHub.DataWarehouse.dll` (666,624 bytes; Entry `0x180069330`):**
  - Decompile the DataWarehouse COM server (`DllGetClassObject`), Vista+ Threadpool work/wait/cleanup group managers (`CreateThreadpoolWork`, `SubmitThreadpoolWork`), data partition storage, and query aggregation engines.
- [ ] **5D.3 `bin/DiagnosticsHub.ScriptedSandboxPlugin.dll` (276,480 bytes; Entry `0x180021ce0`):**
  - Decompile the scripted sandbox host plugin (`DllGetClassObject`, `DllCanUnloadNow`), hidden message window loop (`CreateWindowExW`), and sandbox-to-host COM marshaling bridge.
- [ ] **5D.4 `bin/DiagnosticsHub_is.dll` (50,176 bytes; Entry `0x180008eb0`):**
  - Decompile the Trace Data Helper (`tdh.dll!TdhGetProperty`, `TdhGetPropertySize`) event information service and its COM registration surface.

### Subsystem 5E: F12 Developer Tools Shell, Legacy DevTools & Specialized Analyzers (12 Modules)

- [ ] **5E.1 `bin/F12.dll` (1,421,312 bytes; Entry `0x1800ade40`):**
  - Decompile exported entrypoints (`ShowTools`, `ShowChooser`, `DllCanUnloadNow`, `DllRegisterServer`, `DllUnregisterServer`) and internal F12 frame host, docking/undocking window manager, MSAA accessibility (`OLEACC`), WIC image conversion (`WindowsCodecs`), XmlLite settings persistence, and Windows Error Reporting (`wer.dll`) integration.
- [ ] **5E.2 `bin/F12Tools.dll` (372,224 bytes; Entry `0x180043610`):**
  - Decompile COM factories, tool plugin host bridges, named pipe IPC (`CreatePipe`), cross-thread COM stream marshaling (`CoMarshalInterThreadInterfaceInStream`, `CoRegisterMessageFilter`), and DACL security checks.
- [ ] **5E.3 `bin/F12Resources.dll` (10,949,120 bytes; Entry `0x180001130`):**
  - Decompile the minimal `DllMain` entrypoint (`DisableThreadLibraryCalls` and `/GS` cookie initialization) in `.text` (`0x25c` bytes) alongside full `.rsrc` reconstruction from Phase 2.
- [ ] **5E.4 `bin/iedvtool.dll` (950,784 bytes; Entry `0x180099490`):**
  - Decompile the in-process Developer Tools engine (`DllGetClassObject`, `DllCanUnloadNow`, `DllRegisterServer`, `DllUnregisterServer`), including DOM tree walker, CSS style tracer, `IEFRAME.dll` tab association (`IEAssociateThreadWithTab`, `IESaveFile`), `WININET.dll` cache/cookie/privacy managers, and GDI custom controls.
- [ ] **5E.5 `bin/JSProfilerCore.dll` (67,072 bytes; Entry `0x18000b70c`):**
  - Decompile the JavaScript profiler core COM server (`IActiveScriptProfilerCallback` / `IActiveScriptProfilerControl`), high-resolution timer control (`WINMM.dll!timeBeginPeriod`), sample buffer management, and profile data serialization.
- [ ] **5E.6 `bin/jsprofilerui.dll` (628,736 bytes; Entry `0x180027260`):**
  - Decompile `CreateProfileTab` and the GDI/User32 profiler report grid, call-tree view, CSV/export writers, and accessibility objects.
- [ ] **5E.7 `bin/jsdebuggeride.dll` (142,336 bytes; Entry `0x180019d70`):**
  - Decompile `DllGetClassObject`, `DllCanUnloadNow`, debugger session manager, and `WININET` source document fetcher (`RetrieveUrlCacheEntryStreamW`, `InternetOpenUrlW`).
- [ ] **5E.8 `bin/jsdbgui.dll` (565,248 bytes; Entry `0x180052c30`):**
  - Decompile `CreateConsoleTab`, `CreateScriptTab`, `CreateSourceViewer`, syntax-highlighted GDI source viewer, printing support (`StartDocW`, `StartPage`, `EndDoc`), watch/locals/call-stack panes, and interactive console evaluator.
- [ ] **5E.9 `bin/MemoryAnalyzer.dll` (1,862,144 bytes; Entry `0x1801b2700`):**
  - Decompile `DllGetClassObject`, `DllCanUnloadNow`, heap snapshot ingestion, object graph construction, dominator-tree calculation, snapshot diffing algorithms, and multi-threaded worker callbacks (`TrySubmitThreadpoolCallback`).
- [ ] **5E.10 `bin/networkinspection.dll` (1,217,024 bytes; Entry `0x180053280`):**
  - Decompile `CreateNetworkTab`, HTTP/HTTPS request/response interceptor, timing waterfall renderer, `WININET` cache stream inspector, MIME detector (`urlmon!FindMimeFromData`), and XML/HAR capture serializer.
- [ ] **5E.11 `bin/Timeline.dll` (219,136 bytes; Entry `0x1800299e0`):**
  - Decompile `DllGetClassObject`, `DllCanUnloadNow`, UI responsiveness timeline data model, event lane aggregation, and zoom/pan viewport calculations.
- [ ] **5E.12 `bin/Timeline_is.dll` (171,520 bytes; Entry `0x180021450`):**
  - Decompile `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`, `Timeline.cpu.xml` parser (`XmlLite!CreateXmlReader`), and TDH event correlation state machine (`TdhGetProperty`).

### Subsystem 5F: Direct3D HLSL Compiler Service (1 Module)

- [ ] **5F.1 `bin/D3DCompiler_47.dll` (4,158,464 bytes; Entry `0x18038f360`):**
  - Decompile all **29 exported functions** (`D3DAssemble`, `D3DCompile`, `D3DCompile2`, `D3DCompileFromFile`, `D3DCompressShaders`, `D3DCreateBlob`, `D3DCreateFunctionLinkingGraph`, `D3DCreateLinker`, `D3DDecompressShaders`, `D3DDisassemble`, `D3DDisassemble10Effect`, `D3DDisassemble11Trace`, `D3DDisassembleRegion`, `D3DGetBlobPart`, `D3DGetDebugInfo`, `D3DGetInputAndOutputSignatureBlob`, `D3DGetInputSignatureBlob`, `D3DGetOutputSignatureBlob`, `D3DGetTraceInstructionOffsets`, `D3DLoadModule`, `D3DPreprocess`, `D3DReadFileToBlob`, `D3DReflect`, `D3DReflectLibrary`, `D3DReturnFailure1`, `D3DSetBlobPart`, `D3DStripShader`, `D3DWriteBlobToFile`, `DebugSetMute`).
  - Specify the C-preprocessor (`D3DPreprocess`), HLSL lexer/parser, AST-to-IL lowering, optimization passes, DXBC container formatter (`RDEF`, `ISGN`, `OSGN`, `SHDR`/`SHEX`, `STAT`, `SPDB`), Function Linking Graph (`ID3D11Linker`, `ID3D11FunctionLinkingGraph`), shader reflection (`ID3D11ShaderReflection`), and retail DXBC checksum/hash calculation (`CryptAcquireContextW` / MD5 retail shader hash).

**Exit Criteria:** Every native module has a complete function-level specification in `analysis/report/` and complete, verified header declarations in `src/<module>/interfaces.h`.

---

## Phase 6: Clean-Room Source Reconstruction & Reproducible Build System

**Objective:** Implement clean-room source code for all 49 PE targets under `src/` and construct a deterministic build system that produces drop-in replacement binaries.

### 6.1 Source Tree & Interface Header Completion (`src/<module>/`)
- [ ] Populate `src/<module>/interfaces.h` across all 28 native code directories with verified C/C++ types, constants, GUIDs, COM interfaces, and exported function prototypes (`extern "C"` / `__stdcall` / `__fastcall`).
- [ ] Implement clean-room `.cpp` / `.c` translation units per module adhering strictly to the Phase 4–5 specifications.
- [ ] Create exact Module Definition (`.def`) files (`src/<module>/<module>.def`) for every DLL with exports so ordinal numbering, export names, and `PRIVATE` export attributes match `analysis/report/api-map.md` 1:1.
- [ ] Add compiled MIDL targets (`.idl` -> `*_i.c`, `*_p.c`, `dlldata.c`, `.tlb`) for `ieproxy`, `pdmproxy100`, `msdbg2`, and any DLL with embedded `TYPELIB` resources.

### 6.2 Root Build System (`CMakeLists.txt` & Toolchain Presets)
- [ ] Author a root `CMakeLists.txt` and `CMakePresets.json` supporting:
  - **x86-64 (`amd64`) toolchain** for the 28 native PE32+ code modules (`iexplore.exe`, `ieinstal.exe`, `ielowutil.exe`, and 25 native DLLs).
  - **x86 (`i386`) resource-only toolchain** (`/NOENTRY` / `/DLL`) for the 20 `.mui` satellite images.
  - **x86 (`i386`) C# / MSBuild target** for `iediagcmd.exe`.
- [ ] Configure exact PE linker characteristics per module matching `analysis/report/generated/*.objdump.txt`:
  - `ImageBase` (`0x140000000` for x64 EXEs, `0x00400000` for `iediagcmd.exe`, `0x180000000` for x64 DLLs).
  - `Subsystem` (`WINDOWS_GUI` vs. `WINDOWS_CUI`), DLL characteristics (ASLR `/DYNAMICBASE`, DEP `/NXCOMPAT`, High-Entropy VA `/HIGHENTROPYVA`, `/GS` stack cookies).
  - Delay-load linker flags (`/DELAYLOAD:<dll>`) matching `.didat` tables.
  - Custom import libraries (`.lib`) for private/ordinal-only imports from `IEFRAME.dll`, `MSHTML.dll`, `iertutil.dll`, `urlmon.dll`, `SHLWAPI.dll`, and `OLEAUT32.dll`.
- [ ] Add packaging rules to stage non-PE files (`Timeline.cpu.xml`, `ie9props.propdesc`, `SIGNUP/install.ins`, `en-US/eula.rtf`, `pt-BR/eula.rtf`, `images/bing.ico`, `LICENSE`, `README.md`) alongside built binaries in an output distribution directory (`dist/`).

**Exit Criteria:** A single reproducible build command compiles all 28 native PE32+ images, 1 managed PE32 executable, and 20 `.mui` satellites with zero warnings or unresolved symbols, and stages all 57 corpus deliverables.

---

## Phase 7: Dynamic Tracing, Behavioral Parity & 1:1 Verification Harness

**Objective:** Prove that every reconstructed binary is a faithful 1:1 drop-in replacement for its original counterpart through automated static, ABI, and dynamic behavioral verification.

### 7.1 Isolated Windows 7 SP1 x64 Verification Environment
- [ ] Provision an air-gapped, snapshot-controlled Windows 7 SP1 x64 VM matching IE 11 (`11.0.9600.19597`) system dependencies (`ieframe.dll`, `mshtml.dll`, `jscript9.dll`, `iertutil.dll`, `urlmon.dll`, `wininet.dll`).
- [ ] Configure automated trace collection using WinDbg/CDB scripting, Event Tracing for Windows (ETW), Process Monitor (ProcMon), and API Monitor to record baseline traces from the unmodified `bin/` corpus.

### 7.2 Multi-Tier Verification Suite (`analysis/tools/verify_parity.py`)
- [ ] **Tier 1 — Structural & ABI Parity Verification (Linux & Windows CI):**
  - Verify PE format (`pei-x86-64` vs. `pei-i386`), subsystem, section presence, and resource tree IDs against `analysis/report/generated/inventory.json`.
  - Verify 100% Export Address Table (EAT) parity (exact symbol names, ordinals, and forwarding) across all 49 PE images.
  - Verify COM `sizeof()` class layouts, vtable offsets, and `IID`/`CLSID` constants via static assertions (`static_assert`).
- [ ] **Tier 2 — Component & Subsystem Behavioral Tests (Windows VM):**
  - **Host & Brokers (`iexplore.exe`, `ielowutil.exe`, `ieinstal.exe`, `IEShims.dll`, `ieproxy.dll`):** Verify browser launch, tab process spawning, Protected Mode low-integrity cookie brokering, ActiveX installation elevation prompt, and shim redirection hooks.
  - **Telemetry & Performance (`sqmapi.dll`, `perfcore.dll`, `perf_nt.dll`):** Run API test vectors across all 63 `Sqm*` exports and verify `.sqm` output stream byte parity and ETW trace consumption.
  - **PDM & Script Debugging (`pdm.dll`, `pdmproxy100.dll`, `msdbg2.dll`):** Verify script debugger attachment, breakpoint hit, call-stack enumeration, and cross-process COM marshaling.
  - **Diagnostics Hub & F12 DevTools (`F12*.dll`, `Diagnostics*.dll`, `iedvtool.dll`, `js*.dll`, `MemoryAnalyzer.dll`, `networkinspection.dll`, `Timeline*.dll`):** Launch F12 Developer Tools (`ShowTools`), verify DOM Explorer, Console, Debugger, Network capture, UI Responsiveness timeline (`Timeline.cpu.xml`), Profiler, and Memory heap snapshot capture in both `en-US` and `pt-BR` locales.
  - **Managed CLI (`iediagcmd.exe`):** Compare diagnostic report archives and console outputs between original and reconstructed executables.
  - **HLSL Compiler (`D3DCompiler_47.dll`):** Compile, preprocess, reflect, strip, and disassemble a corpus of Vertex, Pixel, Geometry, Hull, Domain, and Compute shaders (SM 2.0–5.0) and verify byte-for-byte DXBC output parity.
- [ ] **Tier 3 — Binary & CFG Equivalence Auditing:**
  - Run automated function-by-function control-flow graph (CFG) and basic-block comparison (via BinDiff / Diaphora / REA disassembly diffing) between reconstructed modules and `bin/` originals, documenting any compiler codegen divergences in `analysis/report/validation.md`.

**Exit Criteria:** All 49 reconstructed PE modules pass Tier 1 (ABI/structural), Tier 2 (dynamic drop-in replacement), and Tier 3 (CFG/algorithmic parity) checks, with full audit trails recorded in `analysis/report/validation.md`.
