# pdmproxy100.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `a3e0fd851f31be04f0bf268038501f26c5a552311967e42fc4ec7f8a4761fe3e` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/pdmproxy100.dll`
- Bytes: 105,568
- SHA-256: `a3e0fd851f31be04f0bf268038501f26c5a552311967e42fc4ec7f8a4761fe3e`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x180001210` (RVA `0x1210`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `12.0`; OS version: `6.0`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2013-07-12T02:40:34Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `pdmproxy100.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0xaca4 | 0xae00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.orpc` | 0x105 | 0x200 | `0x18000c000` | 0xb200 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.rdata` | 0x7772 | 0x7800 | `0x18000d000` | 0xb400 | CNT_INITIALIZED_DATA, MEM_READ |
| `.data` | 0x3c98 | 0x1a00 | `0x180015000` | 0x12c00 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x8d0 | 0xa00 | `0x180019000` | 0x14600 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x428 | 0x600 | `0x18001a000` | 0x15000 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x6bc | 0x800 | `0x18001b000` | 0x15600 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x13c70` | 0xa8 |
| `Import` | `0x13d18` | 0x50 |
| `Resource` | `0x1a000` | 0x428 |
| `Exception` | `0x19000` | 0x8d0 |
| `Security` | `0x15e00` | 0x3e60 |
| `BaseReloc` | `0x1b000` | 0x6bc |
| `Debug` | `0xd360` | 0x38 |
| `LoadConfig` | `0x13380` | 0x70 |
| `IAT` | `0xd000` | 0x2e8 |

## Static imports

- `KERNEL32.dll`: 64 imports
- `OLEAUT32.dll`: 4 imports
- `RPCRT4.dll`: 22 imports

## Delay-load imports

- None recovered.

## Exports

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/pdmproxy100.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
