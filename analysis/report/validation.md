# Validation

## Performed

- Re-ran `analysis/tools/inventory.py`: all 57 inputs hashed and all 49 PE images parsed without modifying `bin/`.
- Re-ran `analysis/tools/test_pe.py`: locked facts hold for `iexplore.exe` (PE32+, entry `0x19f0`, `.didat` delay-load of `IEFRAME.dll`, PDB `iexplore.pdb`), `iediagcmd.exe` (PE32 i386, CLR `0x2008/0x48`, `mscoree.dll!_CorExeMain`), resource-only `en-US/iexplore.exe.mui`, `IEShims.dll` (10 named exports), and `sqmapi.dll` (63 `Sqm*` exports).
- Re-ran `analysis/tools/verify_phase0.py`: 57/57 files, 49/49 PE images, 30,617,822 bytes, SHA-256 lock matches live `bin/`, 49 module ledgers present.
- Cross-checked `iexplore.exe` using direct GNU objdump, `pe.py`, and REA's GNU objdump adapter. All three report PE32+ / `i386:x86-64` and entry `0x1400019f0`; REA reports unchanged pre/post SHA-256 `cff801d6dc847bb832d0077ce38ddb66ef5b4637ff947bbdbc228eef10494f97`.
- Re-executed `npx -y rea-agents@6.5.0 --version` (prints `6.5.0`) and `inspect-with-objdump ... file_headers`; stdout matched the retained `iexplore-file-headers.json` artifact.
- Confirmed the previous objdump-regex section parser was wrong (IAT descriptor rows such as `00007510` were emitted as sections). The stdlib parser now matches the `Sections:` table in raw objdump.
- Confirmed ordinal-only IAT entries now carry concrete ordinals (`OLEAUT32.dll` 217 thunks, `iertutil.dll` 73, `SHLWAPI.dll` 14, plus `urlmon`, `IEFRAME`, `COMCTL32`, `SHELL32`, `MSHTML`).
- Confirmed delay-load descriptors on `iexplore.exe`, `IEShims.dll`, `ieproxy.dll`, `pdm.dll`, `perf_nt.dll`, and `sqmapi.dll`.
- Confirmed `IMAGE_DIRECTORY_ENTRY_SECURITY` is stored as a file offset (`iexplore.exe` `0xc3c00`; `iediagcmd.exe` `0x54000`, numerically equal to its BaseReloc RVA).
- Confirmed PE32+ named-import thunks keep bit 31 (`import_name_rva(0x80000010, pe32plus=True) == 0x80000010`).
- CodeView `RSDS` records recovered for all 29 code images; 20 `.mui` satellites have no debug directory.

## Not performed

No reconstructed module was compiled because no evidence-supported compatibility implementation exists. No original executable was launched, and no behavioral equivalence, edge-case handling, or runtime success is claimed. No signing validation or Microsoft symbol-server retrieval was performed (PDB *identity* is recorded; PDB *files* are a Phase 1 task).

## Known discrepancies and risks

GNU objdump textual parsing is version-sensitive; retained raw output is authoritative for GNU's view. Import names do not establish prototypes. PE timestamp values are not trusted. Resource-only classification is based on zero entrypoint, `.rsrc`-only sections, and empty IAT/EAT, and is therefore strongly supported but remains a structural characterization, not proof of every loader behavior.
