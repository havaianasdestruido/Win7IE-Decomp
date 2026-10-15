# Consolidated API map

Evidence: `analysis/report/generated/*.objdump.txt` plus the stdlib PE parser in `analysis/tools/pe.py`.
Names and ordinals are Import/Export Address Table observations, not inferred prototypes.

## `bin/D3DCompiler_47.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x18038f360` (RVA `0x38f360`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **False**.
- PDB: `D3DCompiler_47.pdb`.

### Static imports

- `ADVAPI32.dll` (12): `CryptAcquireContextW`, `CryptCreateHash`, `CryptDestroyHash`, `CryptGetHashParam`, `CryptHashData`, `CryptReleaseContext`, `RegCloseKey`, `RegEnumKeyExA`, `RegOpenKeyExA`, `RegOpenKeyExW`, `RegQueryValueExA`, `RegQueryValueExW`
- `KERNEL32.dll` (68): `CloseHandle`, `CopyFileExW`, `CreateFileA`, `CreateFileMappingW`, `CreateFileW`, `DeleteCriticalSection`, `DeleteFileW`, `DeviceIoControl`, `DisableThreadLibraryCalls`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FlushViewOfFile`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableA`, `GetFileAttributesW`, `GetFileSize`, `GetFileSizeEx`, `GetFileType`, `GetFullPathNameA`, `GetFullPathNameW`, `GetLastError`, `GetModuleFileNameA`, `GetProcAddress`, `GetProcessHeap`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVersion`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExW`, `LocalAlloc`, `LocalFree`, `lstrcmpiA`, `MapViewOfFile`, `MapViewOfFileEx`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `ReadFile`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetFileAttributesW`, `SetFilePointer`, `SetLastError`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `UnmapViewOfFile`, `VirtualAlloc`, `VirtualFree`, `WideCharToMultiByte`, `WriteFile`
- `msvcrt.dll` (117): `??1type_info@@UEAA@XZ`, `??2@YAPEAX_K@Z`, `??3@YAXPEAX@Z`, `??_U@YAPEAX_K@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `__unDName`, `_amsg_exit`, `_chsize`, `_clearfp`, `_close`, `_controlfp`, `_CxxThrowException`, `_finite`, `_fpclass`, `_get_osfhandle`, `_initterm`, `_isnan`, `_lock`, `_lseeki64`, `_mbscmp`, `_mbstrlen`, `_memicmp`, `_onexit`, `_open_osfhandle`, `_purecall`, `_read`, `_snwprintf_s`, `_strdup`, `_stricmp`, `_strnicmp`, `_strtoui64`, `_time64`, `_unlock`, `_vsnprintf`, `_vsnwprintf`, `_wcsdup`, `_wcsicmp`, `_wcsnicmp`, `_wfsopen`, `_wfullpath`, `_wgetenv`, `_wmakepath_s`, `_write`, `_wsopen`, `_wsplitpath_s`, `_XcptFilter`, `acos`, `asin`, `atan`, `atan2`, `atof`, `atoi`, `bsearch`, `ceil`, `cos`, `cosh`, `exp`, `fclose`, `floor`, `floorf`, `fmod`, `fread`, `free`, `fseek`, `ftell`, `getenv`, `isalnum`, `isalpha`, `isdigit`, `isspace`, `iswdigit`, `isxdigit`, `log`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memset`, `modf`, `pow`, `qsort`, `setlocale`, `sin`, `sinh`, `sprintf_s`, `sqrt`, `sscanf`, `strcat_s`, `strchr`, `strcmp`, `strcpy_s`, `strncmp`, `strncpy_s`, `strnlen`, `strrchr`, `strstr`, `strtoul`, `swprintf_s`, `tan`, `tanh`, `tolower`, `toupper`, `towlower`, `vsprintf_s`, `wcscat_s`, `wcschr`, `wcscpy_s`, `wcsncat_s`, `wcsncmp`, `wcsncpy_s`, `wcsrchr`, `wcstol`
- `RPCRT4.dll` (1): `UuidCreate`

### Exports (29)

`D3DAssemble`, `D3DCompile`, `D3DCompile2`, `D3DCompileFromFile`, `D3DCompressShaders`, `D3DCreateBlob`, `D3DCreateFunctionLinkingGraph`, `D3DCreateLinker`, `D3DDecompressShaders`, `D3DDisassemble`, `D3DDisassemble10Effect`, `D3DDisassemble11Trace`, `D3DDisassembleRegion`, `D3DGetBlobPart`, `D3DGetDebugInfo`, `D3DGetInputAndOutputSignatureBlob`, `D3DGetInputSignatureBlob`, `D3DGetOutputSignatureBlob`, `D3DGetTraceInstructionOffsets`, `D3DLoadModule`, `D3DPreprocess`, `D3DReadFileToBlob`, `D3DReflect`, `D3DReflectLibrary`, `D3DReturnFailure1`, `D3DSetBlobPart`, `D3DStripShader`, `D3DWriteBlobToFile`, `DebugSetMute`

## `bin/DiagnosticsHub.DataWarehouse.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180069330` (RVA `0x69330`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `DiagnosticsHub.DataWarehouse.pdb`.

### Static imports

- `KERNEL32.dll` (115): `CloseHandle`, `CloseThreadpool`, `CloseThreadpoolCleanupGroup`, `CloseThreadpoolCleanupGroupMembers`, `CloseThreadpoolWork`, `CompareStringOrdinal`, `CompareStringW`, `CreateEventW`, `CreateFileW`, `CreateThreadpool`, `CreateThreadpoolCleanupGroup`, `CreateThreadpoolWait`, `CreateThreadpoolWork`, `DecodePointer`, `DeleteCriticalSection`, `EncodePointer`, `EnterCriticalSection`, `EnumSystemLocalesA`, `ExitProcess`, `FindResourceExW`, `FindStringOrdinal`, `FlsAlloc`, `FlsFree`, `FlsGetValue`, `FlsSetValue`, `FlushFileBuffers`, `FormatMessageW`, `FreeEnvironmentStringsW`, `FreeLibrary`, `GetACP`, `GetCommandLineA`, `GetConsoleCP`, `GetConsoleMode`, `GetCPInfo`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileAttributesW`, `GetFileType`, `GetFullPathNameW`, `GetLastError`, `GetLocaleInfoA`, `GetLocaleInfoW`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleA`, `GetModuleHandleExW`, `GetNativeSystemInfo`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetUserDefaultLCID`, `GetVersionExW`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSetInformation`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `IsValidCodePage`, `IsValidLocale`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadResource`, `LockResource`, `MultiByteToWideChar`, `OutputDebugStringA`, `OutputDebugStringW`, `QueryPerformanceCounter`, `QueryPerformanceFrequency`, `RaiseException`, `ReadConsoleW`, `ReadFile`, `ResetEvent`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlPcToFileHeader`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetEndOfFile`, `SetEvent`, `SetEventWhenCallbackReturns`, `SetFilePointer`, `SetHandleCount`, `SetLastError`, `SetStdHandle`, `SetThreadpoolThreadMaximum`, `SetThreadpoolThreadMinimum`, `SetThreadpoolWait`, `SetThreadStackGuarantee`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `SubmitThreadpoolWork`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualProtect`, `VirtualQuery`, `WaitForSingleObject`, `WaitForThreadpoolWaitCallbacks`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`
- `ole32.dll` (2): `CLSIDFromString`, `CoCreateGuid`
- `OLEAUT32.dll` (6): `ordinal:149`, `ordinal:150`, `ordinal:2`, `ordinal:4`, `ordinal:6`, `ordinal:7`
- `USER32.dll` (1): `UnregisterClassA`

### Exports (1)

`DllGetClassObject`

## `bin/DiagnosticsHub.ScriptedSandboxPlugin.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180021ce0` (RVA `0x21ce0`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `DiagnosticsHub.ScriptedSandboxPlugin.pdb`.

### Static imports

- `ADVAPI32.dll` (3): `RegCloseKey`, `RegOpenKeyExW`, `RegQueryValueExW`
- `KERNEL32.dll` (88): `CloseHandle`, `CompareStringOrdinal`, `CreateFileW`, `DecodePointer`, `DeleteCriticalSection`, `EncodePointer`, `EnterCriticalSection`, `EnumSystemLocalesA`, `ExitProcess`, `FlsAlloc`, `FlsFree`, `FlsGetValue`, `FlsSetValue`, `FlushFileBuffers`, `FlushInstructionCache`, `FreeEnvironmentStringsW`, `FreeLibrary`, `GetACP`, `GetCommandLineA`, `GetConsoleCP`, `GetConsoleMode`, `GetCPInfo`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileType`, `GetLastError`, `GetLocaleInfoA`, `GetLocaleInfoW`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetUserDefaultLCID`, `GetVersionExW`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSetInformation`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsValidCodePage`, `IsValidLocale`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlPcToFileHeader`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetEnvironmentVariableW`, `SetFilePointer`, `SetHandleCount`, `SetLastError`, `SetStdHandle`, `SetThreadStackGuarantee`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `VirtualProtect`, `VirtualQuery`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`
- `ole32.dll` (4): `CLSIDFromString`, `CoCreateGuid`, `CoCreateInstance`, `StringFromGUID2`
- `OLEAUT32.dll` (8): `ordinal:149`, `ordinal:150`, `ordinal:2`, `ordinal:313`, `ordinal:4`, `ordinal:6`, `ordinal:7`, `ordinal:9`
- `USER32.dll` (11): `CallWindowProcW`, `CreateWindowExW`, `DefWindowProcW`, `DestroyWindow`, `GetClassInfoExW`, `GetWindowLongPtrW`, `LoadCursorW`, `PostMessageW`, `RegisterClassExW`, `SetWindowLongPtrW`, `UnregisterClassA`

### Exports (2)

`DllCanUnloadNow`, `DllGetClassObject`

## `bin/DiagnosticsHub_is.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180008eb0` (RVA `0x8eb0`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `DiagnosticsHub_is.pdb`.

### Static imports

- `KERNEL32.dll` (18): `DeleteCriticalSection`, `EnterCriticalSection`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `GetTickCount`, `InitializeCriticalSection`, `LeaveCriticalSection`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `msvcrt.dll` (25): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_XcptFilter`, `free`, `malloc`, `memcpy`, `memcpy_s`, `memmove`, `memset`
- `ole32.dll` (1): `CoCreateInstance`
- `OLEAUT32.dll` (4): `ordinal:2`, `ordinal:4`, `ordinal:6`, `ordinal:7`
- `tdh.dll` (2): `TdhGetProperty`, `TdhGetPropertySize`

