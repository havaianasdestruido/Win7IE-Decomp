# Win7IE-Decomp

Evidence-backed static analysis, reverse-engineering baseline, and clean-room 1:1 reconstruction workspace for the **Windows 7 Internet Explorer 11 (`11.00.9600.19597`)** application host, F12 Developer Tools suite, Diagnostics Hub, Process Debug Manager (PDM), Direct3D HLSL Compiler (`D3DCompiler_47.dll`), and SQM/ETW telemetry components.

---

## Clean-Room 1:1 Decompilation & Reconstruction Roadmap (`TODO.md`)

The complete, phase-divided engineering checklist required to achieve a faithful 1:1 decompilation and clean-room reconstruction of the original application and services is maintained in **[`TODO.md`](./TODO.md)** at the project root:

- **[Phase 0 — Corpus Inventory, Cryptographic Locking & Structural Baseline](./TODO.md#phase-0-corpus-inventory-cryptographic-locking--structural-baseline-completed)** *(Completed)*
- **[Phase 1 — Deep Decompilation Toolchain, Symbol/PDB Recovery & Unwind/RTTI Mapping](./TODO.md#phase-1-deep-decompilation-toolchain-symbolpdb-recovery--unwindrtti-mapping)**
- **[Phase 2 — Non-PE Schemas, Configurations & PE Resource (`.rsrc` / `.mui`) Extraction](./TODO.md#phase-2-non-pe-schemas-configurations--pe-resource-rsrc--mui-extraction)**
- **[Phase 3 — Managed (.NET / CLR) Decompilation & Clean-Room Reconstruction (`iediagcmd.exe`)](./TODO.md#phase-3-managed-net--clr-decompilation--clean-room-reconstruction-iediagcmdexe)**
- **[Phase 4 — COM, RPC/NDR Proxy-Stub, Delay-Load & Ordinal Interface Recovery](./TODO.md#phase-4-com-rpcndr-proxy-stub-delay-load--ordinal-interface-recovery)**
- **[Phase 5 — Native x86-64 Decompilation & Formal Specification by Subsystem (28 PE32+ Modules)](./TODO.md#phase-5-native-x86-64-decompilation--formal-specification-by-subsystem-28-pe32-modules)**
- **[Phase 6 — Clean-Room Source Reconstruction & Reproducible Build System](./TODO.md#phase-6-clean-room-source-reconstruction--reproducible-build-system)**
- **[Phase 7 — Dynamic Tracing, Behavioral Parity & 1:1 Verification Harness](./TODO.md#phase-7-dynamic-tracing-behavioral-parity--11-verification-harness)**

See **[`TODO.md`](./TODO.md)** for per-phase entry/exit criteria, clean-room governance rules (Dirty-Room specification vs. Clean-Room implementation), and per-module tasks across all 57 corpus files.

---

## Corpus Summary

The reference corpus in `bin/` is **strictly read-only** and comprises **57 files (30,617,822 bytes)** verified by SHA-256:

| Category | Count | Architecture / Format | Examples |
|---|---:|---|---|
| **Native Code Executables (`.exe`)** | 3 | PE32+ `x86-64` (`pei-x86-64`) | `iexplore.exe`, `ieinstal.exe`, `ielowutil.exe` |
| **Native Code Libraries (`.dll`)** | 25 | PE32+ `x86-64` (`pei-x86-64`) | `F12.dll`, `iedvtool.dll`, `IEShims.dll`, `ieproxy.dll`, `pdm.dll`, `msdbg2.dll`, `sqmapi.dll`, `D3DCompiler_47.dll`, etc. |
| **Managed CLI Executable (`.exe`)** | 1 | PE32 `i386` CLR (`pei-i386`) | `iediagcmd.exe` (`mscoree.dll!_CorExeMain`) |
| **Locale Resource Satellites (`.mui`)** | 20 | PE32 `i386` resource-only (`pei-i386`) | 10 `en-US/*.mui` + 10 `pt-BR/*.mui` |
| **Schemas, Configs & Static Assets** | 8 | XML, PropDesc, UTF-16LE INS, RTF, ICO, Text | `Timeline.cpu.xml`, `ie9props.propdesc`, `SIGNUP/install.ins`, `en-US/eula.rtf`, `pt-BR/eula.rtf`, `images/bing.ico`, `LICENSE`, `README.md` |

---

## Repository Structure

```text
.
├── README.md                          # Project overview and index (this file)
├── TODO.md                            # Phased 1:1 decompilation & clean-room reconstruction roadmap
├── bin/                               # Read-only reference corpus (57 files, SHA-256 locked)
├── analysis/
│   ├── report/
│   │   ├── final-report.md            # Executive baseline summary and deliverable map
│   │   ├── inventory.md               # Complete file inventory with byte sizes and SHA-256 hashes
│   │   ├── methodology.md             # Tooling, REA 6.5.0 workflows, and evidence policy
│   │   ├── module-analysis.md         # Subsystem classification and structural findings
│   │   ├── api-map.md                 # Consolidated PE import/export tables across all 49 PE images
│   │   ├── dependencies.md            # Static dependency patterns and dynamic-loading caveats
│   │   ├── data-formats.md            # Container formats, CLR headers, and XML/property schemas
│   │   ├── progress.md                # Coverage metrics and remaining work items
│   │   ├── validation.md              # Verification checks performed and explicit non-claims
│   │   ├── generated/                 # Authoritative raw `objdump -x` outputs, inventory.json, dependencies.json
│   │   └── rea/                       # Captured `rea-agents@6.5.0` header and disassembly artifacts
│   └── tools/
│       ├── README.md                  # Tooling documentation
│       ├── pe.py                      # Stdlib PE32/PE32+ structural parser
│       ├── inventory.py               # Corpus hasher, objdump retainer, and ledger generator
│       ├── test_pe.py                 # Locked PE structural facts
│       ├── verify_phase0.py           # 57/49 coverage and hash-lock verifier
│       └── rea_baseline.py            # REA 6.5.0 objdump-adapter reproduction
└── src/
    └── <module>/                      # 49 per-image clean-room evidence ledgers (`README.md` + `interfaces.h`)
```

---

## Reproducing the Structural Baseline

To regenerate the cryptographic inventory, PE structural tables (`analysis/report/generated/`), and per-module evidence skeletons (`src/<module>/`) without modifying `bin/`:

```sh
python3 analysis/tools/test_pe.py
python3 analysis/tools/inventory.py
python3 analysis/tools/verify_phase0.py
```

For the full multi-phase plan from structural baseline to complete 1:1 clean-room source reconstruction and dynamic verification, consult **[`TODO.md`](./TODO.md)**.