### Exports (4)

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/DiagnosticsTap.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x18002b460` (RVA `0x2b460`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `DiagnosticsTap.pdb`.

### Static imports

- `ADVAPI32.dll` (28): `AddAce`, `CopySid`, `GetAclInformation`, `GetLengthSid`, `GetSecurityDescriptorControl`, `GetSecurityDescriptorDacl`, `GetSecurityDescriptorGroup`, `GetSecurityDescriptorLength`, `GetSecurityDescriptorOwner`, `GetSecurityDescriptorSacl`, `GetSidLengthRequired`, `GetSidSubAuthority`, `GetTokenInformation`, `InitializeAcl`, `InitializeSecurityDescriptor`, `InitializeSid`, `IsValidSid`, `MakeAbsoluteSD`, `MakeSelfRelativeSD`, `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`, `SetSecurityDescriptorDacl`
- `KERNEL32.dll` (68): `CloseHandle`, `CompareStringOrdinal`, `CreateEventW`, `CreatePipe`, `CreateThread`, `DecodePointer`, `DeleteCriticalSection`, `DuplicateHandle`, `EncodePointer`, `EnterCriticalSection`, `FindClose`, `FindFirstFileW`, `FindResourceExW`, `FindResourceW`, `FlushInstructionCache`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableW`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetThreadLocale`, `GetTickCount`, `GetUserDefaultLCID`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LocalAlloc`, `LocalFree`, `LockResource`, `lstrcmpiW`, `MultiByteToWideChar`, `OpenProcess`, `OutputDebugStringA`, `OutputDebugStringW`, `QueryPerformanceCounter`, `RaiseException`, `ReadFile`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetThreadLocale`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WaitForSingleObject`, `WriteFile`
- `msvcrt.dll` (46): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??8type_info@@QEBAHAEBV0@@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wfopen_s`, `_XcptFilter`, `calloc`, `fclose`, `fgetws`, `free`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `vswprintf_s`, `wcscat_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcsncpy_s`
- `ole32.dll` (5): `CoCreateInstance`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `StringFromGUID2`
- `OLEAUT32.dll` (14): `ordinal:10`, `ordinal:149`, `ordinal:150`, `ordinal:161`, `ordinal:162`, `ordinal:163`, `ordinal:186`, `ordinal:2`, `ordinal:277`, `ordinal:4`, `ordinal:6`, `ordinal:7`, `ordinal:8`, `ordinal:9`
- `SHLWAPI.dll` (2): `PathGetCharTypeW`, `PathRemoveFileSpecW`
- `urlmon.dll` (2): `CoInternetCombineUrlEx`, `CreateUri`
- `USER32.dll` (20): `CallWindowProcW`, `CharNextW`, `CreateWindowExW`, `DefWindowProcW`, `DispatchMessageW`, `GetClassInfoExW`, `GetMessageW`, `GetWindowLongPtrW`, `IsWindow`, `LoadCursorW`, `PeekMessageW`, `PostMessageW`, `PostQuitMessage`, `PostThreadMessageW`, `RegisterClassExW`, `RegisterWindowMessageW`, `SendMessageW`, `SetWindowLongPtrW`, `TranslateMessage`, `UnregisterClassA`

### Exports (5)

`DllCanUnloadNow`, `DllGetClassObject`, `DllInstall`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/F12.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x1800ade40` (RVA `0xade40`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `F12.pdb`.

### Static imports

- `ADVAPI32.dll` (18): `CopySid`, `EventRegister`, `EventUnregister`, `EventWrite`, `GetLengthSid`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`, `GetTokenInformation`, `IsValidSid`, `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`
- `GDI32.dll` (24): `BitBlt`, `CombineRgn`, `CreateBitmap`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateDIBSection`, `CreateFontIndirectW`, `CreatePatternBrush`, `CreateRectRgn`, `CreateRectRgnIndirect`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `EqualRgn`, `GetDeviceCaps`, `GetObjectW`, `GetPixel`, `GetStockObject`, `GetTextExtentPoint32W`, `PatBlt`, `SelectObject`, `SetBkColor`, `SetLayout`, `SetTextColor`
- `iertutil.dll` (10): `CreateUri`, `ordinal:325`, `ordinal:463`, `ordinal:518`, `ordinal:519`, `ordinal:526`, `ordinal:527`, `ordinal:528`, `ordinal:58`, `ordinal:791`
- `KERNEL32.dll` (101): `ActivateActCtx`, `CloseHandle`, `CompareStringOrdinal`, `CopyFileW`, `CreateActCtxW`, `CreateDirectoryW`, `CreateEventW`, `CreateFileW`, `CreateThread`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `DeleteFileW`, `DuplicateHandle`, `EncodePointer`, `EnterCriticalSection`, `ExitProcess`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileW`, `FindNextFileW`, `FindResourceExW`, `FindResourceW`, `FlushInstructionCache`, `FormatMessageW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableW`, `GetFileAttributesW`, `GetFullPathNameW`, `GetLastError`, `GetLocaleInfoEx`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetProcessIdOfThread`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTempPathW`, `GetTickCount`, `GetUserDefaultUILanguage`, `GetVersionExW`, `GlobalAlloc`, `GlobalFree`, `GlobalHandle`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionEx`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsWow64Process`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LocalFree`, `LockResource`, `lstrcmpiW`, `lstrcmpW`, `lstrlenW`, `MoveFileW`, `MulDiv`, `MultiByteToWideChar`, `OpenProcess`, `OpenThread`, `OutputDebugStringA`, `QueryFullProcessImageNameW`, `QueryPerformanceCounter`, `QueryPerformanceFrequency`, `RaiseException`, `ReadProcessMemory`, `ReleaseActCtx`, `RemoveDirectoryW`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TlsGetValue`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WaitForMultipleObjects`, `WaitForSingleObject`, `WideCharToMultiByte`, `WriteFile`
- `MSIMG32.dll` (1): `AlphaBlend`
- `msvcrt.dll` (63): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??8type_info@@QEBAHAEBV0@@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `__RTDynamicCast`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_errno`, `_get_doserrno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcstoui64`, `_wfopen_s`, `_wtmpnam_s`, `_wtol`, `_XcptFilter`, `calloc`, `difftime`, `fclose`, `feof`, `fflush`, `fputws`, `fread`, `free`, `fseek`, `ftell`, `fwrite`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `strncpy_s`, `swprintf_s`, `time`, `vswprintf_s`, `wcscat_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcsncpy_s`, `wcsstr`
- `ole32.dll` (18): `CLSIDFromProgID`, `CLSIDFromString`, `CoCreateGuid`, `CoCreateInstance`, `CoGetClassObject`, `CoInitializeEx`, `CoSetProxyBlanket`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`, `CreateStreamOnHGlobal`, `IIDFromString`, `OleInitialize`, `OleLockRunning`, `OleUninitialize`, `StringFromCLSID`, `StringFromGUID2`
- `OLEACC.dll` (3): `CreateStdAccessibleObject`, `LresultFromObject`, `ObjectFromLresult`
- `OLEAUT32.dll` (31): `ordinal:10`, `ordinal:12`, `ordinal:146`, `ordinal:149`, `ordinal:15`, `ordinal:150`, `ordinal:16`, `ordinal:161`, `ordinal:162`, `ordinal:163`, `ordinal:186`, `ordinal:19`, `ordinal:2`, `ordinal:20`, `ordinal:21`, `ordinal:22`, `ordinal:27`, `ordinal:277`, `ordinal:313`, `ordinal:314`, `ordinal:37`, `ordinal:38`, `ordinal:4`, `ordinal:40`, `ordinal:41`, `ordinal:420`, `ordinal:6`, `ordinal:7`, `ordinal:77`, `ordinal:8`, `ordinal:9`
- `SHELL32.dll` (3): `SHCreateDirectoryExW`, `SHGetKnownFolderPath`, `SHGetSpecialFolderPathW`
- `SHLWAPI.dll` (8): `PathFileExistsW`, `PathFindFileNameW`, `PathGetCharTypeW`, `PathIsDirectoryW`, `PathIsRelativeW`, `StrStrIW`, `ordinal:176`, `ordinal:219`
- `urlmon.dll` (2): `ordinal:111`, `ordinal:458`
- `USER32.dll` (131): `AdjustWindowRectEx`, `AllowSetForegroundWindow`, `AppendMenuW`, `AttachThreadInput`, `BeginPaint`, `CallNextHookEx`, `CallWindowProcW`, `ChangeWindowMessageFilterEx`, `CharNextW`, `ClientToScreen`, `CopyRect`, `CreateAcceleratorTableW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DestroyAcceleratorTable`, `DestroyMenu`, `DestroyWindow`, `DialogBoxIndirectParamW`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawTextW`, `EnableWindow`, `EndDialog`, `EndPaint`, `EnumChildWindows`, `EnumDisplayMonitors`, `EnumWindows`, `EqualRect`, `FillRect`, `GetAncestor`, `GetAsyncKeyState`, `GetCapture`, `GetClassInfoExW`, `GetClassNameW`, `GetClientRect`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetDlgCtrlID`, `GetDlgItem`, `GetDoubleClickTime`, `GetFocus`, `GetForegroundWindow`, `GetKeyState`, `GetMenu`, `GetMenuItemCount`, `GetMenuItemInfoW`, `GetMessagePos`, `GetMessageW`, `GetMonitorInfoW`, `GetParent`, `GetSysColor`, `GetSystemMetrics`, `GetWindow`, `GetWindowDC`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowPlacement`, `GetWindowRect`, `GetWindowTextLengthW`, `GetWindowTextW`, `GetWindowThreadProcessId`, `InflateRect`, `InvalidateRect`, `InvalidateRgn`, `IsChild`, `IsIconic`, `IsWindow`, `IsWindowEnabled`, `IsWindowVisible`, `IsZoomed`, `KillTimer`, `LoadAcceleratorsW`, `LoadCursorW`, `LoadImageW`, `LoadMenuW`, `LoadStringA`, `LoadStringW`, `MapDialogRect`, `MapWindowPoints`, `MessageBeep`, `MessageBoxW`, `MonitorFromPoint`, `MonitorFromWindow`, `MoveWindow`, `PeekMessageW`, `PostMessageW`, `PostQuitMessage`, `PostThreadMessageW`, `PtInRect`, `RedrawWindow`, `RegisterClassExW`, `RegisterClassW`, `RegisterWindowMessageW`, `ReleaseCapture`, `ReleaseDC`, `RemoveMenu`, `ScreenToClient`, `SendDlgItemMessageW`, `SendInput`, `SendMessageTimeoutW`, `SendMessageW`, `SetActiveWindow`, `SetCapture`, `SetCursor`, `SetFocus`, `SetForegroundWindow`, `SetLayeredWindowAttributes`, `SetParent`, `SetRect`, `SetRectEmpty`, `SetTimer`, `SetWindowContextHelpId`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPlacement`, `SetWindowPos`, `SetWindowsHookExW`, `SetWindowTextW`, `ShowWindow`, `SystemParametersInfoW`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnhookWindowsHookEx`, `UnregisterClassA`, `UpdateLayeredWindow`, `UpdateWindow`, `WindowFromPoint`
- `UxTheme.dll` (1): `IsCompositionActive`
- `VERSION.dll` (3): `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerQueryValueW`
- `wer.dll` (5): `WerReportAddFile`, `WerReportCloseHandle`, `WerReportCreate`, `WerReportSetParameter`, `WerReportSubmit`
- `WindowsCodecs.dll` (1): `WICConvertBitmapSource`
- `XmlLite.dll` (2): `CreateXmlReader`, `CreateXmlWriter`

### Exports (5)

`DllCanUnloadNow`, `DllRegisterServer`, `DllUnregisterServer`, `ShowChooser`, `ShowTools`

## `bin/F12Resources.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180001130` (RVA `0x1130`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `F12Resources.pdb`.

### Static imports

- `KERNEL32.dll` (6): `DisableThreadLibraryCalls`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `GetTickCount`, `QueryPerformanceCounter`

Exports: none recovered.

## `bin/F12Tools.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180043610` (RVA `0x43610`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `F12Tools.pdb`.

### Static imports

- `ADVAPI32.dll` (29): `AddAce`, `CopySid`, `GetAclInformation`, `GetLengthSid`, `GetSecurityDescriptorControl`, `GetSecurityDescriptorDacl`, `GetSecurityDescriptorGroup`, `GetSecurityDescriptorLength`, `GetSecurityDescriptorOwner`, `GetSecurityDescriptorSacl`, `GetSidLengthRequired`, `GetSidSubAuthority`, `GetTokenInformation`, `InitializeAcl`, `InitializeSecurityDescriptor`, `InitializeSid`, `IsValidSid`, `MakeAbsoluteSD`, `MakeSelfRelativeSD`, `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `SetSecurityDescriptorDacl`
- `COMCTL32.dll` (3): `InitCommonControlsEx`, `ordinal:410`, `ordinal:413`
- `KERNEL32.dll` (67): `ActivateActCtx`, `CloseHandle`, `CompareStringOrdinal`, `CreateActCtxW`, `CreateEventW`, `CreatePipe`, `CreateProcessW`, `CreateThread`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `EncodePointer`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindResourceExW`, `FlushInstructionCache`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetSystemWindowsDirectoryW`, `GetThreadLocale`, `GetTickCount`, `GetTickCount64`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsWow64Process`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LocalAlloc`, `LocalFree`, `LockResource`, `lstrcmpiW`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ResetEvent`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetThreadLocale`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WaitForSingleObject`
- `msvcrt.dll` (46): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??8type_info@@QEBAHAEBV0@@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcslwr_s`, `_XcptFilter`, `calloc`, `free`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `vswprintf_s`, `wcscat_s`, `wcschr`, `wcscpy_s`, `wcsncmp`, `wcsncpy_s`, `wcsrchr`, `wcsstr`
- `ole32.dll` (10): `CoCreateInstance`, `CoGetInterfaceAndReleaseStream`, `CoInitializeEx`, `CoMarshalInterThreadInterfaceInStream`, `CoRegisterMessageFilter`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`, `StringFromGUID2`
- `OLEAUT32.dll` (17): `ordinal:10`, `ordinal:12`, `ordinal:146`, `ordinal:149`, `ordinal:150`, `ordinal:161`, `ordinal:162`, `ordinal:163`, `ordinal:186`, `ordinal:2`, `ordinal:277`, `ordinal:314`, `ordinal:4`, `ordinal:6`, `ordinal:7`, `ordinal:8`, `ordinal:9`
- `SHELL32.dll` (1): `SHGetSpecialFolderPathW`
- `SHLWAPI.dll` (5): `PathFileExistsW`, `PathGetCharTypeW`, `PathRemoveFileSpecW`, `ordinal:176`, `ordinal:219`
- `USER32.dll` (38): `AllowSetForegroundWindow`, `AttachThreadInput`, `CallWindowProcW`, `CharNextW`, `CreateWindowExW`, `DefWindowProcW`, `DestroyAcceleratorTable`, `DestroyWindow`, `DispatchMessageW`, `GetAsyncKeyState`, `GetClassInfoExW`, `GetClientRect`, `GetForegroundWindow`, `GetSystemMetrics`, `GetWindowLongPtrW`, `GetWindowThreadProcessId`, `InSendMessage`, `InSendMessageEx`, `IsIconic`, `IsWindow`, `LoadAcceleratorsW`, `LoadCursorW`, `MapWindowPoints`, `MsgWaitForMultipleObjects`, `PeekMessageW`, `PostMessageW`, `RegisterClassExW`, `RegisterWindowMessageW`, `ReplyMessage`, `SendMessageW`, `SetFocus`, `SetForegroundWindow`, `SetParent`, `SetWindowLongPtrW`, `SetWindowPos`, `TranslateAcceleratorW`, `TranslateMessage`, `UnregisterClassA`

### Exports (5)

`DllCanUnloadNow`, `DllGetClassObject`, `DllInstall`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/IEShims.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x1800010e0` (RVA `0x10e0`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `ieshims.pdb`.

### Static imports

- `api-ms-win-downlevel-advapi32-l1-1-0.dll` (9): `RegCloseKey`, `RegCreateKeyExW`, `RegEnumKeyExW`, `RegEnumValueW`, `RegGetValueW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll` (11): `PathFindFileNameW`, `PathGetArgsW`, `PathIsUNCW`, `PathSkipRootW`, `StrCmpCW`, `StrCmpICA`, `StrCmpICW`, `StrCmpIW`, `StrCmpNCW`, `StrCmpNICW`, `StrDupW`
- `iertutil.dll` (10): `ordinal:101`, `ordinal:134`, `ordinal:137`, `ordinal:170`, `ordinal:45`, `ordinal:50`, `ordinal:58`, `ordinal:751`, `ordinal:791`, `ordinal:916`
- `KERNEL32.dll` (90): `CloseHandle`, `CopyFileExW`, `CreateDirectoryW`, `CreateFileMappingW`, `CreateFileW`, `CreateMutexW`, `DecodePointer`, `DelayLoadFailureHook`, `DeleteCriticalSection`, `DeleteProcThreadAttributeList`, `DeviceIoControl`, `DuplicateHandle`, `EncodePointer`, `EnterCriticalSection`, `ExitThread`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileW`, `FindNextFileW`, `FreeLibrary`, `GetCurrentDirectoryW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableW`, `GetFileAttributesW`, `GetFileInformationByHandle`, `GetFileSizeEx`, `GetFullPathNameW`, `GetLastError`, `GetLogicalDriveStringsW`, `GetLongPathNameW`, `GetModuleFileNameW`, `GetModuleHandleA`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetProcessId`, `GetProcessIdOfThread`, `GetSystemDirectoryW`, `GetSystemTimeAsFileTime`, `GetThreadId`, `GetTickCount`, `GetWindowsDirectoryW`, `HeapAlloc`, `HeapFree`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `InitializeProcThreadAttributeList`, `IsWow64Process`, `LeaveCriticalSection`, `LoadLibraryA`, `LoadLibraryExA`, `LoadLibraryW`, `LocalAlloc`, `LocalFree`, `lstrcmpiW`, `MapViewOfFile`, `MultiByteToWideChar`, `OpenEventW`, `OpenFileMappingW`, `OpenProcess`, `OutputDebugStringA`, `OutputDebugStringW`, `QueryDosDeviceW`, `QueryFullProcessImageNameW`, `QueryPerformanceCounter`, `ReleaseMutex`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SearchPathW`, `SetEnvironmentVariableW`, `SetFileAttributesW`, `SetLastError`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `UnmapViewOfFile`, `VirtualProtect`, `VirtualQuery`, `WaitForSingleObject`, `WaitForSingleObjectEx`, `WideCharToMultiByte`
- `msvcrt.dll` (41): `??1type_info@@UEAA@XZ`, `?terminate@@YAXXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_CxxThrowException`, `_initterm`, `_lock`, `_onexit`, `_stricmp`, `_unlock`, `_vscwprintf`, `_vsnwprintf`, `_wcsicmp`, `_wcslwr`, `_wcsnicmp`, `_wfopen`, `_XcptFilter`, `calloc`, `fclose`, `fputws`, `free`, `iswctype`, `iswspace`, `malloc`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `towlower`, `wcschr`, `wcscmp`, `wcsncmp`, `wcspbrk`, `wcsrchr`, `wcsspn`, `wcsstr`, `wcstok_s`
- `ntdll.dll` (2): `NtQueryObject`, `RtlNtStatusToDosError`

### Delay-load imports

- `ADVAPI32.dll` (2): `DecryptFileW`, `EncryptFileW`
- `api-ms-win-downlevel-ole32-l1-1-0.dll` (6): `CoCreateInstance`, `CoInitializeEx`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoUninitialize`, `StringFromGUID2`
- `credui.dll` (2): `SspiPromptForCredentialsA`, `SspiPromptForCredentialsW`
- `MPR.dll` (1): `WNetGetConnectionW`
- `OLEAUT32.dll` (4): `ordinal:2`, `ordinal:6`, `ordinal:8`, `ordinal:9`
- `SHELL32.dll` (3): `ShellExecuteExW`, `SHGetDesktopFolder`, `SHGetFolderPathW`
- `USER32.dll` (14): `AllowSetForegroundWindow`, `EnumChildWindows`, `GetActiveWindow`, `GetAncestor`, `GetClassNameW`, `GetForegroundWindow`, `GetGUIThreadInfo`, `GetParent`, `GetPropW`, `GetWindowLongW`, `GetWindowThreadProcessId`, `IsChild`, `SetLayeredWindowAttributes`, `SetWindowLongPtrW`

### Exports (10)

`AcRedirNotify`, `AcRedirNotifySetEnabled`, `AcRedirSetEnabled`, `IEShims_AdminCheckAndLaunch`, `IEShims_CreateWindowEx`, `IEShims_GetOriginatingThreadId`, `IEShims_InDllMainContext`, `IEShims_Initialize`, `IEShims_SetRedirectRegistryForThread`, `IEShims_Uninitialize`

## `bin/JSProfilerCore.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x18000b70c` (RVA `0xb70c`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **False**.
- PDB: `JSProfilerCore.pdb`.

### Static imports

- `ADVAPI32.dll` (7): `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`
- `iertutil.dll` (1): `CreateUri`
- `KERNEL32.dll` (41): `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `FindResourceExW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTempPathW`, `GetTickCount`, `GetVersionExW`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadResource`, `lstrcmpiW`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `msvcrt.dll` (36): `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??_V@YAXPEAX@Z`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_aligned_free`, `_aligned_malloc`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_wfopen_s`, `_XcptFilter`, `calloc`, `fclose`, `fread`, `free`, `fwrite`, `malloc`, `memcpy`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `wcsncmp`, `wcsncpy_s`
- `ole32.dll` (4): `CoCreateInstance`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`
- `OLEAUT32.dll` (9): `ordinal:15`, `ordinal:16`, `ordinal:2`, `ordinal:23`, `ordinal:24`, `ordinal:277`, `ordinal:6`, `ordinal:8`, `ordinal:9`
- `USER32.dll` (2): `CharNextW`, `UnregisterClassA`
- `WINMM.dll` (2): `timeBeginPeriod`, `timeEndPeriod`

### Exports (2)

`DllCanUnloadNow`, `DllGetClassObject`

## `bin/MemoryAnalyzer.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x1801b2700` (RVA `0x1b2700`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `MemoryAnalyzer.pdb`.

### Static imports

- `KERNEL32.dll` (57): `CloseHandle`, `CloseThreadpool`, `CloseThreadpoolCleanupGroup`, `CloseThreadpoolCleanupGroupMembers`, `CreateFileW`, `CreateThreadpool`, `CreateThreadpoolCleanupGroup`, `DecodePointer`, `DeleteCriticalSection`, `EncodePointer`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindResourceExW`, `FlushInstructionCache`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionEx`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadResource`, `LockResource`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReadFile`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetLastError`, `SetThreadpoolThreadMaximum`, `SetThreadpoolThreadMinimum`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TrySubmitThreadpoolCallback`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WideCharToMultiByte`
- `msvcrt.dll` (47): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `__RTDynamicCast`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_errno`, `_initterm`, `_lock`, `_mbschr`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcstoi64`, `_wcstoui64`, `_XcptFilter`, `clock`, `free`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `tolower`, `toupper`, `vswprintf_s`, `wcscat_s`, `wcscmp`, `wcscpy_s`, `wcsncpy_s`, `wcsstr`, `wcstod`
- `ole32.dll` (1): `CoCreateInstance`
- `OLEAUT32.dll` (8): `ordinal:10`, `ordinal:161`, `ordinal:162`, `ordinal:2`, `ordinal:6`, `ordinal:7`, `ordinal:8`, `ordinal:9`
- `USER32.dll` (11): `CallWindowProcW`, `CreateWindowExW`, `DefWindowProcW`, `DestroyWindow`, `GetClassInfoExW`, `GetWindowLongPtrW`, `LoadCursorW`, `PostMessageW`, `RegisterClassExW`, `SetWindowLongPtrW`, `UnregisterClassA`

### Exports (2)

`DllCanUnloadNow`, `DllGetClassObject`

## `bin/Timeline.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x1800299e0` (RVA `0x299e0`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `Timeline.pdb`.

### Static imports

- `KERNEL32.dll` (33): `DeleteCriticalSection`, `EnterCriticalSection`, `FindResourceExW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionEx`, `LeaveCriticalSection`, `LoadResource`, `LockResource`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `msvcrt.dll` (47): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_ui64tow_s`, `_ultow_s`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcstoi64`, `_wtoi`, `_XcptFilter`, `floor`, `free`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `toupper`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcsncmp`, `wcsncpy_s`, `wcsnlen`, `wcsstr`, `wcstol`
- `ole32.dll` (1): `CoCreateInstance`
- `OLEAUT32.dll` (10): `ordinal:10`, `ordinal:149`, `ordinal:150`, `ordinal:161`, `ordinal:162`, `ordinal:2`, `ordinal:6`, `ordinal:7`, `ordinal:8`, `ordinal:9`
- `SHLWAPI.dll` (2): `PathFileExistsW`, `PathGetCharTypeW`
- `USER32.dll` (1): `UnregisterClassA`

### Exports (2)

`DllCanUnloadNow`, `DllGetClassObject`

## `bin/Timeline_is.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180021450` (RVA `0x21450`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `Timeline_is.pdb`.

### Static imports

- `KERNEL32.dll` (30): `DeleteCriticalSection`, `EnterCriticalSection`, `FindResourceExW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetFileAttributesW`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadResource`, `LockResource`, `MultiByteToWideChar`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `msvcrt.dll` (36): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_resetstkoflw`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wtoi`, `_XcptFilter`, `free`, `malloc`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `toupper`, `vswprintf_s`, `wcscmp`, `wcsncpy_s`, `wcsstr`, `wcstoul`
- `ole32.dll` (1): `CoCreateInstance`
- `OLEAUT32.dll` (5): `ordinal:10`, `ordinal:176`, `ordinal:2`, `ordinal:8`, `ordinal:9`
- `RPCRT4.dll` (1): `UuidFromStringW`
- `SHLWAPI.dll` (1): `SHCreateStreamOnFileEx`
- `tdh.dll` (2): `TdhGetProperty`, `TdhGetPropertySize`
- `USER32.dll` (1): `UnregisterClassA`
- `XmlLite.dll` (1): `CreateXmlReader`

### Exports (4)

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/en-US/DiagnosticsTap.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/en-US/F12.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/en-US/F12Resources.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/en-US/F12Tools.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/en-US/iedvtool.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/en-US/ieinstal.exe.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/en-US/iexplore.exe.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/en-US/jsdbgui.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/en-US/jsprofilerui.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/en-US/networkinspection.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/iediagcmd.exe`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x43f81e` (RVA `0x3f81e`).
- ImageBase: `0x400000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **True**.
- PDB: `IEDiagCmd.pdb`.

### Static imports

- `mscoree.dll` (1): `_CorExeMain`

Exports: none recovered.

## `bin/iedvtool.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180099490` (RVA `0x99490`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `iedvtool.pdb`.

### Static imports

- `ADVAPI32.dll` (10): `EventRegister`, `EventUnregister`, `EventWrite`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`
- `GDI32.dll` (36): `BitBlt`, `CreateBitmap`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateFontIndirectW`, `CreateFontW`, `CreatePatternBrush`, `CreatePen`, `CreateRectRgn`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `GetBkColor`, `GetCurrentObject`, `GetDeviceCaps`, `GetObjectW`, `GetPixel`, `GetStockObject`, `GetTextColor`, `GetTextExtentPoint32W`, `GetTextExtentPointW`, `LineTo`, `MoveToEx`, `PatBlt`, `Rectangle`, `SelectClipRgn`, `SelectObject`, `SetBkColor`, `SetBkMode`, `SetGraphicsMode`, `SetLayout`, `SetTextAlign`, `SetTextColor`, `SetWorldTransform`, `StretchBlt`, `TextOutW`
- `IEFRAME.dll` (9): `IEAssociateThreadWithTab`, `IECancelSaveFile`, `IEGetWriteableFolderPath`, `IEIsProtectedModeProcess`, `IESaveFile`, `IEShowSaveFileDialog`, `ordinal:318`, `ordinal:319`, `ordinal:320`
- `iertutil.dll` (22): `ordinal:347`, `ordinal:453`, `ordinal:457`, `ordinal:458`, `ordinal:518`, `ordinal:519`, `ordinal:575`, `ordinal:576`, `ordinal:61`, `ordinal:64`, `ordinal:65`, `ordinal:650`, `ordinal:651`, `ordinal:654`, `ordinal:655`, `ordinal:656`, `ordinal:657`, `ordinal:660`, `ordinal:68`, `ordinal:681`, `ordinal:70`, `ordinal:791`
- `KERNEL32.dll` (95): `ActivateActCtx`, `CloseHandle`, `CreateActCtxW`, `CreateDirectoryW`, `CreateEventW`, `CreateFileW`, `CreateThread`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `DeleteFileW`, `EncodePointer`, `EnterCriticalSection`, `EnumUILanguagesW`, `ExpandEnvironmentStringsW`, `FileTimeToLocalFileTime`, `FileTimeToSystemTime`, `FindResourceExW`, `FindResourceW`, `FlushInstructionCache`, `FormatMessageW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetDateFormatA`, `GetFileAttributesW`, `GetLastError`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTickCount`, `GetTickCount64`, `GetTimeFormatA`, `GetUserDefaultUILanguage`, `GlobalAddAtomW`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsDebuggerPresent`, `K32GetModuleBaseNameW`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadLibraryW`, `LoadResource`, `LocalAlloc`, `LocalFree`, `LockResource`, `lstrcmpA`, `lstrcmpiA`, `lstrcmpiW`, `lstrcmpW`, `MulDiv`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReleaseActCtx`, `ResetEvent`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `VirtualProtect`, `VirtualQuery`, `WaitForSingleObject`, `WideCharToMultiByte`, `WriteFile`
- `MSHTML.dll` (1): `ordinal:127`
- `MSIMG32.dll` (2): `GradientFill`, `TransparentBlt`
- `msvcrt.dll` (55): `??1type_info@@UEAA@XZ`, `?terminate@@YAXXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_CxxThrowException`, `_errno`, `_initterm`, `_itow_s`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_vsnwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcsnicmp`, `_wfopen_s`, `_XcptFilter`, `atan2`, `calloc`, `cos`, `fclose`, `floor`, `fputs`, `fputws`, `free`, `iswalpha`, `iswascii`, `iswdigit`, `iswspace`, `malloc`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `sin`, `sprintf_s`, `sqrt`, `strchr`, `strtoul`, `swprintf_s`, `toupper`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcscspn`, `wcsncmp`, `wcsncpy_s`, `wcsrchr`, `wcsspn`, `wcsstr`, `wcstol`
- `ole32.dll` (12): `CoCreateInstance`, `CoGetInterfaceAndReleaseStream`, `CoInitializeEx`, `CoMarshalInterThreadInterfaceInStream`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `StringFromGUID2`
- `OLEACC.dll` (2): `CreateStdAccessibleObject`, `LresultFromObject`
- `OLEAUT32.dll` (17): `ordinal:10`, `ordinal:112`, `ordinal:12`, `ordinal:149`, `ordinal:150`, `ordinal:16`, `ordinal:2`, `ordinal:25`, `ordinal:277`, `ordinal:313`, `ordinal:314`, `ordinal:4`, `ordinal:6`, `ordinal:7`, `ordinal:8`, `ordinal:84`, `ordinal:9`
- `SHELL32.dll` (3): `SHGetFolderPathW`, `SHGetKnownFolderPath`, `ordinal:171`
- `SHLWAPI.dll` (20): `PathFindExtensionW`, `PathFindFileNameW`, `PathRemoveFileSpecW`, `PathUndecorateW`, `SHCreateStreamOnFileW`, `SHDeleteKeyW`, `StrChrA`, `StrChrW`, `StrCmpIW`, `StrCmpW`, `StrRChrW`, `StrStrIW`, `StrStrW`, `StrToIntW`, `UrlCanonicalizeW`, `ordinal:158`, `ordinal:176`, `ordinal:2`, `ordinal:219`, `ordinal:225`
- `urlmon.dll` (10): `CoInternetCombineIUri`, `CoInternetCreateZoneManager`, `CoInternetIsFeatureEnabled`, `CreateUri`, `GetMarkOfTheWeb`, `UrlMkSetSessionOption`, `ordinal:423`, `ordinal:446`, `ordinal:447`, `ordinal:449`
- `USER32.dll` (140): `AllowSetForegroundWindow`, `AppendMenuW`, `AttachThreadInput`, `BeginPaint`, `CallNextHookEx`, `CallWindowProcW`, `CharNextW`, `CheckDlgButton`, `CheckMenuItem`, `CheckMenuRadioItem`, `ClientToScreen`, `CloseClipboard`, `CloseWindow`, `CopyRect`, `CreateDialogParamW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DeleteMenu`, `DestroyAcceleratorTable`, `DestroyCursor`, `DestroyIcon`, `DestroyMenu`, `DestroyWindow`, `DialogBoxParamW`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawTextW`, `EmptyClipboard`, `EnableMenuItem`, `EnableWindow`, `EndDialog`, `EndPaint`, `EqualRect`, `FillRect`, `FindWindowExW`, `FrameRect`, `GetActiveWindow`, `GetCapture`, `GetClassInfoExW`, `GetClassLongPtrW`, `GetClassNameW`, `GetClientRect`, `GetComboBoxInfo`, `GetDC`, `GetDesktopWindow`, `GetDlgItem`, `GetDlgItemInt`, `GetDlgItemTextW`, `GetFocus`, `GetKeyState`, `GetMenuState`, `GetMessagePos`, `GetParent`, `GetPropW`, `GetSubMenu`, `GetSysColor`, `GetSysColorBrush`, `GetSystemMetrics`, `GetUpdateRect`, `GetWindow`, `GetWindowInfo`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowPlacement`, `GetWindowRect`, `GetWindowTextW`, `GetWindowThreadProcessId`, `InflateRect`, `InSendMessageEx`, `IntersectRect`, `InvalidateRect`, `IsChild`, `IsDlgButtonChecked`, `IsIconic`, `IsRectEmpty`, `IsWindow`, `IsWindowEnabled`, `IsWindowVisible`, `KillTimer`, `LoadAcceleratorsW`, `LoadCursorW`, `LoadIconW`, `LoadImageW`, `LoadMenuW`, `LoadStringW`, `MapWindowPoints`, `MessageBoxW`, `MoveWindow`, `MsgWaitForMultipleObjects`, `NotifyWinEvent`, `OffsetRect`, `OpenClipboard`, `PeekMessageW`, `PostMessageW`, `PostThreadMessageW`, `PtInRect`, `RedrawWindow`, `RegisterClassExW`, `ReleaseCapture`, `ReleaseDC`, `RemovePropW`, `ReplyMessage`, `ScreenToClient`, `SendMessageTimeoutW`, `SendMessageW`, `SetCapture`, `SetClassLongPtrW`, `SetClassLongW`, `SetClipboardData`, `SetCursor`, `SetDlgItemTextW`, `SetFocus`, `SetForegroundWindow`, `SetLayeredWindowAttributes`, `SetMenuItemInfoW`, `SetParent`, `SetPropW`, `SetRect`, `SetRectEmpty`, `SetTimer`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPlacement`, `SetWindowPos`, `SetWindowsHookExW`, `SetWindowTextW`, `ShowCaret`, `ShowWindow`, `SystemParametersInfoW`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnhookWindowsHookEx`, `UnionRect`, `UnregisterClassA`, `UpdateWindow`, `ValidateRect`, `WindowFromPoint`
- `UxTheme.dll` (1): `IsThemeActive`
- `WININET.dll` (14): `DeleteUrlCacheEntryW`, `FindFirstUrlCacheEntryW`, `FindNextUrlCacheEntryW`, `GetUrlCacheEntryInfoW`, `HttpOpenRequestW`, `InternetCanonicalizeUrlW`, `InternetCrackUrlW`, `InternetGetCookieW`, `InternetSetOptionW`, `PrivacyGetZonePreferenceW`, `PrivacySetZonePreferenceW`, `ReadUrlCacheEntryStream`, `RetrieveUrlCacheEntryStreamW`, `UnlockUrlCacheEntryStream`

### Exports (4)

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/ieinstal.exe`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x14000fa70` (RVA `0xfa70`).
- ImageBase: `0x140000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `ieinstal.pdb`.

### Static imports

- `ADVAPI32.dll` (40): `AddMandatoryAce`, `AllocateAndInitializeSid`, `CheckTokenMembership`, `ConvertStringSidToSidW`, `CopySid`, `CreateWellKnownSid`, `EqualSid`, `FreeSid`, `GetAce`, `GetKernelObjectSecurity`, `GetLengthSid`, `GetSecurityDescriptorSacl`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`, `GetTokenInformation`, `InitializeAcl`, `InitializeSecurityDescriptor`, `IsValidSid`, `OpenProcessToken`, `OpenThreadToken`, `RegCloseKey`, `RegCreateKeyA`, `RegCreateKeyExW`, `RegCreateKeyW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegEnumValueW`, `RegGetValueW`, `RegOpenCurrentUser`, `RegOpenKeyExA`, `RegOpenKeyExW`, `RegOverridePredefKey`, `RegQueryValueExA`, `RegQueryValueExW`, `RegSetValueExA`, `RegSetValueExW`, `SetEntriesInAclW`, `SetKernelObjectSecurity`, `SetSecurityDescriptorDacl`, `SetSecurityDescriptorSacl`
- `AUTHZ.dll` (5): `AuthzAccessCheck`, `AuthzFreeContext`, `AuthzFreeResourceManager`, `AuthzInitializeContextFromSid`, `AuthzInitializeResourceManager`
- `iertutil.dll` (6): `ordinal:134`, `ordinal:172`, `ordinal:200`, `ordinal:201`, `ordinal:650`, `ordinal:658`
- `KERNEL32.dll` (76): `ActivateActCtx`, `CloseHandle`, `CopyFileW`, `CreateActCtxW`, `CreateDirectoryExA`, `CreateEventW`, `CreateFileA`, `CreateFileW`, `CreateProcessW`, `CreateThread`, `DeactivateActCtx`, `DeleteCriticalSection`, `DeleteFileA`, `DeleteFileW`, `DuplicateHandle`, `EnterCriticalSection`, `FindClose`, `FindFirstFileA`, `FindNextFileA`, `FlushInstructionCache`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThread`, `GetCurrentThreadId`, `GetExitCodeThread`, `GetFileAttributesA`, `GetFileAttributesW`, `GetFinalPathNameByHandleW`, `GetFullPathNameW`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetSystemTimeAsFileTime`, `GetTempPathA`, `GetThreadContext`, `GetTickCount`, `GetVersionExA`, `HeapAlloc`, `HeapFree`, `HeapSetInformation`, `InitializeCriticalSection`, `K32GetModuleBaseNameW`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadLibraryW`, `LocalAlloc`, `LocalFree`, `lstrcmpA`, `lstrcmpiA`, `lstrcmpiW`, `MultiByteToWideChar`, `OpenProcess`, `QueryPerformanceCounter`, `ReleaseActCtx`, `RemoveDirectoryA`, `ResumeThread`, `SetEvent`, `SetFileAttributesA`, `SetLastError`, `SetProcessShutdownParameters`, `SetThreadContext`, `SetUnhandledExceptionFilter`, `Sleep`, `SuspendThread`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `VirtualProtect`, `VirtualQuery`, `WaitForSingleObject`, `WideCharToMultiByte`
- `msvcrt.dll` (32): `?terminate@@YAXXZ`, `__C_specific_handler`, `__dllonexit`, `__set_app_type`, `__setusermatherr`, `__wgetmainargs`, `_amsg_exit`, `_cexit`, `_commode`, `_exit`, `_fmode`, `_initterm`, `_lock`, `_onexit`, `_unlock`, `_vsnprintf`, `_vsnwprintf`, `_wcmdln`, `_wcsnicmp`, `_wtoi`, `_XcptFilter`, `exit`, `iscntrl`, `iswalpha`, `iswascii`, `iswcntrl`, `memcpy_s`, `memset`, `rand_s`, `wcschr`, `wcsrchr`, `wcstok`
- `ntdll.dll` (4): `NtFreeVirtualMemory`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`
- `ole32.dll` (14): `CLSIDFromString`, `CoCreateInstance`, `CoGetCallContext`, `CoImpersonateClient`, `CoInitialize`, `CoInitializeEx`, `CoInitializeSecurity`, `CoRegisterClassObject`, `CoRevertToSelf`, `CoRevokeClassObject`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoUninitialize`, `StringFromGUID2`
- `OLEAUT32.dll` (7): `ordinal:163`, `ordinal:186`, `ordinal:2`, `ordinal:442`, `ordinal:443`, `ordinal:6`, `ordinal:7`
- `RPCRT4.dll` (3): `RpcStringFreeW`, `UuidCreate`, `UuidToStringW`
- `urlmon.dll` (6): `CoInternetCreateSecurityManager`, `CoInternetSetFeatureEnabled`, `CompatFlagsFromClsid`, `Extract`, `ordinal:107`, `ordinal:519`
- `USER32.dll` (3): `CharNextW`, `LoadStringW`, `PostQuitMessage`
- `WINTRUST.dll` (4): `CryptCATAdminAcquireContext`, `CryptCATAdminAddCatalog`, `CryptCATAdminReleaseCatalogContext`, `CryptCATAdminReleaseContext`

Exports: none recovered.

## `bin/ielowutil.exe`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x140002940` (RVA `0x2940`).
- ImageBase: `0x140000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `ielowutil.pdb`.

### Static imports

- `iertutil.dll` (1): `ordinal:466`
- `KERNEL32.dll` (39): `ActivateActCtx`, `CloseHandle`, `CreateActCtxW`, `CreateEventW`, `CreateThread`, `DeactivateActCtx`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVersionExA`, `HeapAlloc`, `HeapFree`, `HeapSetInformation`, `IsWow64Process`, `LoadLibraryExW`, `MapViewOfFile`, `OpenEventW`, `OpenFileMappingW`, `QueryPerformanceCounter`, `ReleaseActCtx`, `ResetEvent`, `SetEvent`, `SetLastError`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `UnmapViewOfFile`, `VirtualAlloc`, `WaitForSingleObject`
- `msvcrt.dll` (20): `?terminate@@YAXXZ`, `__C_specific_handler`, `__set_app_type`, `__setusermatherr`, `__wgetmainargs`, `_amsg_exit`, `_cexit`, `_commode`, `_exit`, `_fmode`, `_initterm`, `_vsnwprintf`, `_wcmdln`, `_wcsnicmp`, `_wtoi`, `_XcptFilter`, `exit`, `memset`, `rand_s`, `wcstok`
- `ntdll.dll` (3): `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`
- `ole32.dll` (7): `CLSIDFromString`, `CoCreateInstance`, `CoInitializeEx`, `CoInitializeSecurity`, `CoRegisterClassObject`, `CoRevokeClassObject`, `CoUninitialize`
- `USER32.dll` (5): `DispatchMessageW`, `MsgWaitForMultipleObjects`, `PeekMessageW`, `PostQuitMessage`, `TranslateMessage`
- `WININET.dll` (2): `InternetGetCookieExW`, `InternetSetCookieExW`

Exports: none recovered.

## `bin/ieproxy.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180001ce0` (RVA `0x1ce0`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **False**.
- PDB: `IEProxy.pdb`.

### Static imports

- `api-ms-win-downlevel-advapi32-l1-1-0.dll` (6): `GetAce`, `GetKernelObjectSecurity`, `GetSecurityDescriptorDacl`, `GetSidIdentifierAuthority`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll` (7): `ParseURLW`, `PathCreateFromUrlW`, `PathIsURLW`, `QISearch`, `UrlApplySchemeW`, `UrlCanonicalizeW`, `UrlCreateFromPathW`
- `api-ms-win-downlevel-shlwapi-l2-1-0.dll` (2): `IUnknown_QueryService`, `IUnknown_SetSite`
- `KERNEL32.dll` (39): `CloseHandle`, `CompareStringOrdinal`, `CompareStringW`, `CreateFileW`, `DelayLoadFailureHook`, `DisableThreadLibraryCalls`, `FreeLibrary`, `GetCurrentDirectoryW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetFinalPathNameByHandleW`, `GetLastError`, `GetLocaleInfoEx`, `GetModuleHandleW`, `GetProcAddress`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVersionExA`, `GlobalAlloc`, `GlobalLock`, `GlobalSize`, `GlobalUnlock`, `LoadLibraryExA`, `LoadLibraryExW`, `LocalAlloc`, `LocalFree`, `QueryPerformanceCounter`, `RegCloseKey`, `RegGetValueW`, `RegOpenKeyExW`, `RegQueryValueExW`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `msvcrt.dll` (18): `??2@YAPEAX_K@Z`, `??3@YAXPEAX@Z`, `__C_specific_handler`, `__CxxFrameHandler3`, `_amsg_exit`, `_initterm`, `_purecall`, `_vsnwprintf`, `_XcptFilter`, `free`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memset`, `wcschr`, `wcsstr`
- `RPCRT4.dll` (25): `CStdStubBuffer_AddRef`, `CStdStubBuffer_Connect`, `CStdStubBuffer_CountRefs`, `CStdStubBuffer_DebugServerQueryInterface`, `CStdStubBuffer_DebugServerRelease`, `CStdStubBuffer_Disconnect`, `CStdStubBuffer_Invoke`, `CStdStubBuffer_IsIIDSupported`, `CStdStubBuffer_QueryInterface`, `IUnknown_AddRef_Proxy`, `IUnknown_QueryInterface_Proxy`, `IUnknown_Release_Proxy`, `NdrClientCall3`, `NdrCStdStubBuffer2_Release`, `NdrCStdStubBuffer_Release`, `NdrDllCanUnloadNow`, `NdrDllGetClassObject`, `NdrDllRegisterProxy`, `NdrDllUnregisterProxy`, `NdrGetUserMarshalInfo`, `NdrOleAllocate`, `NdrOleFree`, `NdrStubCall3`, `NdrStubForwardingFunction`, `RpcRaiseException`

### Delay-load imports

- `api-ms-win-downlevel-ole32-l1-1-0.dll` (2): `CoCreateInstance`, `CoGetStdMarshalEx`
- `GDI32.dll` (10): `CreateBitmap`, `CreatePalette`, `GetBitmapBits`, `GetEnhMetaFileBits`, `GetMetaFileBitsEx`, `GetObjectA`, `GetObjectType`, `GetPaletteEntries`, `SetEnhMetaFileBits`, `SetMetaFileBitsEx`
- `iertutil.dll` (3): `ordinal:44`, `ordinal:650`, `ordinal:655`
- `ole32.dll` (88): `CoAllowSetForegroundWindow`, `CoGetMarshalSizeMax`, `CoMarshalInterface`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUnmarshalInterface`, `HBITMAP_UserFree`, `HBITMAP_UserFree64`, `HBITMAP_UserMarshal`, `HBITMAP_UserMarshal64`, `HBITMAP_UserSize`, `HBITMAP_UserSize64`, `HBITMAP_UserUnmarshal`, `HBITMAP_UserUnmarshal64`, `HGLOBAL_UserFree`, `HGLOBAL_UserFree64`, `HGLOBAL_UserMarshal`, `HGLOBAL_UserMarshal64`, `HGLOBAL_UserSize`, `HGLOBAL_UserSize64`, `HGLOBAL_UserUnmarshal`, `HGLOBAL_UserUnmarshal64`, `HICON_UserFree`, `HICON_UserFree64`, `HICON_UserMarshal`, `HICON_UserMarshal64`, `HICON_UserSize`, `HICON_UserSize64`, `HICON_UserUnmarshal`, `HICON_UserUnmarshal64`, `HMENU_UserFree`, `HMENU_UserFree64`, `HMENU_UserMarshal`, `HMENU_UserMarshal64`, `HMENU_UserSize`, `HMENU_UserSize64`, `HMENU_UserUnmarshal`, `HMENU_UserUnmarshal64`, `HWND_UserFree`, `HWND_UserFree64`, `HWND_UserMarshal`, `HWND_UserMarshal64`, `HWND_UserSize`, `HWND_UserSize64`, `HWND_UserUnmarshal`, `HWND_UserUnmarshal64`, `NdrProxyForwardingFunction10`, `NdrProxyForwardingFunction11`, `NdrProxyForwardingFunction12`, `NdrProxyForwardingFunction13`, `NdrProxyForwardingFunction14`, `NdrProxyForwardingFunction3`, `NdrProxyForwardingFunction4`, `NdrProxyForwardingFunction5`, `NdrProxyForwardingFunction6`, `NdrProxyForwardingFunction7`, `NdrProxyForwardingFunction8`, `NdrProxyForwardingFunction9`, `ObjectStublessClient10`, `ObjectStublessClient11`, `ObjectStublessClient12`, `ObjectStublessClient13`, `ObjectStublessClient14`, `ObjectStublessClient15`, `ObjectStublessClient16`, `ObjectStublessClient17`, `ObjectStublessClient18`, `ObjectStublessClient19`, `ObjectStublessClient20`, `ObjectStublessClient21`, `ObjectStublessClient22`, `ObjectStublessClient23`, `ObjectStublessClient24`, `ObjectStublessClient25`, `ObjectStublessClient26`, `ObjectStublessClient27`, `ObjectStublessClient28`, `ObjectStublessClient29`, `ObjectStublessClient3`, `ObjectStublessClient30`, `ObjectStublessClient31`, `ObjectStublessClient4`, `ObjectStublessClient5`, `ObjectStublessClient6`, `ObjectStublessClient7`, `ObjectStublessClient8`, `ObjectStublessClient9`, `ReleaseStgMedium`
- `OLEAUT32.dll` (27): `BSTR_UserFree64`, `BSTR_UserMarshal64`, `BSTR_UserSize64`, `BSTR_UserUnmarshal64`, `LPSAFEARRAY_UserFree64`, `LPSAFEARRAY_UserMarshal64`, `LPSAFEARRAY_UserSize64`, `LPSAFEARRAY_UserUnmarshal64`, `VARIANT_UserFree64`, `VARIANT_UserMarshal64`, `VARIANT_UserSize64`, `VARIANT_UserUnmarshal64`, `ordinal:2`, `ordinal:283`, `ordinal:284`, `ordinal:285`, `ordinal:286`, `ordinal:287`, `ordinal:288`, `ordinal:289`, `ordinal:290`, `ordinal:291`, `ordinal:292`, `ordinal:293`, `ordinal:294`, `ordinal:6`, `ordinal:7`
- `PROPSYS.dll` (2): `PSPropertyBag_ReadDWORD`, `PSPropertyBag_ReadStrAlloc`
- `SHELL32.dll` (2): `SHCreateItemFromParsingName`, `SHCreateShellItemArrayFromShellItem`
- `USER32.dll` (5): `AllowSetForegroundWindow`, `FindWindowExW`, `GetWindowThreadProcessId`, `PostMessageW`, `SendMessageTimeoutW`

### Exports (5)

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`, `GetProxyDllInfo`

## `bin/iexplore.exe`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x1400019f0` (RVA `0x19f0`).
- ImageBase: `0x140000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `iexplore.pdb`.

### Static imports

- `api-ms-win-downlevel-advapi32-l1-1-0.dll` (8): `EventRegister`, `EventUnregister`, `EventWrite`, `EventWriteTransfer`, `RegCloseKey`, `RegGetValueW`, `RegOpenKeyExW`, `RegQueryValueExW`
- `api-ms-win-downlevel-shell32-l1-1-0.dll` (2): `CommandLineToArgvW`, `SetCurrentProcessExplicitAppUserModelID`
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll` (1): `StrStrIW`
- `iertutil.dll` (7): `ordinal:139`, `ordinal:32`, `ordinal:650`, `ordinal:701`, `ordinal:796`, `ordinal:840`, `ordinal:9`
- `KERNEL32.dll` (39): `CloseHandle`, `CreateProcessW`, `DeleteCriticalSection`, `ExpandEnvironmentStringsW`, `FreeLibrary`, `GetCommandLineW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetStartupInfoW`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVersionExA`, `HeapSetInformation`, `InitializeCriticalSection`, `IsDebuggerPresent`, `LoadLibraryExA`, `LoadLibraryExW`, `LocalAlloc`, `LocalFree`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetDllDirectoryW`, `SetErrorMode`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualProtect`, `VirtualQuery`
- `msvcrt.dll` (20): `?terminate@@YAXXZ`, `__C_specific_handler`, `__set_app_type`, `__setusermatherr`, `__wgetmainargs`, `_amsg_exit`, `_cexit`, `_commode`, `_exit`, `_fmode`, `_initterm`, `_vsnwprintf`, `_wcmdln`, `_XcptFilter`, `exit`, `iswspace`, `memcpy`, `memset`, `rand_s`, `wcsncmp`
- `USER32.dll` (6): `AllowSetForegroundWindow`, `FindWindowExW`, `GetWindowThreadProcessId`, `IsWindowEnabled`, `IsWindowVisible`, `SendMessageTimeoutW`

### Delay-load imports

- `IEFRAME.dll` (5): `ordinal:212`, `ordinal:251`, `ordinal:255`, `ordinal:256`, `ordinal:258`

Exports: none recovered.

## `bin/jsdbgui.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180052c30` (RVA `0x52c30`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **False**.
- PDB: `jsdbgui.pdb`.

### Static imports

- `ADVAPI32.dll` (10): `EventRegister`, `EventUnregister`, `EventWrite`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`
- `GDI32.dll` (35): `AbortDoc`, `BitBlt`, `CreateBitmap`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateFontIndirectW`, `CreatePatternBrush`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `EndDoc`, `EndPage`, `ExtCreatePen`, `ExtTextOutW`, `GetDeviceCaps`, `GetFontUnicodeRanges`, `GetObjectW`, `GetTextExtentPoint32W`, `GetTextExtentPointW`, `GetTextMetricsW`, `LineTo`, `MoveToEx`, `PatBlt`, `SelectObject`, `SetBkColor`, `SetBkMode`, `SetBrushOrgEx`, `SetMapMode`, `SetStretchBltMode`, `SetTextColor`, `SetViewportOrgEx`, `StartDocW`, `StartPage`, `StretchBlt`, `TextOutW`
- `iertutil.dll` (6): `ordinal:61`, `ordinal:64`, `ordinal:65`, `ordinal:650`, `ordinal:68`, `ordinal:70`
- `KERNEL32.dll` (63): `ActivateActCtx`, `CreateActCtxW`, `DeactivateActCtx`, `DeleteCriticalSection`, `EnterCriticalSection`, `EnumUILanguagesW`, `FindResourceExW`, `FlushInstructionCache`, `FormatMessageA`, `FormatMessageW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetUserDefaultUILanguage`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadLibraryW`, `LoadResource`, `LocalFree`, `LockResource`, `lstrcmpiW`, `lstrcmpW`, `lstrlenW`, `MulDiv`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReleaseActCtx`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TryEnterCriticalSection`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WideCharToMultiByte`
- `MSIMG32.dll` (1): `TransparentBlt`
- `msvcrt.dll` (50): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_CxxThrowException`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscprintf`, `_vscwprintf`, `_vsnwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcsnicmp`, `_XcptFilter`, `calloc`, `free`, `iswalnum`, `iswalpha`, `iswdigit`, `iswgraph`, `iswspace`, `iswxdigit`, `malloc`, `memcpy`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `towupper`, `vsprintf_s`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcscspn`, `wcsncpy_s`, `wcspbrk`, `wcsrchr`, `wcsspn`, `wcsstr`
- `ole32.dll` (6): `CoCreateInstance`, `CoInitialize`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`
- `OLEACC.dll` (2): `CreateStdAccessibleObject`, `LresultFromObject`
- `OLEAUT32.dll` (15): `ordinal:10`, `ordinal:12`, `ordinal:147`, `ordinal:15`, `ordinal:16`, `ordinal:2`, `ordinal:23`, `ordinal:24`, `ordinal:277`, `ordinal:314`, `ordinal:4`, `ordinal:6`, `ordinal:7`, `ordinal:8`, `ordinal:9`
- `SHLWAPI.dll` (6): `StrCmpLogicalW`, `StrCmpNW`, `StrStrIW`, `StrStrW`, `StrToIntW`, `ordinal:219`
- `urlmon.dll` (2): `CreateUri`, `ordinal:423`
- `USER32.dll` (111): `BeginPaint`, `CallNextHookEx`, `CallWindowProcW`, `CharNextW`, `CheckMenuItem`, `ClientToScreen`, `CloseClipboard`, `CreateDialogParamW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DeleteMenu`, `DestroyAcceleratorTable`, `DestroyIcon`, `DestroyMenu`, `DestroyWindow`, `DialogBoxParamW`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawMenuBar`, `DrawTextW`, `EmptyClipboard`, `EnableMenuItem`, `EnableWindow`, `EndDialog`, `EndPaint`, `FillRect`, `GetCapture`, `GetCaretPos`, `GetClassInfoExW`, `GetClientRect`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetDlgItem`, `GetDlgItemInt`, `GetFocus`, `GetForegroundWindow`, `GetKeyState`, `GetMessagePos`, `GetMonitorInfoW`, `GetParent`, `GetScrollInfo`, `GetScrollPos`, `GetSubMenu`, `GetSysColor`, `GetSysColorBrush`, `GetSystemMetrics`, `GetWindow`, `GetWindowDC`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowRect`, `GetWindowTextLengthW`, `GetWindowTextW`, `InsertMenuW`, `IntersectRect`, `InvalidateRect`, `IsChild`, `IsDialogMessageW`, `IsDlgButtonChecked`, `IsIconic`, `IsWindow`, `IsWindowVisible`, `KillTimer`, `LoadAcceleratorsW`, `LoadCursorW`, `LoadImageW`, `LoadMenuW`, `LoadStringW`, `MapWindowPoints`, `MessageBoxW`, `MonitorFromPoint`, `MoveWindow`, `OpenClipboard`, `PostMessageW`, `PtInRect`, `RedrawWindow`, `RegisterClassExW`, `ReleaseCapture`, `ReleaseDC`, `ScreenToClient`, `SendMessageW`, `SetCapture`, `SetClipboardData`, `SetCursor`, `SetDlgItemTextW`, `SetFocus`, `SetForegroundWindow`, `SetParent`, `SetRect`, `SetRectEmpty`, `SetScrollInfo`, `SetScrollPos`, `SetTimer`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPos`, `SetWindowsHookExW`, `SetWindowTextW`, `ShowWindow`, `SystemParametersInfoW`, `TrackMouseEvent`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnhookWindowsHookEx`, `UnregisterClassA`, `UpdateWindow`, `WindowFromPoint`

### Exports (3)

`CreateConsoleTab`, `CreateScriptTab`, `CreateSourceViewer`

## `bin/jsdebuggeride.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180019d70` (RVA `0x19d70`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **False**.
- PDB: `jsdebuggeride.pdb`.

### Static imports

- `ADVAPI32.dll` (8): `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`
- `KERNEL32.dll` (43): `CloseHandle`, `CreateEventW`, `DeleteCriticalSection`, `EnterCriticalSection`, `FindResourceExW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GlobalAlloc`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadResource`, `LockResource`, `lstrcmpiW`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TryEnterCriticalSection`, `UnhandledExceptionFilter`
- `msvcrt.dll` (45): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??_V@YAXPEAX@Z`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wfopen_s`, `_wtoi`, `_XcptFilter`, `calloc`, `fclose`, `feof`, `fread`, `free`, `fseek`, `ftell`, `malloc`, `memcmp`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `vswprintf_s`, `wcscmp`, `wcsncpy_s`, `wcsstr`
- `ole32.dll` (7): `CoCreateInstance`, `CoDisconnectObject`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CreateStreamOnHGlobal`, `StringFromCLSID`
- `OLEAUT32.dll` (14): `ordinal:10`, `ordinal:12`, `ordinal:149`, `ordinal:150`, `ordinal:2`, `ordinal:23`, `ordinal:24`, `ordinal:277`, `ordinal:314`, `ordinal:4`, `ordinal:6`, `ordinal:7`, `ordinal:8`, `ordinal:9`
- `SHLWAPI.dll` (1): `ordinal:219`
- `urlmon.dll` (2): `CoInternetCombineIUri`, `CreateUri`
- `USER32.dll` (6): `CharNextW`, `DispatchMessageW`, `MsgWaitForMultipleObjects`, `PeekMessageW`, `TranslateMessage`, `UnregisterClassA`
- `WININET.dll` (7): `InternetCloseHandle`, `InternetOpenUrlW`, `InternetOpenW`, `InternetReadFile`, `ReadUrlCacheEntryStream`, `RetrieveUrlCacheEntryStreamW`, `UnlockUrlCacheEntryStream`

### Exports (2)

`DllCanUnloadNow`, `DllGetClassObject`

## `bin/jsprofilerui.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180027260` (RVA `0x27260`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **False**.
- PDB: `jsprofilerui.pdb`.

### Static imports

- `ADVAPI32.dll` (7): `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`
- `GDI32.dll` (20): `BitBlt`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateFontIndirectW`, `CreateFontW`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `ExtTextOutW`, `GetDeviceCaps`, `GetObjectW`, `GetTextExtentExPointW`, `GetTextExtentPoint32W`, `GetTextExtentPointW`, `SelectObject`, `SetBkColor`, `SetBkMode`, `SetLayout`, `SetTextAlign`, `SetTextColor`
- `iertutil.dll` (6): `CreateUri`, `ordinal:61`, `ordinal:64`, `ordinal:65`, `ordinal:68`, `ordinal:70`
- `KERNEL32.dll` (69): `ActivateActCtx`, `CloseHandle`, `CreateActCtxW`, `CreateDirectoryW`, `CreateEventW`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `DeleteFileW`, `EncodePointer`, `EnterCriticalSection`, `EnumUILanguagesW`, `FindResourceExW`, `FlushInstructionCache`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableA`, `GetFileAttributesW`, `GetLastError`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetNumberFormatW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTickCount`, `GetUserDefaultUILanguage`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LockResource`, `lstrcmpiW`, `lstrcmpW`, `MulDiv`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReleaseActCtx`, `ResetEvent`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`
- `msvcrt.dll` (44): `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_CxxThrowException`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_ultow_s`, `_unlock`, `_vscwprintf`, `_vsnwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wfopen_s`, `_XcptFilter`, `atoi`, `calloc`, `fclose`, `fputs`, `fputws`, `free`, `iswspace`, `malloc`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcsncpy_s`, `wcsstr`, `wcstol`
- `ole32.dll` (4): `CoCreateInstance`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`
- `OLEACC.dll` (2): `CreateStdAccessibleObject`, `LresultFromObject`
- `OLEAUT32.dll` (10): `ordinal:10`, `ordinal:12`, `ordinal:147`, `ordinal:2`, `ordinal:277`, `ordinal:4`, `ordinal:6`, `ordinal:8`, `ordinal:84`, `ordinal:9`
- `SHLWAPI.dll` (1): `ordinal:219`
- `urlmon.dll` (1): `ordinal:423`
- `USER32.dll` (90): `AdjustWindowRectEx`, `AppendMenuW`, `BeginPaint`, `CallWindowProcW`, `CharNextW`, `CheckMenuItem`, `CheckMenuRadioItem`, `ClientToScreen`, `CloseClipboard`, `CopyAcceleratorTableW`, `CreateAcceleratorTableW`, `CreateDialogParamW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DeleteMenu`, `DestroyAcceleratorTable`, `DestroyMenu`, `DestroyWindow`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawTextW`, `EmptyClipboard`, `EnableMenuItem`, `EnableWindow`, `EndPaint`, `FillRect`, `GetCapture`, `GetClassInfoExW`, `GetClientRect`, `GetCursorPos`, `GetDC`, `GetDlgCtrlID`, `GetDlgItem`, `GetFocus`, `GetKeyState`, `GetMenu`, `GetMenuItemCount`, `GetMessagePos`, `GetParent`, `GetScrollPos`, `GetSysColor`, `GetSysColorBrush`, `GetSystemMetrics`, `GetWindowLongA`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowRect`, `GetWindowTextW`, `InflateRect`, `InvalidateRect`, `IsWindow`, `IsWindowEnabled`, `IsWindowVisible`, `KillTimer`, `LoadAcceleratorsW`, `LoadCursorW`, `LoadImageW`, `LoadStringW`, `MoveWindow`, `MsgWaitForMultipleObjects`, `OpenClipboard`, `PeekMessageW`, `PostMessageW`, `PtInRect`, `RegisterClassExW`, `ReleaseCapture`, `ReleaseDC`, `ScreenToClient`, `SendMessageW`, `SetCapture`, `SetClipboardData`, `SetCursor`, `SetFocus`, `SetRect`, `SetScrollInfo`, `SetScrollPos`, `SetTimer`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPos`, `SetWindowTextW`, `ShowWindow`, `SystemParametersInfoW`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnregisterClassA`, `UpdateWindow`

### Exports (1)

`CreateProfileTab`

## `bin/msdbg2.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x18000164c` (RVA `0x164c`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `msdbg2.pdb`.

### Static imports

- `KERNEL32.dll` (64): `CloseHandle`, `CreateFileW`, `DecodePointer`, `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `EncodePointer`, `EnterCriticalSection`, `ExitProcess`, `FlushFileBuffers`, `FreeEnvironmentStringsW`, `GetACP`, `GetCommandLineA`, `GetConsoleCP`, `GetConsoleMode`, `GetCPInfo`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileType`, `GetLastError`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemTimeAsFileTime`, `HeapAlloc`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSectionAndSpinCount`, `IsDebuggerPresent`, `IsProcessorFeaturePresent`, `IsValidCodePage`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExW`, `MultiByteToWideChar`, `OutputDebugStringW`, `QueryPerformanceCounter`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetFilePointerEx`, `SetLastError`, `SetStdHandle`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`
- `ole32.dll` (4): `HWND_UserFree`, `HWND_UserMarshal`, `HWND_UserSize`, `HWND_UserUnmarshal`
- `OLEAUT32.dll` (8): `ordinal:283`, `ordinal:284`, `ordinal:285`, `ordinal:286`, `ordinal:287`, `ordinal:288`, `ordinal:289`, `ordinal:290`
- `RPCRT4.dll` (23): `CStdStubBuffer_AddRef`, `CStdStubBuffer_Connect`, `CStdStubBuffer_CountRefs`, `CStdStubBuffer_DebugServerQueryInterface`, `CStdStubBuffer_DebugServerRelease`, `CStdStubBuffer_Disconnect`, `CStdStubBuffer_Invoke`, `CStdStubBuffer_IsIIDSupported`, `CStdStubBuffer_QueryInterface`, `IUnknown_AddRef_Proxy`, `IUnknown_QueryInterface_Proxy`, `IUnknown_Release_Proxy`, `NdrClientCall2`, `NdrCStdStubBuffer2_Release`, `NdrCStdStubBuffer_Release`, `NdrDllCanUnloadNow`, `NdrDllGetClassObject`, `NdrDllRegisterProxy`, `NdrDllUnregisterProxy`, `NdrOleAllocate`, `NdrOleFree`, `NdrStubCall2`, `NdrStubForwardingFunction`

### Exports (4)

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/networkinspection.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180053280` (RVA `0x53280`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **False**.
- PDB: `networkinspection.pdb`.

### Static imports

- `ADVAPI32.dll` (8): `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`
- `GDI32.dll` (25): `BitBlt`, `CreateBitmap`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateDIBSection`, `CreateFontIndirectW`, `CreateFontW`, `CreatePatternBrush`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `ExtTextOutW`, `GetDeviceCaps`, `GetObjectW`, `GetStockObject`, `GetTextExtentExPointW`, `GetTextExtentPoint32W`, `GetTextMetricsW`, `PatBlt`, `SelectObject`, `SetBkColor`, `SetBkMode`, `SetLayout`, `SetTextColor`, `SetViewportOrgEx`
- `iertutil.dll` (8): `CreateUri`, `ordinal:61`, `ordinal:64`, `ordinal:65`, `ordinal:650`, `ordinal:654`, `ordinal:68`, `ordinal:70`
- `KERNEL32.dll` (89): `ActivateActCtx`, `CloseHandle`, `CompareFileTime`, `CompareStringW`, `CreateActCtxW`, `CreateDirectoryW`, `CreateEventW`, `CreateMutexW`, `CreateThread`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `DeleteFileW`, `EncodePointer`, `EnterCriticalSection`, `EnumUILanguagesW`, `FileTimeToLocalFileTime`, `FileTimeToSystemTime`, `FindResourceExW`, `FlushInstructionCache`, `FormatMessageW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetDateFormatW`, `GetDurationFormatEx`, `GetFileAttributesW`, `GetLastError`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetNumberFormatW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTickCount`, `GetTickCount64`, `GetTimeFormatW`, `GetTimeZoneInformation`, `GetUserDefaultUILanguage`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadLibraryW`, `LoadResource`, `LocalFree`, `LockResource`, `lstrcmpiW`, `lstrcmpW`, `lstrlenW`, `MulDiv`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReleaseActCtx`, `ReleaseMutex`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetThreadPriority`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `SystemTimeToFileTime`, `TerminateProcess`, `TzSpecificLocalTimeToSystemTime`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WaitForMultipleObjects`, `WaitForSingleObject`, `WideCharToMultiByte`
- `MSIMG32.dll` (1): `AlphaBlend`
- `msvcrt.dll` (56): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_CxxThrowException`, `_errno`, `_initterm`, `_ismbcspace`, `_lock`, `_mbschr`, `_mbscspn`, `_mbsinc`, `_mbsspn`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcsnicmp`, `_wcsupr_s`, `_wfopen_s`, `_wtoi`, `_XcptFilter`, `calloc`, `fclose`, `fputs`, `fputws`, `free`, `fwrite`, `iswspace`, `malloc`, `memcmp`, `memcpy_s`, `memmove_s`, `memset`, `qsort_s`, `realloc`, `swprintf_s`, `towupper`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcscspn`, `wcsncpy_s`, `wcsrchr`, `wcsspn`, `wcsstr`, `wcstol`
- `ole32.dll` (5): `CoCreateInstance`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CreateStreamOnHGlobal`
- `OLEACC.dll` (2): `CreateStdAccessibleObject`, `LresultFromObject`
- `OLEAUT32.dll` (9): `ordinal:10`, `ordinal:12`, `ordinal:2`, `ordinal:277`, `ordinal:4`, `ordinal:6`, `ordinal:7`, `ordinal:8`, `ordinal:9`
- `SHELL32.dll` (1): `ShellExecuteW`
- `SHLWAPI.dll` (4): `PathFindExtensionW`, `PathIsFileSpecW`, `SHCreateStreamOnFileW`, `ordinal:219`
- `urlmon.dll` (2): `FindMimeFromData`, `QueryAssociations`
- `USER32.dll` (97): `AppendMenuW`, `BeginPaint`, `CallWindowProcW`, `CharNextW`, `CharUpperW`, `CheckMenuItem`, `CheckMenuRadioItem`, `ClientToScreen`, `CloseClipboard`, `CopyAcceleratorTableW`, `CreateAcceleratorTableW`, `CreateDialogParamW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DestroyAcceleratorTable`, `DestroyMenu`, `DestroyWindow`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawTextW`, `EmptyClipboard`, `EnableMenuItem`, `EnableWindow`, `EndPaint`, `FillRect`, `GetCapture`, `GetClassInfoExW`, `GetClassNameW`, `GetClientRect`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetDlgCtrlID`, `GetDlgItem`, `GetFocus`, `GetKeyState`, `GetMessagePos`, `GetMonitorInfoW`, `GetParent`, `GetScrollInfo`, `GetSysColor`, `GetSysColorBrush`, `GetSystemMetrics`, `GetWindow`, `GetWindowDC`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowRect`, `GetWindowTextLengthW`, `GetWindowTextW`, `InvalidateRect`, `IsChild`, `IsWindow`, `IsWindowEnabled`, `IsWindowVisible`, `LoadAcceleratorsW`, `LoadBitmapW`, `LoadCursorW`, `LoadImageW`, `LoadStringW`, `MapWindowPoints`, `MessageBoxW`, `MonitorFromPoint`, `MoveWindow`, `OffsetRect`, `OpenClipboard`, `PeekMessageW`, `PostMessageW`, `PtInRect`, `RegisterClassExW`, `ReleaseCapture`, `ReleaseDC`, `ScreenToClient`, `ScrollWindowEx`, `SendMessageW`, `SetCapture`, `SetClipboardData`, `SetCursor`, `SetFocus`, `SetParent`, `SetRectEmpty`, `SetScrollInfo`, `SetScrollPos`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPos`, `SetWindowTextW`, `ShowWindow`, `SystemParametersInfoW`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnregisterClassA`, `UpdateWindow`, `WindowFromPoint`
- `VERSION.dll` (3): `GetFileVersionInfoExW`, `GetFileVersionInfoSizeExW`, `VerQueryValueW`
- `WindowsCodecs.dll` (1): `WICConvertBitmapSource`
- `WININET.dll` (9): `DeleteUrlCacheEntryW`, `FindFirstUrlCacheEntryW`, `FindNextUrlCacheEntryW`, `GetUrlCacheEntryInfoExW`, `InternetSetOptionW`, `InternetTimeToSystemTimeW`, `ReadUrlCacheEntryStream`, `RetrieveUrlCacheEntryStreamW`, `UnlockUrlCacheEntryStream`

### Exports (1)

`CreateNetworkTab`

## `bin/pdm.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180036a54` (RVA `0x36a54`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `pdm.pdb`.

### Static imports

- `ADVAPI32.dll` (33): `AddAce`, `CopySid`, `EqualSid`, `GetAclInformation`, `GetLengthSid`, `GetSecurityDescriptorControl`, `GetSecurityDescriptorDacl`, `GetSecurityDescriptorGroup`, `GetSecurityDescriptorOwner`, `GetSecurityDescriptorSacl`, `GetSidIdentifierAuthority`, `GetSidLengthRequired`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`, `GetTokenInformation`, `InitializeAcl`, `InitializeSecurityDescriptor`, `InitializeSid`, `IsValidSid`, `MakeAbsoluteSD`, `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegEnumKeyW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `SetSecurityDescriptorDacl`, `SetSecurityDescriptorSacl`
- `KERNEL32.dll` (120): `CloseHandle`, `CreateEventW`, `CreateFileMappingW`, `CreateFileW`, `CreateMutexW`, `CreateSemaphoreW`, `CreateThread`, `DecodePointer`, `DeleteCriticalSection`, `DuplicateHandle`, `EncodePointer`, `EnterCriticalSection`, `ExitProcess`, `FindResourceExW`, `FindResourceW`, `FlushFileBuffers`, `FlushInstructionCache`, `FormatMessageA`, `FormatMessageW`, `FreeEnvironmentStringsW`, `FreeLibrary`, `FreeLibraryAndExitThread`, `GetACP`, `GetCommandLineA`, `GetComputerNameW`, `GetConsoleCP`, `GetConsoleMode`, `GetCPInfo`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThread`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileAttributesW`, `GetFileType`, `GetLastError`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleA`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetThreadLocale`, `GetTickCount`, `GetVersion`, `GetVersionExW`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSectionAndSpinCount`, `InitializeCriticalSectionEx`, `InitializeSListHead`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsDebuggerPresent`, `IsProcessorFeaturePresent`, `IsValidCodePage`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadLibraryW`, `LoadResource`, `LocalFree`, `LockResource`, `lstrcmpiW`, `MapViewOfFile`, `MultiByteToWideChar`, `OpenEventW`, `OpenFileMappingW`, `OpenProcess`, `OutputDebugStringW`, `ProcessIdToSessionId`, `QueryPerformanceCounter`, `RaiseException`, `RegisterWaitForSingleObject`, `ReleaseMutex`, `ReleaseSemaphore`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlPcToFileHeader`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetEvent`, `SetFilePointerEx`, `SetLastError`, `SetStdHandle`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `UnmapViewOfFile`, `UnregisterWaitEx`, `VirtualAlloc`, `VirtualFree`, `VirtualProtect`, `VirtualQuery`, `WaitForMultipleObjects`, `WaitForSingleObject`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`
- `ole32.dll` (18): `CLSIDFromString`, `CoCreateInstance`, `CoGetObjectContext`, `CoInitialize`, `CoInitializeEx`, `CoMarshalInterface`, `CoQueryProxyBlanket`, `CoRegisterMessageFilter`, `CoReleaseMarshalData`, `CoSetProxyBlanket`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`, `CoUnmarshalInterface`, `CoWaitForMultipleHandles`, `CreateStreamOnHGlobal`, `StringFromGUID2`
- `OLEAUT32.dll` (17): `ordinal:10`, `ordinal:11`, `ordinal:12`, `ordinal:148`, `ordinal:149`, `ordinal:150`, `ordinal:17`, `ordinal:19`, `ordinal:2`, `ordinal:20`, `ordinal:277`, `ordinal:313`, `ordinal:4`, `ordinal:6`, `ordinal:7`, `ordinal:8`, `ordinal:9`
- `USER32.dll` (17): `CallWindowProcW`, `CharNextW`, `CreateWindowExW`, `DefWindowProcW`, `DestroyWindow`, `DispatchMessageW`, `GetClassInfoExW`, `GetWindowLongPtrW`, `IsWindow`, `LoadCursorW`, `MsgWaitForMultipleObjects`, `MsgWaitForMultipleObjectsEx`, `PeekMessageW`, `PostMessageW`, `RegisterClassExW`, `SetWindowLongPtrW`, `UnregisterClassW`

### Delay-load imports

- `VERSION.dll` (3): `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerQueryValueW`
- `WTSAPI32.dll` (2): `WTSEnumerateProcessesW`, `WTSFreeMemory`

### Exports (4)

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/pdmproxy100.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180001210` (RVA `0x1210`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `pdmproxy100.pdb`.

### Static imports

- `KERNEL32.dll` (64): `CloseHandle`, `CreateFileW`, `DecodePointer`, `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `EncodePointer`, `EnterCriticalSection`, `ExitProcess`, `FlushFileBuffers`, `FreeEnvironmentStringsW`, `GetACP`, `GetCommandLineA`, `GetConsoleCP`, `GetConsoleMode`, `GetCPInfo`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileType`, `GetLastError`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemTimeAsFileTime`, `HeapAlloc`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSectionAndSpinCount`, `IsDebuggerPresent`, `IsProcessorFeaturePresent`, `IsValidCodePage`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExW`, `MultiByteToWideChar`, `OutputDebugStringW`, `QueryPerformanceCounter`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetFilePointerEx`, `SetLastError`, `SetStdHandle`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`
- `OLEAUT32.dll` (4): `ordinal:283`, `ordinal:284`, `ordinal:285`, `ordinal:286`
- `RPCRT4.dll` (22): `CStdStubBuffer_AddRef`, `CStdStubBuffer_Connect`, `CStdStubBuffer_CountRefs`, `CStdStubBuffer_DebugServerQueryInterface`, `CStdStubBuffer_DebugServerRelease`, `CStdStubBuffer_Disconnect`, `CStdStubBuffer_Invoke`, `CStdStubBuffer_IsIIDSupported`, `CStdStubBuffer_QueryInterface`, `IUnknown_AddRef_Proxy`, `IUnknown_QueryInterface_Proxy`, `IUnknown_Release_Proxy`, `NdrCStdStubBuffer2_Release`, `NdrCStdStubBuffer_Release`, `NdrDllCanUnloadNow`, `NdrDllGetClassObject`, `NdrDllRegisterProxy`, `NdrDllUnregisterProxy`, `NdrOleAllocate`, `NdrOleFree`, `NdrStubCall2`, `NdrStubForwardingFunction`

### Exports (4)

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/perf_nt.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x180112bd8` (RVA `0x112bd8`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **False**.
- PDB: `perf_nt.pdb`.

### Static imports

- `ADVAPI32.dll` (9): `CopySid`, `EventRegister`, `EventUnregister`, `EventWrite`, `GetLengthSid`, `IsValidSid`, `RegCloseKey`, `RegOpenKeyExW`, `RegQueryValueExW`
- `KERNEL32.dll` (71): `CloseHandle`, `CopyFileW`, `CreateDirectoryW`, `CreateEventW`, `CreateFileMappingW`, `CreateFileW`, `CreateThread`, `DebugBreak`, `DeleteCriticalSection`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindResourceExW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetDllDirectoryW`, `GetDriveTypeW`, `GetEnvironmentVariableW`, `GetFileInformationByHandleEx`, `GetFileSize`, `GetFullPathNameW`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVolumePathNameW`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeConditionVariable`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LocalAlloc`, `LockFileEx`, `LockResource`, `lstrcmpiW`, `MapViewOfFileEx`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryFullProcessImageNameW`, `QueryPerformanceCounter`, `RaiseException`, `ReadFile`, `ResumeThread`, `SetDllDirectoryW`, `SetEndOfFile`, `SetEvent`, `SetFilePointer`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `SleepConditionVariableCS`, `TerminateProcess`, `UnhandledExceptionFilter`, `UnlockFileEx`, `UnmapViewOfFile`, `WaitForSingleObjectEx`, `WakeConditionVariable`, `WideCharToMultiByte`, `WriteFile`
- `msvcrt.dll` (100): `??0bad_cast@@QEAA@AEBV0@@Z`, `??0bad_cast@@QEAA@PEBD@Z`, `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1bad_cast@@UEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `___lc_codepage_func`, `___lc_handle_func`, `___mb_cur_max_func`, `__C_specific_handler`, `__crtGetStringTypeW`, `__crtLCMapStringW`, `__CxxFrameHandler3`, `__dllonexit`, `__mb_cur_max`, `__pctype_func`, `_aligned_free`, `_aligned_malloc`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_errno`, `_i64tow`, `_i64tow_s`, `_initterm`, `_iob`, `_itow_s`, `_lock`, `_memicmp`, `_onexit`, `_purecall`, `_snwscanf_s`, `_stricmp`, `_unlock`, `_vscwprintf`, `_vsnprintf`, `_vsnwprintf`, `_wcsdup`, `_wcsicmp`, `_wcsnicmp`, `_wfsopen`, `_wtof`, `_XcptFilter`, `abort`, `calloc`, `ceil`, `fclose`, `feof`, `fflush`, `fgetc`, `fgetpos`, `fgets`, `fgetwc`, `floor`, `fopen`, `fprintf`, `fputwc`, `fputws`, `free`, `fseek`, `fsetpos`, `fwprintf`, `fwrite`, `iswdigit`, `iswspace`, `ldiv`, `malloc`, `memchr`, `memcmp`, `memcpy`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `setlocale`, `setvbuf`, `strcpy_s`, `towlower`, `ungetc`, `ungetwc`, `vfprintf`, `vswprintf_s`, `wcscat_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcscspn`, `wcsncmp`, `wcsncpy_s`, `wcsnlen`, `wcsrchr`, `wcsspn`, `wcsstr`, `wcstok_s`, `wcstol`
- `ntdll.dll` (4): `RtlCaptureContext`, `RtlLengthSid`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`
- `SHELL32.dll` (1): `SHGetFolderPathW`
- `SHLWAPI.dll` (10): `PathCombineW`, `PathFileExistsW`, `PathFindExtensionW`, `PathIsDirectoryW`, `PathIsUNCW`, `PathRemoveFileSpecW`, `PathStripPathW`, `PathStripToRootW`, `SHCreateStreamOnFileW`, `ordinal:12`
- `USER32.dll` (2): `CharLowerW`, `UnregisterClassA`
- `XmlLite.dll` (1): `CreateXmlReader`

### Delay-load imports

- `dbghelp.dll` (14): `ImageDirectoryEntryToData`, `ImageRvaToVa`, `SymCleanup`, `SymFindFileInPathW`, `SymGetModuleInfoW64`, `SymGetOptions`, `SymGetSearchPathW`, `SymInitialize`, `SymLoadModuleExW`, `SymRegisterCallbackW64`, `SymSetOptions`, `SymSetSearchPathW`, `SymSrvGetFileIndexInfoW`, `SymUnloadModule64`
- `ole32.dll` (3): `CoCreateInstance`, `CoInitializeEx`, `CoUninitialize`
- `OLEAUT32.dll` (2): `ordinal:6`, `ordinal:7`
- `VERSION.dll` (3): `GetFileVersionInfoExW`, `GetFileVersionInfoSizeExW`, `VerQueryValueW`

### Exports (4)

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/perfcore.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x18001a5ac` (RVA `0x1a5ac`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`; CLR metadata: **False**.
- PDB: `perfcore.pdb`.

### Static imports

- `ADVAPI32.dll` (5): `CloseTrace`, `EventRegister`, `EventUnregister`, `OpenTraceW`, `ProcessTrace`
- `KERNEL32.dll` (28): `DeleteCriticalSection`, `EnterCriticalSection`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadLibraryW`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `msvcrt.dll` (34): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?what@exception@@UEBAPEBDXZ`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_initterm`, `_iob`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_wcsdup`, `_wcsicmp`, `_XcptFilter`, `fprintf`, `free`, `ldiv`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove_s`, `memset`, `towlower`, `vfprintf`, `wcschr`
- `ntdll.dll` (3): `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`
- `ole32.dll` (1): `CoCreateInstance`
- `OLEAUT32.dll` (4): `ordinal:149`, `ordinal:150`, `ordinal:2`, `ordinal:6`

### Exports (4)

`DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/pt-BR/DiagnosticsTap.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/pt-BR/F12.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/pt-BR/F12Resources.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/pt-BR/F12Tools.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/pt-BR/iedvtool.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/pt-BR/ieinstal.exe.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/pt-BR/iexplore.exe.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/pt-BR/jsdbgui.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/pt-BR/jsprofilerui.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/pt-BR/networkinspection.dll.mui`

- Format: `PE32`; machine: `IMAGE_FILE_MACHINE_I386`; entry: `0x10000000` (RVA `0x0`).
- ImageBase: `0x10000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: none recovered.

No named static imports recovered (resource-only image or empty IAT).

Exports: none recovered.

## `bin/sqmapi.dll`

- Format: `PE32+`; machine: `IMAGE_FILE_MACHINE_AMD64`; entry: `0x1800014d4` (RVA `0x14d4`).
- ImageBase: `0x180000000`; subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`; CLR metadata: **False**.
- PDB: `sqmapi.pdb`.

### Static imports

- `ADVAPI32.dll` (36): `ConvertSidToStringSidW`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `CreateWellKnownSid`, `CryptAcquireContextW`, `CryptGenRandom`, `CryptReleaseContext`, `GetFileSecurityW`, `GetSecurityDescriptorDacl`, `GetSecurityDescriptorOwner`, `GetTokenInformation`, `GetTraceEnableFlags`, `GetTraceEnableLevel`, `GetTraceLoggerHandle`, `ImpersonateLoggedOnUser`, `InitializeSecurityDescriptor`, `OpenProcessToken`, `OpenThreadToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegEnumKeyW`, `RegEnumValueW`, `RegisterTraceGuidsW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RevertToSelf`, `SetEntriesInAclW`, `SetFileSecurityW`, `SetNamedSecurityInfoW`, `SetSecurityDescriptorDacl`, `TraceMessage`, `UnregisterTraceGuids`
- `KERNEL32.dll` (97): `CloseHandle`, `CompareFileTime`, `CompareStringW`, `CopyFileW`, `CreateDirectoryW`, `CreateEventW`, `CreateFileMappingW`, `CreateFileW`, `CreateMutexW`, `CreateThread`, `DelayLoadFailureHook`, `DeleteCriticalSection`, `DeleteFileW`, `DisableThreadLibraryCalls`, `DuplicateHandle`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FileTimeToSystemTime`, `FindClose`, `FindFirstFileW`, `FindNextFileW`, `FindResourceW`, `FreeLibrary`, `FreeLibraryAndExitThread`, `FreeResource`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThread`, `GetCurrentThreadId`, `GetEnvironmentVariableW`, `GetFileAttributesExW`, `GetFileAttributesW`, `GetFileSize`, `GetFileSizeEx`, `GetLastError`, `GetLongPathNameW`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetNativeSystemInfo`, `GetProcAddress`, `GetSystemDefaultLCID`, `GetSystemDirectoryW`, `GetSystemTime`, `GetSystemTimeAsFileTime`, `GetSystemWow64DirectoryW`, `GetTempFileNameW`, `GetTempPathW`, `GetThreadPriority`, `GetTickCount`, `GetUserGeoID`, `GetVersionExW`, `GlobalFree`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadLibraryW`, `LoadResource`, `LocalAlloc`, `LocalFree`, `LockResource`, `lstrlenW`, `MapViewOfFile`, `OpenFileMappingW`, `OpenMutexW`, `OutputDebugStringA`, `QueryPerformanceCounter`, `ReadFile`, `ReleaseMutex`, `ResetEvent`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetErrorMode`, `SetEvent`, `SetFileAttributesW`, `SetFilePointer`, `SetFilePointerEx`, `SetLastError`, `SetThreadPriority`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `SystemTimeToFileTime`, `TerminateProcess`, `UnhandledExceptionFilter`, `UnmapViewOfFile`, `VerifyVersionInfoW`, `VerSetConditionMask`, `VirtualAlloc`, `VirtualFree`, `VirtualProtect`, `WaitForMultipleObjectsEx`, `WaitForSingleObject`, `WideCharToMultiByte`, `WriteFile`
- `msvcrt.dll` (52): `??1type_info@@UEAA@XZ`, `__badioinfo`, `__C_specific_handler`, `__CxxFrameHandler`, `__mb_cur_max`, `__pioinfo`, `_amsg_exit`, `_callnewh`, `_CxxThrowException`, `_errno`, `_fileno`, `_initterm`, `_purecall`, `_read`, `_strtoui64`, `_vsnprintf`, `_vsnwprintf`, `_wcsicmp`, `_wcsnicmp`, `_wfopen`, `_wtoi`, `_wtoi64`, `_XcptFilter`, `calloc`, `ceilf`, `fclose`, `fread`, `free`, `fseek`, `fwprintf`, `fwrite`, `isdigit`, `isleadbyte`, `iswalpha`, `iswctype`, `isxdigit`, `localeconv`, `malloc`, `mbtowc`, `memcpy`, `memset`, `rand`, `realloc`, `srand`, `time`, `ungetc`, `wcschr`, `wcsncmp`, `wcsrchr`, `wcsstr`, `wcstombs`, `wctomb`
- `ntdll.dll` (4): `NtQuerySystemTime`, `RtlAllocateHeap`, `RtlFreeHeap`, `RtlGetVersion`
- `RPCRT4.dll` (3): `RpcStringFreeW`, `UuidCreateSequential`, `UuidToStringW`
- `USER32.dll` (5): `DispatchMessageW`, `GetSystemMetrics`, `MsgWaitForMultipleObjects`, `PeekMessageW`, `TranslateMessage`

### Delay-load imports

- `Cabinet.dll` (7): `ordinal:10`, `ordinal:11`, `ordinal:13`, `ordinal:14`, `ordinal:20`, `ordinal:22`, `ordinal:23`
- `CRYPT32.dll` (4): `CertFreeCertificateChain`, `CertFreeCertificateContext`, `CertGetCertificateChain`, `CertVerifyCertificateChainPolicy`
- `ole32.dll` (6): `CoCreateGuid`, `CoCreateInstance`, `CoInitialize`, `CoInitializeEx`, `CoUninitialize`, `StringFromGUID2`
- `WINHTTP.dll` (20): `WinHttpAddRequestHeaders`, `WinHttpCloseHandle`, `WinHttpConnect`, `WinHttpCrackUrl`, `WinHttpGetDefaultProxyConfiguration`, `WinHttpGetIEProxyConfigForCurrentUser`, `WinHttpGetProxyForUrl`, `WinHttpOpen`, `WinHttpOpenRequest`, `WinHttpQueryHeaders`, `WinHttpQueryOption`, `WinHttpReadData`, `WinHttpReceiveResponse`, `WinHttpSendRequest`, `WinHttpSetCredentials`, `WinHttpSetOption`, `WinHttpSetStatusCallback`, `WinHttpSetTimeouts`, `WinHttpTimeFromSystemTime`, `WinHttpWriteData`
- `XmlLite.dll` (2): `CreateXmlReader`, `CreateXmlWriter`

### Exports (63)

`SqmAddToAverage`, `SqmAddToStream`, `SqmAddToStreamDWord`, `SqmAddToStreamDWord64`, `SqmAddToStreamString`, `SqmAddToStreamV`, `SqmCheckEscalationAddToStreamDWord`, `SqmCheckEscalationAddToStreamDWord64`, `SqmCheckEscalationAddToStreamString`, `SqmCheckEscalationSetDWord`, `SqmCheckEscalationSetDWord64`, `SqmCheckEscalationSetString`, `SqmCleanup`, `SqmClearFlags`, `SqmCreateNewId`, `SqmEndSession`, `SqmEndSessionEx`, `SqmFlushSession`, `SqmGetEnabled`, `SqmGetEscalationRuleStatus`, `SqmGetFlags`, `SqmGetInstrumentationProperty`, `SqmGetLastUploadTime`, `SqmGetMachineId`, `SqmGetSession`, `SqmGetSessionStartTime`, `SqmGetUserId`, `SqmIncrement`, `SqmIsNamespaceEnabled`, `SqmIsWindowsOptedIn`, `SqmLoadEscalationManifest`, `SqmReadSharedMachineId`, `SqmReadSharedUserId`, `SqmSet`, `SqmSetAppId`, `SqmSetAppVersion`, `SqmSetBits`, `SqmSetBool`, `SqmSetCurrentTimeAsUploadTime`, `SqmSetDWord64`, `SqmSetEnabled`, `SqmSetEscalationInfo`, `SqmSetFlags`, `SqmSetIfMax`, `SqmSetIfMin`, `SqmSetMachineId`, `SqmSetString`, `SqmSetUserId`, `SqmStartSession`, `SqmStartUpload`, `SqmStartUploadEx`, `SqmSysprepCleanup`, `SqmSysprepGeneralize`, `SqmSysprepSpecialize`, `SqmTimerAccumulate`, `SqmTimerAddToAverage`, `SqmTimerRecord`, `SqmTimerStart`, `SqmUnattendedSetup`, `SqmUnloadEscalationManifest`, `SqmWaitForUploadComplete`, `SqmWriteSharedMachineId`, `SqmWriteSharedUserId`
