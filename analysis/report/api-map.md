# Consolidated API map

Evidence: `analysis/report/generated/*.objdump.txt`; names are PE import/export table observations, not inferred prototypes.

## `bin/D3DCompiler_47.dll`

Architecture: `i386:x86-64`; entry: `0x000000018038f360`; CLR metadata: **False**.

- `ADVAPI32.dll` (12 names): `CryptAcquireContextW`, `CryptCreateHash`, `CryptDestroyHash`, `CryptGetHashParam`, `CryptHashData`, `CryptReleaseContext`, `RegCloseKey`, `RegEnumKeyExA`, `RegOpenKeyExA`, `RegOpenKeyExW`, `RegQueryValueExA`, `RegQueryValueExW`
- `KERNEL32.dll` (68 names): `CloseHandle`, `CopyFileExW`, `CreateFileA`, `CreateFileMappingW`, `CreateFileW`, `DeleteCriticalSection`, `DeleteFileW`, `DeviceIoControl`, `DisableThreadLibraryCalls`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FlushViewOfFile`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableA`, `GetFileAttributesW`, `GetFileSize`, `GetFileSizeEx`, `GetFileType`, `GetFullPathNameA`, `GetFullPathNameW`, `GetLastError`, `GetModuleFileNameA`, `GetProcAddress`, `GetProcessHeap`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVersion`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExW`, `LocalAlloc`, `LocalFree`, `MapViewOfFile`, `MapViewOfFileEx`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `ReadFile`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetFileAttributesW`, `SetFilePointer`, `SetLastError`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `UnmapViewOfFile`, `VirtualAlloc`, `VirtualFree`, `WideCharToMultiByte`, `WriteFile`, `lstrcmpiA`
- `RPCRT4.dll` (1 names): `UuidCreate`
- `msvcrt.dll` (117 names): `??1type_info@@UEAA@XZ`, `??2@YAPEAX_K@Z`, `??3@YAXPEAX@Z`, `??_U@YAPEAX_K@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `__unDName`, `_amsg_exit`, `_chsize`, `_clearfp`, `_close`, `_controlfp`, `_finite`, `_fpclass`, `_get_osfhandle`, `_initterm`, `_isnan`, `_lock`, `_lseeki64`, `_mbscmp`, `_mbstrlen`, `_memicmp`, `_onexit`, `_open_osfhandle`, `_purecall`, `_read`, `_snwprintf_s`, `_strdup`, `_stricmp`, `_strnicmp`, `_strtoui64`, `_time64`, `_unlock`, `_vsnprintf`, `_vsnwprintf`, `_wcsdup`, `_wcsicmp`, `_wcsnicmp`, `_wfsopen`, `_wfullpath`, `_wgetenv`, `_wmakepath_s`, `_write`, `_wsopen`, `_wsplitpath_s`, `acos`, `asin`, `atan`, `atan2`, `atof`, `atoi`, `bsearch`, `ceil`, `cos`, `cosh`, `exp`, `fclose`, `floor`, `floorf`, `fmod`, `fread`, `free`, `fseek`, `ftell`, `getenv`, `isalnum`, `isalpha`, `isdigit`, `isspace`, `iswdigit`, `isxdigit`, `log`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memset`, `modf`, `pow`, `qsort`, `setlocale`, `sin`, `sinh`, `sprintf_s`, `sqrt`, `sscanf`, `strcat_s`, `strchr`, `strcmp`, `strcpy_s`, `strncmp`, `strncpy_s`, `strnlen`, `strrchr`, `strstr`, `strtoul`, `swprintf_s`, `tan`, `tanh`, `tolower`, `toupper`, `towlower`, `vsprintf_s`, `wcscat_s`, `wcschr`, `wcscpy_s`, `wcsncat_s`, `wcsncmp`, `wcsncpy_s`, `wcsrchr`, `wcstol`
- Exports: `D3DAssemble`, `D3DCompile`, `D3DCompile2`, `D3DCompileFromFile`, `D3DCompressShaders`, `D3DCreateBlob`, `D3DCreateFunctionLinkingGraph`, `D3DCreateLinker`, `D3DDecompressShaders`, `D3DDisassemble`, `D3DDisassemble10Effect`, `D3DDisassemble11Trace`, `D3DDisassembleRegion`, `D3DGetBlobPart`, `D3DGetDebugInfo`, `D3DGetInputAndOutputSignatureBlob`, `D3DGetInputSignatureBlob`, `D3DGetOutputSignatureBlob`, `D3DGetTraceInstructionOffsets`, `D3DLoadModule`, `D3DPreprocess`, `D3DReadFileToBlob`, `D3DReflect`, `D3DReflectLibrary`, `D3DReturnFailure1`, `D3DSetBlobPart`, `D3DStripShader`, `D3DWriteBlobToFile`, `DebugSetMute`

## `bin/DiagnosticsHub.DataWarehouse.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180069330`; CLR metadata: **False**.

- `KERNEL32.dll` (115 names): `CloseHandle`, `CloseThreadpool`, `CloseThreadpoolCleanupGroup`, `CloseThreadpoolCleanupGroupMembers`, `CloseThreadpoolWork`, `CompareStringOrdinal`, `CompareStringW`, `CreateEventW`, `CreateFileW`, `CreateThreadpool`, `CreateThreadpoolCleanupGroup`, `CreateThreadpoolWait`, `CreateThreadpoolWork`, `DecodePointer`, `DeleteCriticalSection`, `EncodePointer`, `EnterCriticalSection`, `EnumSystemLocalesA`, `ExitProcess`, `FindResourceExW`, `FindStringOrdinal`, `FlsAlloc`, `FlsFree`, `FlsGetValue`, `FlsSetValue`, `FlushFileBuffers`, `FormatMessageW`, `FreeEnvironmentStringsW`, `FreeLibrary`, `GetACP`, `GetCPInfo`, `GetCommandLineA`, `GetConsoleCP`, `GetConsoleMode`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileAttributesW`, `GetFileType`, `GetFullPathNameW`, `GetLastError`, `GetLocaleInfoA`, `GetLocaleInfoW`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleA`, `GetModuleHandleExW`, `GetNativeSystemInfo`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetUserDefaultLCID`, `GetVersionExW`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSetInformation`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `IsValidCodePage`, `IsValidLocale`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadResource`, `LockResource`, `MultiByteToWideChar`, `OutputDebugStringA`, `OutputDebugStringW`, `QueryPerformanceCounter`, `QueryPerformanceFrequency`, `RaiseException`, `ReadConsoleW`, `ReadFile`, `ResetEvent`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlPcToFileHeader`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetEndOfFile`, `SetEvent`, `SetEventWhenCallbackReturns`, `SetFilePointer`, `SetHandleCount`, `SetLastError`, `SetStdHandle`, `SetThreadStackGuarantee`, `SetThreadpoolThreadMaximum`, `SetThreadpoolThreadMinimum`, `SetThreadpoolWait`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `SubmitThreadpoolWork`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualProtect`, `VirtualQuery`, `WaitForSingleObject`, `WaitForThreadpoolWaitCallbacks`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `USER32.dll` (1 names): `UnregisterClassA`
- `ole32.dll` (2 names): `CLSIDFromString`, `CoCreateGuid`
- Exports: `DllGetClassObject`

## `bin/DiagnosticsHub.ScriptedSandboxPlugin.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180021ce0`; CLR metadata: **False**.

- `ADVAPI32.dll` (3 names): `RegCloseKey`, `RegOpenKeyExW`, `RegQueryValueExW`
- `KERNEL32.dll` (88 names): `CloseHandle`, `CompareStringOrdinal`, `CreateFileW`, `DecodePointer`, `DeleteCriticalSection`, `EncodePointer`, `EnterCriticalSection`, `EnumSystemLocalesA`, `ExitProcess`, `FlsAlloc`, `FlsFree`, `FlsGetValue`, `FlsSetValue`, `FlushFileBuffers`, `FlushInstructionCache`, `FreeEnvironmentStringsW`, `FreeLibrary`, `GetACP`, `GetCPInfo`, `GetCommandLineA`, `GetConsoleCP`, `GetConsoleMode`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileType`, `GetLastError`, `GetLocaleInfoA`, `GetLocaleInfoW`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetUserDefaultLCID`, `GetVersionExW`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSetInformation`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsValidCodePage`, `IsValidLocale`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlPcToFileHeader`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetEnvironmentVariableW`, `SetFilePointer`, `SetHandleCount`, `SetLastError`, `SetStdHandle`, `SetThreadStackGuarantee`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `VirtualProtect`, `VirtualQuery`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `USER32.dll` (11 names): `CallWindowProcW`, `CreateWindowExW`, `DefWindowProcW`, `DestroyWindow`, `GetClassInfoExW`, `GetWindowLongPtrW`, `LoadCursorW`, `PostMessageW`, `RegisterClassExW`, `SetWindowLongPtrW`, `UnregisterClassA`
- `ole32.dll` (4 names): `CLSIDFromString`, `CoCreateGuid`, `CoCreateInstance`, `StringFromGUID2`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`

## `bin/DiagnosticsHub_is.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180008eb0`; CLR metadata: **False**.

- `KERNEL32.dll` (18 names): `DeleteCriticalSection`, `EnterCriticalSection`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `GetTickCount`, `InitializeCriticalSection`, `LeaveCriticalSection`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `msvcrt.dll` (25 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `free`, `malloc`, `memcpy`, `memcpy_s`, `memmove`, `memset`
- `ole32.dll` (1 names): `CoCreateInstance`
- `tdh.dll` (2 names): `TdhGetProperty`, `TdhGetPropertySize`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/DiagnosticsTap.dll`

Architecture: `i386:x86-64`; entry: `0x000000018002b460`; CLR metadata: **False**.

- `ADVAPI32.dll` (28 names): `AddAce`, `CopySid`, `GetAclInformation`, `GetLengthSid`, `GetSecurityDescriptorControl`, `GetSecurityDescriptorDacl`, `GetSecurityDescriptorGroup`, `GetSecurityDescriptorLength`, `GetSecurityDescriptorOwner`, `GetSecurityDescriptorSacl`, `GetSidLengthRequired`, `GetSidSubAuthority`, `GetTokenInformation`, `InitializeAcl`, `InitializeSecurityDescriptor`, `InitializeSid`, `IsValidSid`, `MakeAbsoluteSD`, `MakeSelfRelativeSD`, `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`, `SetSecurityDescriptorDacl`
- `KERNEL32.dll` (68 names): `CloseHandle`, `CompareStringOrdinal`, `CreateEventW`, `CreatePipe`, `CreateThread`, `DecodePointer`, `DeleteCriticalSection`, `DuplicateHandle`, `EncodePointer`, `EnterCriticalSection`, `FindClose`, `FindFirstFileW`, `FindResourceExW`, `FindResourceW`, `FlushInstructionCache`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableW`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetThreadLocale`, `GetTickCount`, `GetUserDefaultLCID`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LocalAlloc`, `LocalFree`, `LockResource`, `MultiByteToWideChar`, `OpenProcess`, `OutputDebugStringA`, `OutputDebugStringW`, `QueryPerformanceCounter`, `RaiseException`, `ReadFile`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetThreadLocale`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WaitForSingleObject`, `WriteFile`, `lstrcmpiW`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `SHLWAPI.dll` (2 names): `PathGetCharTypeW`, `PathRemoveFileSpecW`
- `USER32.dll` (20 names): `CallWindowProcW`, `CharNextW`, `CreateWindowExW`, `DefWindowProcW`, `DispatchMessageW`, `GetClassInfoExW`, `GetMessageW`, `GetWindowLongPtrW`, `IsWindow`, `LoadCursorW`, `PeekMessageW`, `PostMessageW`, `PostQuitMessage`, `PostThreadMessageW`, `RegisterClassExW`, `RegisterWindowMessageW`, `SendMessageW`, `SetWindowLongPtrW`, `TranslateMessage`, `UnregisterClassA`
- `msvcrt.dll` (46 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??8type_info@@QEBAHAEBV0@@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wfopen_s`, `calloc`, `fclose`, `fgetws`, `free`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `vswprintf_s`, `wcscat_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcsncpy_s`
- `ole32.dll` (5 names): `CoCreateInstance`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `StringFromGUID2`
- `urlmon.dll` (2 names): `CoInternetCombineUrlEx`, `CreateUri`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllInstall`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/F12.dll`

Architecture: `i386:x86-64`; entry: `0x00000001800ade40`; CLR metadata: **False**.

- `ADVAPI32.dll` (18 names): `CopySid`, `EventRegister`, `EventUnregister`, `EventWrite`, `GetLengthSid`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`, `GetTokenInformation`, `IsValidSid`, `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`
- `GDI32.dll` (24 names): `BitBlt`, `CombineRgn`, `CreateBitmap`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateDIBSection`, `CreateFontIndirectW`, `CreatePatternBrush`, `CreateRectRgn`, `CreateRectRgnIndirect`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `EqualRgn`, `GetDeviceCaps`, `GetObjectW`, `GetPixel`, `GetStockObject`, `GetTextExtentPoint32W`, `PatBlt`, `SelectObject`, `SetBkColor`, `SetLayout`, `SetTextColor`
- `KERNEL32.dll` (101 names): `ActivateActCtx`, `CloseHandle`, `CompareStringOrdinal`, `CopyFileW`, `CreateActCtxW`, `CreateDirectoryW`, `CreateEventW`, `CreateFileW`, `CreateThread`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `DeleteFileW`, `DuplicateHandle`, `EncodePointer`, `EnterCriticalSection`, `ExitProcess`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileW`, `FindNextFileW`, `FindResourceExW`, `FindResourceW`, `FlushInstructionCache`, `FormatMessageW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableW`, `GetFileAttributesW`, `GetFullPathNameW`, `GetLastError`, `GetLocaleInfoEx`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetProcessIdOfThread`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTempPathW`, `GetTickCount`, `GetUserDefaultUILanguage`, `GetVersionExW`, `GlobalAlloc`, `GlobalFree`, `GlobalHandle`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionEx`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsWow64Process`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LocalFree`, `LockResource`, `MoveFileW`, `MulDiv`, `MultiByteToWideChar`, `OpenProcess`, `OpenThread`, `OutputDebugStringA`, `QueryFullProcessImageNameW`, `QueryPerformanceCounter`, `QueryPerformanceFrequency`, `RaiseException`, `ReadProcessMemory`, `ReleaseActCtx`, `RemoveDirectoryW`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TlsGetValue`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WaitForMultipleObjects`, `WaitForSingleObject`, `WideCharToMultiByte`, `WriteFile`, `lstrcmpW`, `lstrcmpiW`, `lstrlenW`
- `MSIMG32.dll` (1 names): `AlphaBlend`
- `OLEACC.dll` (3 names): `CreateStdAccessibleObject`, `LresultFromObject`, `ObjectFromLresult`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `SHELL32.dll` (3 names): `SHCreateDirectoryExW`, `SHGetKnownFolderPath`, `SHGetSpecialFolderPathW`
- `SHLWAPI.dll` (7 names): `(ordinal-only import; name unavailable)`, `PathFileExistsW`, `PathFindFileNameW`, `PathGetCharTypeW`, `PathIsDirectoryW`, `PathIsRelativeW`, `StrStrIW`
- `USER32.dll` (131 names): `AdjustWindowRectEx`, `AllowSetForegroundWindow`, `AppendMenuW`, `AttachThreadInput`, `BeginPaint`, `CallNextHookEx`, `CallWindowProcW`, `ChangeWindowMessageFilterEx`, `CharNextW`, `ClientToScreen`, `CopyRect`, `CreateAcceleratorTableW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DestroyAcceleratorTable`, `DestroyMenu`, `DestroyWindow`, `DialogBoxIndirectParamW`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawTextW`, `EnableWindow`, `EndDialog`, `EndPaint`, `EnumChildWindows`, `EnumDisplayMonitors`, `EnumWindows`, `EqualRect`, `FillRect`, `GetAncestor`, `GetAsyncKeyState`, `GetCapture`, `GetClassInfoExW`, `GetClassNameW`, `GetClientRect`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetDlgCtrlID`, `GetDlgItem`, `GetDoubleClickTime`, `GetFocus`, `GetForegroundWindow`, `GetKeyState`, `GetMenu`, `GetMenuItemCount`, `GetMenuItemInfoW`, `GetMessagePos`, `GetMessageW`, `GetMonitorInfoW`, `GetParent`, `GetSysColor`, `GetSystemMetrics`, `GetWindow`, `GetWindowDC`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowPlacement`, `GetWindowRect`, `GetWindowTextLengthW`, `GetWindowTextW`, `GetWindowThreadProcessId`, `InflateRect`, `InvalidateRect`, `InvalidateRgn`, `IsChild`, `IsIconic`, `IsWindow`, `IsWindowEnabled`, `IsWindowVisible`, `IsZoomed`, `KillTimer`, `LoadAcceleratorsW`, `LoadCursorW`, `LoadImageW`, `LoadMenuW`, `LoadStringA`, `LoadStringW`, `MapDialogRect`, `MapWindowPoints`, `MessageBeep`, `MessageBoxW`, `MonitorFromPoint`, `MonitorFromWindow`, `MoveWindow`, `PeekMessageW`, `PostMessageW`, `PostQuitMessage`, `PostThreadMessageW`, `PtInRect`, `RedrawWindow`, `RegisterClassExW`, `RegisterClassW`, `RegisterWindowMessageW`, `ReleaseCapture`, `ReleaseDC`, `RemoveMenu`, `ScreenToClient`, `SendDlgItemMessageW`, `SendInput`, `SendMessageTimeoutW`, `SendMessageW`, `SetActiveWindow`, `SetCapture`, `SetCursor`, `SetFocus`, `SetForegroundWindow`, `SetLayeredWindowAttributes`, `SetParent`, `SetRect`, `SetRectEmpty`, `SetTimer`, `SetWindowContextHelpId`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPlacement`, `SetWindowPos`, `SetWindowTextW`, `SetWindowsHookExW`, `ShowWindow`, `SystemParametersInfoW`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnhookWindowsHookEx`, `UnregisterClassA`, `UpdateLayeredWindow`, `UpdateWindow`, `WindowFromPoint`
- `UxTheme.dll` (1 names): `IsCompositionActive`
- `VERSION.dll` (3 names): `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerQueryValueW`
- `WindowsCodecs.dll` (1 names): `WICConvertBitmapSource`
- `XmlLite.dll` (2 names): `CreateXmlReader`, `CreateXmlWriter`
- `iertutil.dll` (2 names): `(ordinal-only import; name unavailable)`, `CreateUri`
- `msvcrt.dll` (63 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??8type_info@@QEBAHAEBV0@@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__RTDynamicCast`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_errno`, `_get_doserrno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcstoui64`, `_wfopen_s`, `_wtmpnam_s`, `_wtol`, `calloc`, `difftime`, `fclose`, `feof`, `fflush`, `fputws`, `fread`, `free`, `fseek`, `ftell`, `fwrite`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `strncpy_s`, `swprintf_s`, `time`, `vswprintf_s`, `wcscat_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcsncpy_s`, `wcsstr`
- `ole32.dll` (18 names): `CLSIDFromProgID`, `CLSIDFromString`, `CoCreateGuid`, `CoCreateInstance`, `CoGetClassObject`, `CoInitializeEx`, `CoSetProxyBlanket`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`, `CreateStreamOnHGlobal`, `IIDFromString`, `OleInitialize`, `OleLockRunning`, `OleUninitialize`, `StringFromCLSID`, `StringFromGUID2`
- `urlmon.dll` (1 names): `(ordinal-only import; name unavailable)`
- `wer.dll` (5 names): `WerReportAddFile`, `WerReportCloseHandle`, `WerReportCreate`, `WerReportSetParameter`, `WerReportSubmit`
- Exports: `DllCanUnloadNow`, `DllRegisterServer`, `DllUnregisterServer`, `ShowChooser`, `ShowTools`

## `bin/F12Resources.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180001130`; CLR metadata: **False**.

- `KERNEL32.dll` (6 names): `DisableThreadLibraryCalls`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `GetTickCount`, `QueryPerformanceCounter`
- Exports: none recovered.

## `bin/F12Tools.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180043610`; CLR metadata: **False**.

- `ADVAPI32.dll` (29 names): `AddAce`, `CopySid`, `GetAclInformation`, `GetLengthSid`, `GetSecurityDescriptorControl`, `GetSecurityDescriptorDacl`, `GetSecurityDescriptorGroup`, `GetSecurityDescriptorLength`, `GetSecurityDescriptorOwner`, `GetSecurityDescriptorSacl`, `GetSidLengthRequired`, `GetSidSubAuthority`, `GetTokenInformation`, `InitializeAcl`, `InitializeSecurityDescriptor`, `InitializeSid`, `IsValidSid`, `MakeAbsoluteSD`, `MakeSelfRelativeSD`, `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `SetSecurityDescriptorDacl`
- `COMCTL32.dll` (2 names): `(ordinal-only import; name unavailable)`, `InitCommonControlsEx`
- `KERNEL32.dll` (67 names): `ActivateActCtx`, `CloseHandle`, `CompareStringOrdinal`, `CreateActCtxW`, `CreateEventW`, `CreatePipe`, `CreateProcessW`, `CreateThread`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `EncodePointer`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindResourceExW`, `FlushInstructionCache`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetSystemWindowsDirectoryW`, `GetThreadLocale`, `GetTickCount`, `GetTickCount64`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsWow64Process`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LocalAlloc`, `LocalFree`, `LockResource`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ResetEvent`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetThreadLocale`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WaitForSingleObject`, `lstrcmpiW`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `SHELL32.dll` (1 names): `SHGetSpecialFolderPathW`
- `SHLWAPI.dll` (4 names): `(ordinal-only import; name unavailable)`, `PathFileExistsW`, `PathGetCharTypeW`, `PathRemoveFileSpecW`
- `USER32.dll` (38 names): `AllowSetForegroundWindow`, `AttachThreadInput`, `CallWindowProcW`, `CharNextW`, `CreateWindowExW`, `DefWindowProcW`, `DestroyAcceleratorTable`, `DestroyWindow`, `DispatchMessageW`, `GetAsyncKeyState`, `GetClassInfoExW`, `GetClientRect`, `GetForegroundWindow`, `GetSystemMetrics`, `GetWindowLongPtrW`, `GetWindowThreadProcessId`, `InSendMessage`, `InSendMessageEx`, `IsIconic`, `IsWindow`, `LoadAcceleratorsW`, `LoadCursorW`, `MapWindowPoints`, `MsgWaitForMultipleObjects`, `PeekMessageW`, `PostMessageW`, `RegisterClassExW`, `RegisterWindowMessageW`, `ReplyMessage`, `SendMessageW`, `SetFocus`, `SetForegroundWindow`, `SetParent`, `SetWindowLongPtrW`, `SetWindowPos`, `TranslateAcceleratorW`, `TranslateMessage`, `UnregisterClassA`
- `msvcrt.dll` (46 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??8type_info@@QEBAHAEBV0@@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcslwr_s`, `calloc`, `free`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `vswprintf_s`, `wcscat_s`, `wcschr`, `wcscpy_s`, `wcsncmp`, `wcsncpy_s`, `wcsrchr`, `wcsstr`
- `ole32.dll` (10 names): `CoCreateInstance`, `CoGetInterfaceAndReleaseStream`, `CoInitializeEx`, `CoMarshalInterThreadInterfaceInStream`, `CoRegisterMessageFilter`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`, `StringFromGUID2`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllInstall`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/IEShims.dll`

Architecture: `i386:x86-64`; entry: `0x00000001800010e0`; CLR metadata: **False**.

- `KERNEL32.dll` (90 names): `CloseHandle`, `CopyFileExW`, `CreateDirectoryW`, `CreateFileMappingW`, `CreateFileW`, `CreateMutexW`, `DecodePointer`, `DelayLoadFailureHook`, `DeleteCriticalSection`, `DeleteProcThreadAttributeList`, `DeviceIoControl`, `DuplicateHandle`, `EncodePointer`, `EnterCriticalSection`, `ExitThread`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileW`, `FindNextFileW`, `FreeLibrary`, `GetCurrentDirectoryW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableW`, `GetFileAttributesW`, `GetFileInformationByHandle`, `GetFileSizeEx`, `GetFullPathNameW`, `GetLastError`, `GetLogicalDriveStringsW`, `GetLongPathNameW`, `GetModuleFileNameW`, `GetModuleHandleA`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetProcessId`, `GetProcessIdOfThread`, `GetSystemDirectoryW`, `GetSystemTimeAsFileTime`, `GetThreadId`, `GetTickCount`, `GetWindowsDirectoryW`, `HeapAlloc`, `HeapFree`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `InitializeProcThreadAttributeList`, `IsWow64Process`, `LeaveCriticalSection`, `LoadLibraryA`, `LoadLibraryExA`, `LoadLibraryW`, `LocalAlloc`, `LocalFree`, `MapViewOfFile`, `MultiByteToWideChar`, `OpenEventW`, `OpenFileMappingW`, `OpenProcess`, `OutputDebugStringA`, `OutputDebugStringW`, `QueryDosDeviceW`, `QueryFullProcessImageNameW`, `QueryPerformanceCounter`, `ReleaseMutex`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SearchPathW`, `SetEnvironmentVariableW`, `SetFileAttributesW`, `SetLastError`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `UnmapViewOfFile`, `VirtualProtect`, `VirtualQuery`, `WaitForSingleObject`, `WaitForSingleObjectEx`, `WideCharToMultiByte`, `lstrcmpiW`
- `api-ms-win-downlevel-advapi32-l1-1-0.dll` (9 names): `RegCloseKey`, `RegCreateKeyExW`, `RegEnumKeyExW`, `RegEnumValueW`, `RegGetValueW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll` (11 names): `PathFindFileNameW`, `PathGetArgsW`, `PathIsUNCW`, `PathSkipRootW`, `StrCmpCW`, `StrCmpICA`, `StrCmpICW`, `StrCmpIW`, `StrCmpNCW`, `StrCmpNICW`, `StrDupW`
- `iertutil.dll` (1 names): `(ordinal-only import; name unavailable)`
- `msvcrt.dll` (41 names): `??1type_info@@UEAA@XZ`, `?terminate@@YAXXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_initterm`, `_lock`, `_onexit`, `_stricmp`, `_unlock`, `_vscwprintf`, `_vsnwprintf`, `_wcsicmp`, `_wcslwr`, `_wcsnicmp`, `_wfopen`, `calloc`, `fclose`, `fputws`, `free`, `iswctype`, `iswspace`, `malloc`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `towlower`, `wcschr`, `wcscmp`, `wcsncmp`, `wcspbrk`, `wcsrchr`, `wcsspn`, `wcsstr`, `wcstok_s`
- `ntdll.dll` (2 names): `NtQueryObject`, `RtlNtStatusToDosError`
- Exports: `AcRedirNotify`, `AcRedirNotifySetEnabled`, `AcRedirSetEnabled`, `IEShims_AdminCheckAndLaunch`, `IEShims_CreateWindowEx`, `IEShims_GetOriginatingThreadId`, `IEShims_InDllMainContext`, `IEShims_Initialize`, `IEShims_SetRedirectRegistryForThread`, `IEShims_Uninitialize`

## `bin/JSProfilerCore.dll`

Architecture: `i386:x86-64`; entry: `0x000000018000b70c`; CLR metadata: **False**.

- `ADVAPI32.dll` (7 names): `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`
- `KERNEL32.dll` (41 names): `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `FindResourceExW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTempPathW`, `GetTickCount`, `GetVersionExW`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadResource`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `lstrcmpiW`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `USER32.dll` (2 names): `CharNextW`, `UnregisterClassA`
- `WINMM.dll` (2 names): `timeBeginPeriod`, `timeEndPeriod`
- `iertutil.dll` (1 names): `CreateUri`
- `msvcrt.dll` (36 names): `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??_V@YAXPEAX@Z`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_aligned_free`, `_aligned_malloc`, `_amsg_exit`, `_callnewh`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_wfopen_s`, `calloc`, `fclose`, `fread`, `free`, `fwrite`, `malloc`, `memcpy`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `wcsncmp`, `wcsncpy_s`
- `ole32.dll` (4 names): `CoCreateInstance`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`

## `bin/MemoryAnalyzer.dll`

Architecture: `i386:x86-64`; entry: `0x00000001801b2700`; CLR metadata: **False**.

- `KERNEL32.dll` (57 names): `CloseHandle`, `CloseThreadpool`, `CloseThreadpoolCleanupGroup`, `CloseThreadpoolCleanupGroupMembers`, `CreateFileW`, `CreateThreadpool`, `CreateThreadpoolCleanupGroup`, `DecodePointer`, `DeleteCriticalSection`, `EncodePointer`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindResourceExW`, `FlushInstructionCache`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionEx`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadResource`, `LockResource`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReadFile`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetLastError`, `SetThreadpoolThreadMaximum`, `SetThreadpoolThreadMinimum`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TrySubmitThreadpoolCallback`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WideCharToMultiByte`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `USER32.dll` (11 names): `CallWindowProcW`, `CreateWindowExW`, `DefWindowProcW`, `DestroyWindow`, `GetClassInfoExW`, `GetWindowLongPtrW`, `LoadCursorW`, `PostMessageW`, `RegisterClassExW`, `SetWindowLongPtrW`, `UnregisterClassA`
- `msvcrt.dll` (47 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__RTDynamicCast`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_errno`, `_initterm`, `_lock`, `_mbschr`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcstoi64`, `_wcstoui64`, `clock`, `free`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `tolower`, `toupper`, `vswprintf_s`, `wcscat_s`, `wcscmp`, `wcscpy_s`, `wcsncpy_s`, `wcsstr`, `wcstod`
- `ole32.dll` (1 names): `CoCreateInstance`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`

## `bin/Timeline.dll`

Architecture: `i386:x86-64`; entry: `0x00000001800299e0`; CLR metadata: **False**.

- `KERNEL32.dll` (33 names): `DeleteCriticalSection`, `EnterCriticalSection`, `FindResourceExW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionEx`, `LeaveCriticalSection`, `LoadResource`, `LockResource`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `SHLWAPI.dll` (2 names): `PathFileExistsW`, `PathGetCharTypeW`
- `USER32.dll` (1 names): `UnregisterClassA`
- `msvcrt.dll` (47 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??_V@YAXPEAX@Z`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_ui64tow_s`, `_ultow_s`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcstoi64`, `_wtoi`, `floor`, `free`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `toupper`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcsncmp`, `wcsncpy_s`, `wcsnlen`, `wcsstr`, `wcstol`
- `ole32.dll` (1 names): `CoCreateInstance`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`

## `bin/Timeline_is.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180021450`; CLR metadata: **False**.

- `KERNEL32.dll` (30 names): `DeleteCriticalSection`, `EnterCriticalSection`, `FindResourceExW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetFileAttributesW`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadResource`, `LockResource`, `MultiByteToWideChar`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `RPCRT4.dll` (1 names): `UuidFromStringW`
- `SHLWAPI.dll` (1 names): `SHCreateStreamOnFileEx`
- `USER32.dll` (1 names): `UnregisterClassA`
- `XmlLite.dll` (1 names): `CreateXmlReader`
- `msvcrt.dll` (36 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_resetstkoflw`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wtoi`, `free`, `malloc`, `memcpy`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `toupper`, `vswprintf_s`, `wcscmp`, `wcsncpy_s`, `wcsstr`, `wcstoul`
- `ole32.dll` (1 names): `CoCreateInstance`
- `tdh.dll` (2 names): `TdhGetProperty`, `TdhGetPropertySize`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/en-US/DiagnosticsTap.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/en-US/F12.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/en-US/F12Resources.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/en-US/F12Tools.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/en-US/iedvtool.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/en-US/ieinstal.exe.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/en-US/iexplore.exe.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/en-US/jsdbgui.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/en-US/jsprofilerui.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/en-US/networkinspection.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/iediagcmd.exe`

Architecture: `i386`; entry: `0x0043f81e`; CLR metadata: **True**.

- `mscoree.dll` (1 names): `_CorExeMain`
- Exports: none recovered.

## `bin/iedvtool.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180099490`; CLR metadata: **False**.

- `ADVAPI32.dll` (10 names): `EventRegister`, `EventUnregister`, `EventWrite`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`
- `GDI32.dll` (36 names): `BitBlt`, `CreateBitmap`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateFontIndirectW`, `CreateFontW`, `CreatePatternBrush`, `CreatePen`, `CreateRectRgn`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `GetBkColor`, `GetCurrentObject`, `GetDeviceCaps`, `GetObjectW`, `GetPixel`, `GetStockObject`, `GetTextColor`, `GetTextExtentPoint32W`, `GetTextExtentPointW`, `LineTo`, `MoveToEx`, `PatBlt`, `Rectangle`, `SelectClipRgn`, `SelectObject`, `SetBkColor`, `SetBkMode`, `SetGraphicsMode`, `SetLayout`, `SetTextAlign`, `SetTextColor`, `SetWorldTransform`, `StretchBlt`, `TextOutW`
- `IEFRAME.dll` (7 names): `(ordinal-only import; name unavailable)`, `IEAssociateThreadWithTab`, `IECancelSaveFile`, `IEGetWriteableFolderPath`, `IEIsProtectedModeProcess`, `IESaveFile`, `IEShowSaveFileDialog`
- `KERNEL32.dll` (95 names): `ActivateActCtx`, `CloseHandle`, `CreateActCtxW`, `CreateDirectoryW`, `CreateEventW`, `CreateFileW`, `CreateThread`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `DeleteFileW`, `EncodePointer`, `EnterCriticalSection`, `EnumUILanguagesW`, `ExpandEnvironmentStringsW`, `FileTimeToLocalFileTime`, `FileTimeToSystemTime`, `FindResourceExW`, `FindResourceW`, `FlushInstructionCache`, `FormatMessageW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetDateFormatA`, `GetFileAttributesW`, `GetLastError`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTickCount`, `GetTickCount64`, `GetTimeFormatA`, `GetUserDefaultUILanguage`, `GlobalAddAtomW`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapCreate`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsDebuggerPresent`, `K32GetModuleBaseNameW`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadLibraryW`, `LoadResource`, `LocalAlloc`, `LocalFree`, `LockResource`, `MulDiv`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReleaseActCtx`, `ResetEvent`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `VirtualProtect`, `VirtualQuery`, `WaitForSingleObject`, `WideCharToMultiByte`, `WriteFile`, `lstrcmpA`, `lstrcmpW`, `lstrcmpiA`, `lstrcmpiW`
- `MSHTML.dll` (1 names): `(ordinal-only import; name unavailable)`
- `MSIMG32.dll` (2 names): `GradientFill`, `TransparentBlt`
- `OLEACC.dll` (2 names): `CreateStdAccessibleObject`, `LresultFromObject`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `SHELL32.dll` (3 names): `(ordinal-only import; name unavailable)`, `SHGetFolderPathW`, `SHGetKnownFolderPath`
- `SHLWAPI.dll` (16 names): `(ordinal-only import; name unavailable)`, `PathFindExtensionW`, `PathFindFileNameW`, `PathRemoveFileSpecW`, `PathUndecorateW`, `SHCreateStreamOnFileW`, `SHDeleteKeyW`, `StrChrA`, `StrChrW`, `StrCmpIW`, `StrCmpW`, `StrRChrW`, `StrStrIW`, `StrStrW`, `StrToIntW`, `UrlCanonicalizeW`
- `USER32.dll` (140 names): `AllowSetForegroundWindow`, `AppendMenuW`, `AttachThreadInput`, `BeginPaint`, `CallNextHookEx`, `CallWindowProcW`, `CharNextW`, `CheckDlgButton`, `CheckMenuItem`, `CheckMenuRadioItem`, `ClientToScreen`, `CloseClipboard`, `CloseWindow`, `CopyRect`, `CreateDialogParamW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DeleteMenu`, `DestroyAcceleratorTable`, `DestroyCursor`, `DestroyIcon`, `DestroyMenu`, `DestroyWindow`, `DialogBoxParamW`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawTextW`, `EmptyClipboard`, `EnableMenuItem`, `EnableWindow`, `EndDialog`, `EndPaint`, `EqualRect`, `FillRect`, `FindWindowExW`, `FrameRect`, `GetActiveWindow`, `GetCapture`, `GetClassInfoExW`, `GetClassLongPtrW`, `GetClassNameW`, `GetClientRect`, `GetComboBoxInfo`, `GetDC`, `GetDesktopWindow`, `GetDlgItem`, `GetDlgItemInt`, `GetDlgItemTextW`, `GetFocus`, `GetKeyState`, `GetMenuState`, `GetMessagePos`, `GetParent`, `GetPropW`, `GetSubMenu`, `GetSysColor`, `GetSysColorBrush`, `GetSystemMetrics`, `GetUpdateRect`, `GetWindow`, `GetWindowInfo`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowPlacement`, `GetWindowRect`, `GetWindowTextW`, `GetWindowThreadProcessId`, `InSendMessageEx`, `InflateRect`, `IntersectRect`, `InvalidateRect`, `IsChild`, `IsDlgButtonChecked`, `IsIconic`, `IsRectEmpty`, `IsWindow`, `IsWindowEnabled`, `IsWindowVisible`, `KillTimer`, `LoadAcceleratorsW`, `LoadCursorW`, `LoadIconW`, `LoadImageW`, `LoadMenuW`, `LoadStringW`, `MapWindowPoints`, `MessageBoxW`, `MoveWindow`, `MsgWaitForMultipleObjects`, `NotifyWinEvent`, `OffsetRect`, `OpenClipboard`, `PeekMessageW`, `PostMessageW`, `PostThreadMessageW`, `PtInRect`, `RedrawWindow`, `RegisterClassExW`, `ReleaseCapture`, `ReleaseDC`, `RemovePropW`, `ReplyMessage`, `ScreenToClient`, `SendMessageTimeoutW`, `SendMessageW`, `SetCapture`, `SetClassLongPtrW`, `SetClassLongW`, `SetClipboardData`, `SetCursor`, `SetDlgItemTextW`, `SetFocus`, `SetForegroundWindow`, `SetLayeredWindowAttributes`, `SetMenuItemInfoW`, `SetParent`, `SetPropW`, `SetRect`, `SetRectEmpty`, `SetTimer`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPlacement`, `SetWindowPos`, `SetWindowTextW`, `SetWindowsHookExW`, `ShowCaret`, `ShowWindow`, `SystemParametersInfoW`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnhookWindowsHookEx`, `UnionRect`, `UnregisterClassA`, `UpdateWindow`, `ValidateRect`, `WindowFromPoint`
- `UxTheme.dll` (1 names): `IsThemeActive`
- `WININET.dll` (14 names): `DeleteUrlCacheEntryW`, `FindFirstUrlCacheEntryW`, `FindNextUrlCacheEntryW`, `GetUrlCacheEntryInfoW`, `HttpOpenRequestW`, `InternetCanonicalizeUrlW`, `InternetCrackUrlW`, `InternetGetCookieW`, `InternetSetOptionW`, `PrivacyGetZonePreferenceW`, `PrivacySetZonePreferenceW`, `ReadUrlCacheEntryStream`, `RetrieveUrlCacheEntryStreamW`, `UnlockUrlCacheEntryStream`
- `iertutil.dll` (1 names): `(ordinal-only import; name unavailable)`
- `msvcrt.dll` (55 names): `??1type_info@@UEAA@XZ`, `?terminate@@YAXXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_errno`, `_initterm`, `_itow_s`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_vsnwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcsnicmp`, `_wfopen_s`, `atan2`, `calloc`, `cos`, `fclose`, `floor`, `fputs`, `fputws`, `free`, `iswalpha`, `iswascii`, `iswdigit`, `iswspace`, `malloc`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `sin`, `sprintf_s`, `sqrt`, `strchr`, `strtoul`, `swprintf_s`, `toupper`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcscspn`, `wcsncmp`, `wcsncpy_s`, `wcsrchr`, `wcsspn`, `wcsstr`, `wcstol`
- `ole32.dll` (12 names): `CoCreateInstance`, `CoGetInterfaceAndReleaseStream`, `CoInitializeEx`, `CoMarshalInterThreadInterfaceInStream`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `StringFromGUID2`
- `urlmon.dll` (7 names): `(ordinal-only import; name unavailable)`, `CoInternetCombineIUri`, `CoInternetCreateZoneManager`, `CoInternetIsFeatureEnabled`, `CreateUri`, `GetMarkOfTheWeb`, `UrlMkSetSessionOption`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/ieinstal.exe`

Architecture: `i386:x86-64`; entry: `0x000000014000fa70`; CLR metadata: **False**.

- `ADVAPI32.dll` (40 names): `AddMandatoryAce`, `AllocateAndInitializeSid`, `CheckTokenMembership`, `ConvertStringSidToSidW`, `CopySid`, `CreateWellKnownSid`, `EqualSid`, `FreeSid`, `GetAce`, `GetKernelObjectSecurity`, `GetLengthSid`, `GetSecurityDescriptorSacl`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`, `GetTokenInformation`, `InitializeAcl`, `InitializeSecurityDescriptor`, `IsValidSid`, `OpenProcessToken`, `OpenThreadToken`, `RegCloseKey`, `RegCreateKeyA`, `RegCreateKeyExW`, `RegCreateKeyW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegEnumValueW`, `RegGetValueW`, `RegOpenCurrentUser`, `RegOpenKeyExA`, `RegOpenKeyExW`, `RegOverridePredefKey`, `RegQueryValueExA`, `RegQueryValueExW`, `RegSetValueExA`, `RegSetValueExW`, `SetEntriesInAclW`, `SetKernelObjectSecurity`, `SetSecurityDescriptorDacl`, `SetSecurityDescriptorSacl`
- `AUTHZ.dll` (5 names): `AuthzAccessCheck`, `AuthzFreeContext`, `AuthzFreeResourceManager`, `AuthzInitializeContextFromSid`, `AuthzInitializeResourceManager`
- `KERNEL32.dll` (76 names): `ActivateActCtx`, `CloseHandle`, `CopyFileW`, `CreateActCtxW`, `CreateDirectoryExA`, `CreateEventW`, `CreateFileA`, `CreateFileW`, `CreateProcessW`, `CreateThread`, `DeactivateActCtx`, `DeleteCriticalSection`, `DeleteFileA`, `DeleteFileW`, `DuplicateHandle`, `EnterCriticalSection`, `FindClose`, `FindFirstFileA`, `FindNextFileA`, `FlushInstructionCache`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThread`, `GetCurrentThreadId`, `GetExitCodeThread`, `GetFileAttributesA`, `GetFileAttributesW`, `GetFinalPathNameByHandleW`, `GetFullPathNameW`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetSystemTimeAsFileTime`, `GetTempPathA`, `GetThreadContext`, `GetTickCount`, `GetVersionExA`, `HeapAlloc`, `HeapFree`, `HeapSetInformation`, `InitializeCriticalSection`, `K32GetModuleBaseNameW`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadLibraryW`, `LocalAlloc`, `LocalFree`, `MultiByteToWideChar`, `OpenProcess`, `QueryPerformanceCounter`, `ReleaseActCtx`, `RemoveDirectoryA`, `ResumeThread`, `SetEvent`, `SetFileAttributesA`, `SetLastError`, `SetProcessShutdownParameters`, `SetThreadContext`, `SetUnhandledExceptionFilter`, `Sleep`, `SuspendThread`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `VirtualProtect`, `VirtualQuery`, `WaitForSingleObject`, `WideCharToMultiByte`, `lstrcmpA`, `lstrcmpiA`, `lstrcmpiW`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `RPCRT4.dll` (3 names): `RpcStringFreeW`, `UuidCreate`, `UuidToStringW`
- `USER32.dll` (3 names): `CharNextW`, `LoadStringW`, `PostQuitMessage`
- `WINTRUST.dll` (4 names): `CryptCATAdminAcquireContext`, `CryptCATAdminAddCatalog`, `CryptCATAdminReleaseCatalogContext`, `CryptCATAdminReleaseContext`
- `iertutil.dll` (1 names): `(ordinal-only import; name unavailable)`
- `msvcrt.dll` (32 names): `?terminate@@YAXXZ`, `_XcptFilter`, `__C_specific_handler`, `__dllonexit`, `__set_app_type`, `__setusermatherr`, `__wgetmainargs`, `_amsg_exit`, `_cexit`, `_commode`, `_exit`, `_fmode`, `_initterm`, `_lock`, `_onexit`, `_unlock`, `_vsnprintf`, `_vsnwprintf`, `_wcmdln`, `_wcsnicmp`, `_wtoi`, `exit`, `iscntrl`, `iswalpha`, `iswascii`, `iswcntrl`, `memcpy_s`, `memset`, `rand_s`, `wcschr`, `wcsrchr`, `wcstok`
- `ntdll.dll` (4 names): `NtFreeVirtualMemory`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`
- `ole32.dll` (14 names): `CLSIDFromString`, `CoCreateInstance`, `CoGetCallContext`, `CoImpersonateClient`, `CoInitialize`, `CoInitializeEx`, `CoInitializeSecurity`, `CoRegisterClassObject`, `CoRevertToSelf`, `CoRevokeClassObject`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoUninitialize`, `StringFromGUID2`
- `urlmon.dll` (5 names): `(ordinal-only import; name unavailable)`, `CoInternetCreateSecurityManager`, `CoInternetSetFeatureEnabled`, `CompatFlagsFromClsid`, `Extract`
- Exports: none recovered.

## `bin/ielowutil.exe`

Architecture: `i386:x86-64`; entry: `0x0000000140002940`; CLR metadata: **False**.

- `KERNEL32.dll` (39 names): `ActivateActCtx`, `CloseHandle`, `CreateActCtxW`, `CreateEventW`, `CreateThread`, `DeactivateActCtx`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVersionExA`, `HeapAlloc`, `HeapFree`, `HeapSetInformation`, `IsWow64Process`, `LoadLibraryExW`, `MapViewOfFile`, `OpenEventW`, `OpenFileMappingW`, `QueryPerformanceCounter`, `ReleaseActCtx`, `ResetEvent`, `SetEvent`, `SetLastError`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `UnmapViewOfFile`, `VirtualAlloc`, `WaitForSingleObject`
- `USER32.dll` (5 names): `DispatchMessageW`, `MsgWaitForMultipleObjects`, `PeekMessageW`, `PostQuitMessage`, `TranslateMessage`
- `WININET.dll` (2 names): `InternetGetCookieExW`, `InternetSetCookieExW`
- `iertutil.dll` (1 names): `(ordinal-only import; name unavailable)`
- `msvcrt.dll` (20 names): `?terminate@@YAXXZ`, `_XcptFilter`, `__C_specific_handler`, `__set_app_type`, `__setusermatherr`, `__wgetmainargs`, `_amsg_exit`, `_cexit`, `_commode`, `_exit`, `_fmode`, `_initterm`, `_vsnwprintf`, `_wcmdln`, `_wcsnicmp`, `_wtoi`, `exit`, `memset`, `rand_s`, `wcstok`
- `ntdll.dll` (3 names): `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`
- `ole32.dll` (7 names): `CLSIDFromString`, `CoCreateInstance`, `CoInitializeEx`, `CoInitializeSecurity`, `CoRegisterClassObject`, `CoRevokeClassObject`, `CoUninitialize`
- Exports: none recovered.

## `bin/ieproxy.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180001ce0`; CLR metadata: **False**.

- `KERNEL32.dll` (39 names): `CloseHandle`, `CompareStringOrdinal`, `CompareStringW`, `CreateFileW`, `DelayLoadFailureHook`, `DisableThreadLibraryCalls`, `FreeLibrary`, `GetCurrentDirectoryW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetFinalPathNameByHandleW`, `GetLastError`, `GetLocaleInfoEx`, `GetModuleHandleW`, `GetProcAddress`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVersionExA`, `GlobalAlloc`, `GlobalLock`, `GlobalSize`, `GlobalUnlock`, `LoadLibraryExA`, `LoadLibraryExW`, `LocalAlloc`, `LocalFree`, `QueryPerformanceCounter`, `RegCloseKey`, `RegGetValueW`, `RegOpenKeyExW`, `RegQueryValueExW`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `RPCRT4.dll` (25 names): `CStdStubBuffer_AddRef`, `CStdStubBuffer_Connect`, `CStdStubBuffer_CountRefs`, `CStdStubBuffer_DebugServerQueryInterface`, `CStdStubBuffer_DebugServerRelease`, `CStdStubBuffer_Disconnect`, `CStdStubBuffer_Invoke`, `CStdStubBuffer_IsIIDSupported`, `CStdStubBuffer_QueryInterface`, `IUnknown_AddRef_Proxy`, `IUnknown_QueryInterface_Proxy`, `IUnknown_Release_Proxy`, `NdrCStdStubBuffer2_Release`, `NdrCStdStubBuffer_Release`, `NdrClientCall3`, `NdrDllCanUnloadNow`, `NdrDllGetClassObject`, `NdrDllRegisterProxy`, `NdrDllUnregisterProxy`, `NdrGetUserMarshalInfo`, `NdrOleAllocate`, `NdrOleFree`, `NdrStubCall3`, `NdrStubForwardingFunction`, `RpcRaiseException`
- `api-ms-win-downlevel-advapi32-l1-1-0.dll` (6 names): `GetAce`, `GetKernelObjectSecurity`, `GetSecurityDescriptorDacl`, `GetSidIdentifierAuthority`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll` (7 names): `ParseURLW`, `PathCreateFromUrlW`, `PathIsURLW`, `QISearch`, `UrlApplySchemeW`, `UrlCanonicalizeW`, `UrlCreateFromPathW`
- `api-ms-win-downlevel-shlwapi-l2-1-0.dll` (2 names): `IUnknown_QueryService`, `IUnknown_SetSite`
- `msvcrt.dll` (18 names): `??2@YAPEAX_K@Z`, `??3@YAXPEAX@Z`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `_amsg_exit`, `_initterm`, `_purecall`, `_vsnwprintf`, `free`, `iswalpha`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memset`, `wcschr`, `wcsstr`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`, `GetProxyDllInfo`

## `bin/iexplore.exe`

Architecture: `i386:x86-64`; entry: `0x00000001400019f0`; CLR metadata: **False**.

- `KERNEL32.dll` (39 names): `CloseHandle`, `CreateProcessW`, `DeleteCriticalSection`, `ExpandEnvironmentStringsW`, `FreeLibrary`, `GetCommandLineW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetProcAddress`, `GetStartupInfoW`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVersionExA`, `HeapSetInformation`, `InitializeCriticalSection`, `IsDebuggerPresent`, `LoadLibraryExA`, `LoadLibraryExW`, `LocalAlloc`, `LocalFree`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetDllDirectoryW`, `SetErrorMode`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualProtect`, `VirtualQuery`
- `USER32.dll` (6 names): `AllowSetForegroundWindow`, `FindWindowExW`, `GetWindowThreadProcessId`, `IsWindowEnabled`, `IsWindowVisible`, `SendMessageTimeoutW`
- `api-ms-win-downlevel-advapi32-l1-1-0.dll` (8 names): `EventRegister`, `EventUnregister`, `EventWrite`, `EventWriteTransfer`, `RegCloseKey`, `RegGetValueW`, `RegOpenKeyExW`, `RegQueryValueExW`
- `api-ms-win-downlevel-shell32-l1-1-0.dll` (2 names): `CommandLineToArgvW`, `SetCurrentProcessExplicitAppUserModelID`
- `api-ms-win-downlevel-shlwapi-l1-1-0.dll` (1 names): `StrStrIW`
- `iertutil.dll` (1 names): `(ordinal-only import; name unavailable)`
- `msvcrt.dll` (20 names): `?terminate@@YAXXZ`, `_XcptFilter`, `__C_specific_handler`, `__set_app_type`, `__setusermatherr`, `__wgetmainargs`, `_amsg_exit`, `_cexit`, `_commode`, `_exit`, `_fmode`, `_initterm`, `_vsnwprintf`, `_wcmdln`, `exit`, `iswspace`, `memcpy`, `memset`, `rand_s`, `wcsncmp`
- Exports: none recovered.

## `bin/jsdbgui.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180052c30`; CLR metadata: **False**.

- `ADVAPI32.dll` (10 names): `EventRegister`, `EventUnregister`, `EventWrite`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`
- `GDI32.dll` (35 names): `AbortDoc`, `BitBlt`, `CreateBitmap`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateFontIndirectW`, `CreatePatternBrush`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `EndDoc`, `EndPage`, `ExtCreatePen`, `ExtTextOutW`, `GetDeviceCaps`, `GetFontUnicodeRanges`, `GetObjectW`, `GetTextExtentPoint32W`, `GetTextExtentPointW`, `GetTextMetricsW`, `LineTo`, `MoveToEx`, `PatBlt`, `SelectObject`, `SetBkColor`, `SetBkMode`, `SetBrushOrgEx`, `SetMapMode`, `SetStretchBltMode`, `SetTextColor`, `SetViewportOrgEx`, `StartDocW`, `StartPage`, `StretchBlt`, `TextOutW`
- `KERNEL32.dll` (63 names): `ActivateActCtx`, `CreateActCtxW`, `DeactivateActCtx`, `DeleteCriticalSection`, `EnterCriticalSection`, `EnumUILanguagesW`, `FindResourceExW`, `FlushInstructionCache`, `FormatMessageA`, `FormatMessageW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetUserDefaultUILanguage`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadLibraryW`, `LoadResource`, `LocalFree`, `LockResource`, `MulDiv`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReleaseActCtx`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TryEnterCriticalSection`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WideCharToMultiByte`, `lstrcmpW`, `lstrcmpiW`, `lstrlenW`
- `MSIMG32.dll` (1 names): `TransparentBlt`
- `OLEACC.dll` (2 names): `CreateStdAccessibleObject`, `LresultFromObject`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `SHLWAPI.dll` (6 names): `(ordinal-only import; name unavailable)`, `StrCmpLogicalW`, `StrCmpNW`, `StrStrIW`, `StrStrW`, `StrToIntW`
- `USER32.dll` (111 names): `BeginPaint`, `CallNextHookEx`, `CallWindowProcW`, `CharNextW`, `CheckMenuItem`, `ClientToScreen`, `CloseClipboard`, `CreateDialogParamW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DeleteMenu`, `DestroyAcceleratorTable`, `DestroyIcon`, `DestroyMenu`, `DestroyWindow`, `DialogBoxParamW`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawMenuBar`, `DrawTextW`, `EmptyClipboard`, `EnableMenuItem`, `EnableWindow`, `EndDialog`, `EndPaint`, `FillRect`, `GetCapture`, `GetCaretPos`, `GetClassInfoExW`, `GetClientRect`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetDlgItem`, `GetDlgItemInt`, `GetFocus`, `GetForegroundWindow`, `GetKeyState`, `GetMessagePos`, `GetMonitorInfoW`, `GetParent`, `GetScrollInfo`, `GetScrollPos`, `GetSubMenu`, `GetSysColor`, `GetSysColorBrush`, `GetSystemMetrics`, `GetWindow`, `GetWindowDC`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowRect`, `GetWindowTextLengthW`, `GetWindowTextW`, `InsertMenuW`, `IntersectRect`, `InvalidateRect`, `IsChild`, `IsDialogMessageW`, `IsDlgButtonChecked`, `IsIconic`, `IsWindow`, `IsWindowVisible`, `KillTimer`, `LoadAcceleratorsW`, `LoadCursorW`, `LoadImageW`, `LoadMenuW`, `LoadStringW`, `MapWindowPoints`, `MessageBoxW`, `MonitorFromPoint`, `MoveWindow`, `OpenClipboard`, `PostMessageW`, `PtInRect`, `RedrawWindow`, `RegisterClassExW`, `ReleaseCapture`, `ReleaseDC`, `ScreenToClient`, `SendMessageW`, `SetCapture`, `SetClipboardData`, `SetCursor`, `SetDlgItemTextW`, `SetFocus`, `SetForegroundWindow`, `SetParent`, `SetRect`, `SetRectEmpty`, `SetScrollInfo`, `SetScrollPos`, `SetTimer`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPos`, `SetWindowTextW`, `SetWindowsHookExW`, `ShowWindow`, `SystemParametersInfoW`, `TrackMouseEvent`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnhookWindowsHookEx`, `UnregisterClassA`, `UpdateWindow`, `WindowFromPoint`
- `iertutil.dll` (1 names): `(ordinal-only import; name unavailable)`
- `msvcrt.dll` (50 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscprintf`, `_vscwprintf`, `_vsnwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcsnicmp`, `calloc`, `free`, `iswalnum`, `iswalpha`, `iswdigit`, `iswgraph`, `iswspace`, `iswxdigit`, `malloc`, `memcpy`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `towupper`, `vsprintf_s`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcscspn`, `wcsncpy_s`, `wcspbrk`, `wcsrchr`, `wcsspn`, `wcsstr`
- `ole32.dll` (6 names): `CoCreateInstance`, `CoInitialize`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`
- `urlmon.dll` (2 names): `(ordinal-only import; name unavailable)`, `CreateUri`
- Exports: `CreateConsoleTab`, `CreateScriptTab`, `CreateSourceViewer`

## `bin/jsdebuggeride.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180019d70`; CLR metadata: **False**.

- `ADVAPI32.dll` (8 names): `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`
- `KERNEL32.dll` (43 names): `CloseHandle`, `CreateEventW`, `DeleteCriticalSection`, `EnterCriticalSection`, `FindResourceExW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GlobalAlloc`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InitializeCriticalSectionAndSpinCount`, `LeaveCriticalSection`, `LoadLibraryExW`, `LoadResource`, `LockResource`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TryEnterCriticalSection`, `UnhandledExceptionFilter`, `lstrcmpiW`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `SHLWAPI.dll` (1 names): `(ordinal-only import; name unavailable)`
- `USER32.dll` (6 names): `CharNextW`, `DispatchMessageW`, `MsgWaitForMultipleObjects`, `PeekMessageW`, `TranslateMessage`, `UnregisterClassA`
- `WININET.dll` (7 names): `InternetCloseHandle`, `InternetOpenUrlW`, `InternetOpenW`, `InternetReadFile`, `ReadUrlCacheEntryStream`, `RetrieveUrlCacheEntryStreamW`, `UnlockUrlCacheEntryStream`
- `msvcrt.dll` (45 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `??3@YAXPEAX@Z`, `??_V@YAXPEAX@Z`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wfopen_s`, `_wtoi`, `calloc`, `fclose`, `feof`, `fread`, `free`, `fseek`, `ftell`, `malloc`, `memcmp`, `memcpy_s`, `memmove`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `vswprintf_s`, `wcscmp`, `wcsncpy_s`, `wcsstr`
- `ole32.dll` (7 names): `CoCreateInstance`, `CoDisconnectObject`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CreateStreamOnHGlobal`, `StringFromCLSID`
- `urlmon.dll` (2 names): `CoInternetCombineIUri`, `CreateUri`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`

## `bin/jsprofilerui.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180027260`; CLR metadata: **False**.

- `ADVAPI32.dll` (7 names): `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegSetValueExW`
- `GDI32.dll` (20 names): `BitBlt`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateFontIndirectW`, `CreateFontW`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `ExtTextOutW`, `GetDeviceCaps`, `GetObjectW`, `GetTextExtentExPointW`, `GetTextExtentPoint32W`, `GetTextExtentPointW`, `SelectObject`, `SetBkColor`, `SetBkMode`, `SetLayout`, `SetTextAlign`, `SetTextColor`
- `KERNEL32.dll` (69 names): `ActivateActCtx`, `CloseHandle`, `CreateActCtxW`, `CreateDirectoryW`, `CreateEventW`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `DeleteFileW`, `EncodePointer`, `EnterCriticalSection`, `EnumUILanguagesW`, `FindResourceExW`, `FlushInstructionCache`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentVariableA`, `GetFileAttributesW`, `GetLastError`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetNumberFormatW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTickCount`, `GetUserDefaultUILanguage`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LockResource`, `MulDiv`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReleaseActCtx`, `ResetEvent`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `lstrcmpW`, `lstrcmpiW`
- `OLEACC.dll` (2 names): `CreateStdAccessibleObject`, `LresultFromObject`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `SHLWAPI.dll` (1 names): `(ordinal-only import; name unavailable)`
- `USER32.dll` (90 names): `AdjustWindowRectEx`, `AppendMenuW`, `BeginPaint`, `CallWindowProcW`, `CharNextW`, `CheckMenuItem`, `CheckMenuRadioItem`, `ClientToScreen`, `CloseClipboard`, `CopyAcceleratorTableW`, `CreateAcceleratorTableW`, `CreateDialogParamW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DeleteMenu`, `DestroyAcceleratorTable`, `DestroyMenu`, `DestroyWindow`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawTextW`, `EmptyClipboard`, `EnableMenuItem`, `EnableWindow`, `EndPaint`, `FillRect`, `GetCapture`, `GetClassInfoExW`, `GetClientRect`, `GetCursorPos`, `GetDC`, `GetDlgCtrlID`, `GetDlgItem`, `GetFocus`, `GetKeyState`, `GetMenu`, `GetMenuItemCount`, `GetMessagePos`, `GetParent`, `GetScrollPos`, `GetSysColor`, `GetSysColorBrush`, `GetSystemMetrics`, `GetWindowLongA`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowRect`, `GetWindowTextW`, `InflateRect`, `InvalidateRect`, `IsWindow`, `IsWindowEnabled`, `IsWindowVisible`, `KillTimer`, `LoadAcceleratorsW`, `LoadCursorW`, `LoadImageW`, `LoadStringW`, `MoveWindow`, `MsgWaitForMultipleObjects`, `OpenClipboard`, `PeekMessageW`, `PostMessageW`, `PtInRect`, `RegisterClassExW`, `ReleaseCapture`, `ReleaseDC`, `ScreenToClient`, `SendMessageW`, `SetCapture`, `SetClipboardData`, `SetCursor`, `SetFocus`, `SetRect`, `SetScrollInfo`, `SetScrollPos`, `SetTimer`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPos`, `SetWindowTextW`, `ShowWindow`, `SystemParametersInfoW`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnregisterClassA`, `UpdateWindow`
- `iertutil.dll` (2 names): `(ordinal-only import; name unavailable)`, `CreateUri`
- `msvcrt.dll` (44 names): `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_errno`, `_initterm`, `_lock`, `_onexit`, `_purecall`, `_ultow_s`, `_unlock`, `_vscwprintf`, `_vsnwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wfopen_s`, `atoi`, `calloc`, `fclose`, `fputs`, `fputws`, `free`, `iswspace`, `malloc`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `swprintf_s`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcsncpy_s`, `wcsstr`, `wcstol`
- `ole32.dll` (4 names): `CoCreateInstance`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`
- `urlmon.dll` (1 names): `(ordinal-only import; name unavailable)`
- Exports: `CreateProfileTab`

## `bin/msdbg2.dll`

Architecture: `i386:x86-64`; entry: `0x000000018000164c`; CLR metadata: **False**.

- `KERNEL32.dll` (64 names): `CloseHandle`, `CreateFileW`, `DecodePointer`, `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `EncodePointer`, `EnterCriticalSection`, `ExitProcess`, `FlushFileBuffers`, `FreeEnvironmentStringsW`, `GetACP`, `GetCPInfo`, `GetCommandLineA`, `GetConsoleCP`, `GetConsoleMode`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileType`, `GetLastError`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemTimeAsFileTime`, `HeapAlloc`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSectionAndSpinCount`, `IsDebuggerPresent`, `IsProcessorFeaturePresent`, `IsValidCodePage`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExW`, `MultiByteToWideChar`, `OutputDebugStringW`, `QueryPerformanceCounter`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetFilePointerEx`, `SetLastError`, `SetStdHandle`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `RPCRT4.dll` (23 names): `CStdStubBuffer_AddRef`, `CStdStubBuffer_Connect`, `CStdStubBuffer_CountRefs`, `CStdStubBuffer_DebugServerQueryInterface`, `CStdStubBuffer_DebugServerRelease`, `CStdStubBuffer_Disconnect`, `CStdStubBuffer_Invoke`, `CStdStubBuffer_IsIIDSupported`, `CStdStubBuffer_QueryInterface`, `IUnknown_AddRef_Proxy`, `IUnknown_QueryInterface_Proxy`, `IUnknown_Release_Proxy`, `NdrCStdStubBuffer2_Release`, `NdrCStdStubBuffer_Release`, `NdrClientCall2`, `NdrDllCanUnloadNow`, `NdrDllGetClassObject`, `NdrDllRegisterProxy`, `NdrDllUnregisterProxy`, `NdrOleAllocate`, `NdrOleFree`, `NdrStubCall2`, `NdrStubForwardingFunction`
- `ole32.dll` (4 names): `HWND_UserFree`, `HWND_UserMarshal`, `HWND_UserSize`, `HWND_UserUnmarshal`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/networkinspection.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180053280`; CLR metadata: **False**.

- `ADVAPI32.dll` (8 names): `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`
- `GDI32.dll` (25 names): `BitBlt`, `CreateBitmap`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateDIBSection`, `CreateFontIndirectW`, `CreateFontW`, `CreatePatternBrush`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `ExtTextOutW`, `GetDeviceCaps`, `GetObjectW`, `GetStockObject`, `GetTextExtentExPointW`, `GetTextExtentPoint32W`, `GetTextMetricsW`, `PatBlt`, `SelectObject`, `SetBkColor`, `SetBkMode`, `SetLayout`, `SetTextColor`, `SetViewportOrgEx`
- `KERNEL32.dll` (89 names): `ActivateActCtx`, `CloseHandle`, `CompareFileTime`, `CompareStringW`, `CreateActCtxW`, `CreateDirectoryW`, `CreateEventW`, `CreateMutexW`, `CreateThread`, `DeactivateActCtx`, `DecodePointer`, `DeleteCriticalSection`, `DeleteFileW`, `EncodePointer`, `EnterCriticalSection`, `EnumUILanguagesW`, `FileTimeToLocalFileTime`, `FileTimeToSystemTime`, `FindResourceExW`, `FlushInstructionCache`, `FormatMessageW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetDateFormatW`, `GetDurationFormatEx`, `GetFileAttributesW`, `GetLastError`, `GetLocaleInfoW`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetNumberFormatW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTempFileNameW`, `GetTickCount`, `GetTickCount64`, `GetTimeFormatW`, `GetTimeZoneInformation`, `GetUserDefaultUILanguage`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadLibraryW`, `LoadResource`, `LocalFree`, `LockResource`, `MulDiv`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `ReleaseActCtx`, `ReleaseMutex`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `SetEvent`, `SetLastError`, `SetThreadPriority`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `SystemTimeToFileTime`, `TerminateProcess`, `TzSpecificLocalTimeToSystemTime`, `UnhandledExceptionFilter`, `VirtualAlloc`, `VirtualFree`, `WaitForMultipleObjects`, `WaitForSingleObject`, `WideCharToMultiByte`, `lstrcmpW`, `lstrcmpiW`, `lstrlenW`
- `MSIMG32.dll` (1 names): `AlphaBlend`
- `OLEACC.dll` (2 names): `CreateStdAccessibleObject`, `LresultFromObject`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `SHELL32.dll` (1 names): `ShellExecuteW`
- `SHLWAPI.dll` (4 names): `(ordinal-only import; name unavailable)`, `PathFindExtensionW`, `PathIsFileSpecW`, `SHCreateStreamOnFileW`
- `USER32.dll` (97 names): `AppendMenuW`, `BeginPaint`, `CallWindowProcW`, `CharNextW`, `CharUpperW`, `CheckMenuItem`, `CheckMenuRadioItem`, `ClientToScreen`, `CloseClipboard`, `CopyAcceleratorTableW`, `CreateAcceleratorTableW`, `CreateDialogParamW`, `CreatePopupMenu`, `CreateWindowExW`, `DefWindowProcW`, `DestroyAcceleratorTable`, `DestroyMenu`, `DestroyWindow`, `DispatchMessageW`, `DrawEdge`, `DrawFocusRect`, `DrawTextW`, `EmptyClipboard`, `EnableMenuItem`, `EnableWindow`, `EndPaint`, `FillRect`, `GetCapture`, `GetClassInfoExW`, `GetClassNameW`, `GetClientRect`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetDlgCtrlID`, `GetDlgItem`, `GetFocus`, `GetKeyState`, `GetMessagePos`, `GetMonitorInfoW`, `GetParent`, `GetScrollInfo`, `GetSysColor`, `GetSysColorBrush`, `GetSystemMetrics`, `GetWindow`, `GetWindowDC`, `GetWindowLongPtrW`, `GetWindowLongW`, `GetWindowRect`, `GetWindowTextLengthW`, `GetWindowTextW`, `InvalidateRect`, `IsChild`, `IsWindow`, `IsWindowEnabled`, `IsWindowVisible`, `LoadAcceleratorsW`, `LoadBitmapW`, `LoadCursorW`, `LoadImageW`, `LoadStringW`, `MapWindowPoints`, `MessageBoxW`, `MonitorFromPoint`, `MoveWindow`, `OffsetRect`, `OpenClipboard`, `PeekMessageW`, `PostMessageW`, `PtInRect`, `RegisterClassExW`, `ReleaseCapture`, `ReleaseDC`, `ScreenToClient`, `ScrollWindowEx`, `SendMessageW`, `SetCapture`, `SetClipboardData`, `SetCursor`, `SetFocus`, `SetParent`, `SetRectEmpty`, `SetScrollInfo`, `SetScrollPos`, `SetWindowLongPtrW`, `SetWindowLongW`, `SetWindowPos`, `SetWindowTextW`, `ShowWindow`, `SystemParametersInfoW`, `TrackPopupMenuEx`, `TranslateAcceleratorW`, `TranslateMessage`, `UnregisterClassA`, `UpdateWindow`, `WindowFromPoint`
- `VERSION.dll` (3 names): `GetFileVersionInfoExW`, `GetFileVersionInfoSizeExW`, `VerQueryValueW`
- `WININET.dll` (9 names): `DeleteUrlCacheEntryW`, `FindFirstUrlCacheEntryW`, `FindNextUrlCacheEntryW`, `GetUrlCacheEntryInfoExW`, `InternetSetOptionW`, `InternetTimeToSystemTimeW`, `ReadUrlCacheEntryStream`, `RetrieveUrlCacheEntryStreamW`, `UnlockUrlCacheEntryStream`
- `WindowsCodecs.dll` (1 names): `WICConvertBitmapSource`
- `iertutil.dll` (2 names): `(ordinal-only import; name unavailable)`, `CreateUri`
- `msvcrt.dll` (56 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_errno`, `_initterm`, `_ismbcspace`, `_lock`, `_mbschr`, `_mbscspn`, `_mbsinc`, `_mbsspn`, `_onexit`, `_purecall`, `_unlock`, `_vscwprintf`, `_wcsicmp`, `_wcslwr_s`, `_wcsnicmp`, `_wcsupr_s`, `_wfopen_s`, `_wtoi`, `calloc`, `fclose`, `fputs`, `fputws`, `free`, `fwrite`, `iswspace`, `malloc`, `memcmp`, `memcpy_s`, `memmove_s`, `memset`, `qsort_s`, `realloc`, `swprintf_s`, `towupper`, `vswprintf_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcscspn`, `wcsncpy_s`, `wcsrchr`, `wcsspn`, `wcsstr`, `wcstol`
- `ole32.dll` (5 names): `CoCreateInstance`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CreateStreamOnHGlobal`
- `urlmon.dll` (2 names): `FindMimeFromData`, `QueryAssociations`
- Exports: `CreateNetworkTab`

## `bin/pdm.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180036a54`; CLR metadata: **False**.

- `ADVAPI32.dll` (33 names): `AddAce`, `CopySid`, `EqualSid`, `GetAclInformation`, `GetLengthSid`, `GetSecurityDescriptorControl`, `GetSecurityDescriptorDacl`, `GetSecurityDescriptorGroup`, `GetSecurityDescriptorOwner`, `GetSecurityDescriptorSacl`, `GetSidIdentifierAuthority`, `GetSidLengthRequired`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`, `GetTokenInformation`, `InitializeAcl`, `InitializeSecurityDescriptor`, `InitializeSid`, `IsValidSid`, `MakeAbsoluteSD`, `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegEnumKeyW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `SetSecurityDescriptorDacl`, `SetSecurityDescriptorSacl`
- `KERNEL32.dll` (120 names): `CloseHandle`, `CreateEventW`, `CreateFileMappingW`, `CreateFileW`, `CreateMutexW`, `CreateSemaphoreW`, `CreateThread`, `DecodePointer`, `DeleteCriticalSection`, `DuplicateHandle`, `EncodePointer`, `EnterCriticalSection`, `ExitProcess`, `FindResourceExW`, `FindResourceW`, `FlushFileBuffers`, `FlushInstructionCache`, `FormatMessageA`, `FormatMessageW`, `FreeEnvironmentStringsW`, `FreeLibrary`, `FreeLibraryAndExitThread`, `GetACP`, `GetCPInfo`, `GetCommandLineA`, `GetComputerNameW`, `GetConsoleCP`, `GetConsoleMode`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThread`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileAttributesW`, `GetFileType`, `GetLastError`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleA`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetThreadLocale`, `GetTickCount`, `GetVersion`, `GetVersionExW`, `GlobalAlloc`, `GlobalFree`, `GlobalLock`, `GlobalUnlock`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSectionAndSpinCount`, `InitializeCriticalSectionEx`, `InitializeSListHead`, `InterlockedPopEntrySList`, `InterlockedPushEntrySList`, `IsDebuggerPresent`, `IsProcessorFeaturePresent`, `IsValidCodePage`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadLibraryW`, `LoadResource`, `LocalFree`, `LockResource`, `MapViewOfFile`, `MultiByteToWideChar`, `OpenEventW`, `OpenFileMappingW`, `OpenProcess`, `OutputDebugStringW`, `ProcessIdToSessionId`, `QueryPerformanceCounter`, `RaiseException`, `RegisterWaitForSingleObject`, `ReleaseMutex`, `ReleaseSemaphore`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlPcToFileHeader`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetEvent`, `SetFilePointerEx`, `SetLastError`, `SetStdHandle`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `UnmapViewOfFile`, `UnregisterWaitEx`, `VirtualAlloc`, `VirtualFree`, `VirtualProtect`, `VirtualQuery`, `WaitForMultipleObjects`, `WaitForSingleObject`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`, `lstrcmpiW`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `USER32.dll` (17 names): `CallWindowProcW`, `CharNextW`, `CreateWindowExW`, `DefWindowProcW`, `DestroyWindow`, `DispatchMessageW`, `GetClassInfoExW`, `GetWindowLongPtrW`, `IsWindow`, `LoadCursorW`, `MsgWaitForMultipleObjects`, `MsgWaitForMultipleObjectsEx`, `PeekMessageW`, `PostMessageW`, `RegisterClassExW`, `SetWindowLongPtrW`, `UnregisterClassW`
- `ole32.dll` (18 names): `CLSIDFromString`, `CoCreateInstance`, `CoGetObjectContext`, `CoInitialize`, `CoInitializeEx`, `CoMarshalInterface`, `CoQueryProxyBlanket`, `CoRegisterMessageFilter`, `CoReleaseMarshalData`, `CoSetProxyBlanket`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoUninitialize`, `CoUnmarshalInterface`, `CoWaitForMultipleHandles`, `CreateStreamOnHGlobal`, `StringFromGUID2`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/pdmproxy100.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180001210`; CLR metadata: **False**.

- `KERNEL32.dll` (64 names): `CloseHandle`, `CreateFileW`, `DecodePointer`, `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `EncodePointer`, `EnterCriticalSection`, `ExitProcess`, `FlushFileBuffers`, `FreeEnvironmentStringsW`, `GetACP`, `GetCPInfo`, `GetCommandLineA`, `GetConsoleCP`, `GetConsoleMode`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetEnvironmentStringsW`, `GetFileType`, `GetLastError`, `GetModuleFileNameA`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetModuleHandleW`, `GetOEMCP`, `GetProcAddress`, `GetProcessHeap`, `GetStartupInfoW`, `GetStdHandle`, `GetStringTypeW`, `GetSystemTimeAsFileTime`, `HeapAlloc`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSectionAndSpinCount`, `IsDebuggerPresent`, `IsProcessorFeaturePresent`, `IsValidCodePage`, `LCMapStringW`, `LeaveCriticalSection`, `LoadLibraryExW`, `MultiByteToWideChar`, `OutputDebugStringW`, `QueryPerformanceCounter`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlUnwindEx`, `RtlVirtualUnwind`, `SetFilePointerEx`, `SetLastError`, `SetStdHandle`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `TlsAlloc`, `TlsFree`, `TlsGetValue`, `TlsSetValue`, `UnhandledExceptionFilter`, `WideCharToMultiByte`, `WriteConsoleW`, `WriteFile`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `RPCRT4.dll` (22 names): `CStdStubBuffer_AddRef`, `CStdStubBuffer_Connect`, `CStdStubBuffer_CountRefs`, `CStdStubBuffer_DebugServerQueryInterface`, `CStdStubBuffer_DebugServerRelease`, `CStdStubBuffer_Disconnect`, `CStdStubBuffer_Invoke`, `CStdStubBuffer_IsIIDSupported`, `CStdStubBuffer_QueryInterface`, `IUnknown_AddRef_Proxy`, `IUnknown_QueryInterface_Proxy`, `IUnknown_Release_Proxy`, `NdrCStdStubBuffer2_Release`, `NdrCStdStubBuffer_Release`, `NdrDllCanUnloadNow`, `NdrDllGetClassObject`, `NdrDllRegisterProxy`, `NdrDllUnregisterProxy`, `NdrOleAllocate`, `NdrOleFree`, `NdrStubCall2`, `NdrStubForwardingFunction`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/perf_nt.dll`

Architecture: `i386:x86-64`; entry: `0x0000000180112bd8`; CLR metadata: **False**.

- `ADVAPI32.dll` (9 names): `CopySid`, `EventRegister`, `EventUnregister`, `EventWrite`, `GetLengthSid`, `IsValidSid`, `RegCloseKey`, `RegOpenKeyExW`, `RegQueryValueExW`
- `KERNEL32.dll` (71 names): `CloseHandle`, `CopyFileW`, `CreateDirectoryW`, `CreateEventW`, `CreateFileMappingW`, `CreateFileW`, `CreateThread`, `DebugBreak`, `DeleteCriticalSection`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindResourceExW`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetDllDirectoryW`, `GetDriveTypeW`, `GetEnvironmentVariableW`, `GetFileInformationByHandleEx`, `GetFileSize`, `GetFullPathNameW`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemInfo`, `GetSystemTimeAsFileTime`, `GetTickCount`, `GetVolumePathNameW`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeConditionVariable`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadLibraryExA`, `LoadLibraryExW`, `LoadResource`, `LocalAlloc`, `LockFileEx`, `LockResource`, `MapViewOfFileEx`, `MultiByteToWideChar`, `OutputDebugStringA`, `QueryFullProcessImageNameW`, `QueryPerformanceCounter`, `RaiseException`, `ReadFile`, `ResumeThread`, `SetDllDirectoryW`, `SetEndOfFile`, `SetEvent`, `SetFilePointer`, `SetLastError`, `SetUnhandledExceptionFilter`, `SizeofResource`, `Sleep`, `SleepConditionVariableCS`, `TerminateProcess`, `UnhandledExceptionFilter`, `UnlockFileEx`, `UnmapViewOfFile`, `WaitForSingleObjectEx`, `WakeConditionVariable`, `WideCharToMultiByte`, `WriteFile`, `lstrcmpiW`
- `SHELL32.dll` (1 names): `SHGetFolderPathW`
- `SHLWAPI.dll` (10 names): `(ordinal-only import; name unavailable)`, `PathCombineW`, `PathFileExistsW`, `PathFindExtensionW`, `PathIsDirectoryW`, `PathIsUNCW`, `PathRemoveFileSpecW`, `PathStripPathW`, `PathStripToRootW`, `SHCreateStreamOnFileW`
- `USER32.dll` (2 names): `CharLowerW`, `UnregisterClassA`
- `XmlLite.dll` (1 names): `CreateXmlReader`
- `msvcrt.dll` (100 names): `??0bad_cast@@QEAA@AEBV0@@Z`, `??0bad_cast@@QEAA@PEBD@Z`, `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1bad_cast@@UEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?terminate@@YAXXZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `___lc_codepage_func`, `___lc_handle_func`, `___mb_cur_max_func`, `__crtGetStringTypeW`, `__crtLCMapStringW`, `__dllonexit`, `__mb_cur_max`, `__pctype_func`, `_aligned_free`, `_aligned_malloc`, `_amsg_exit`, `_callnewh`, `_errno`, `_i64tow`, `_i64tow_s`, `_initterm`, `_iob`, `_itow_s`, `_lock`, `_memicmp`, `_onexit`, `_purecall`, `_snwscanf_s`, `_stricmp`, `_unlock`, `_vscwprintf`, `_vsnprintf`, `_vsnwprintf`, `_wcsdup`, `_wcsicmp`, `_wcsnicmp`, `_wfsopen`, `_wtof`, `abort`, `calloc`, `ceil`, `fclose`, `feof`, `fflush`, `fgetc`, `fgetpos`, `fgets`, `fgetwc`, `floor`, `fopen`, `fprintf`, `fputwc`, `fputws`, `free`, `fseek`, `fsetpos`, `fwprintf`, `fwrite`, `iswdigit`, `iswspace`, `ldiv`, `malloc`, `memchr`, `memcmp`, `memcpy`, `memcpy_s`, `memmove_s`, `memset`, `realloc`, `setlocale`, `setvbuf`, `strcpy_s`, `towlower`, `ungetc`, `ungetwc`, `vfprintf`, `vswprintf_s`, `wcscat_s`, `wcschr`, `wcscmp`, `wcscpy_s`, `wcscspn`, `wcsncmp`, `wcsncpy_s`, `wcsnlen`, `wcsrchr`, `wcsspn`, `wcsstr`, `wcstok_s`, `wcstol`
- `ntdll.dll` (4 names): `RtlCaptureContext`, `RtlLengthSid`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/perfcore.dll`

Architecture: `i386:x86-64`; entry: `0x000000018001a5ac`; CLR metadata: **False**.

- `ADVAPI32.dll` (5 names): `CloseTrace`, `EventRegister`, `EventUnregister`, `OpenTraceW`, `ProcessTrace`
- `KERNEL32.dll` (28 names): `DeleteCriticalSection`, `EnterCriticalSection`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleExW`, `GetProcAddress`, `GetProcessHeap`, `GetSystemTimeAsFileTime`, `GetTickCount`, `HeapAlloc`, `HeapDestroy`, `HeapFree`, `HeapReAlloc`, `HeapSize`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadLibraryW`, `OutputDebugStringA`, `QueryPerformanceCounter`, `RaiseException`, `SetUnhandledExceptionFilter`, `Sleep`, `TerminateProcess`, `UnhandledExceptionFilter`
- `OLEAUT32.dll` (1 names): `(ordinal-only import; name unavailable)`
- `msvcrt.dll` (34 names): `??0exception@@QEAA@AEBQEBD@Z`, `??0exception@@QEAA@AEBQEBDH@Z`, `??0exception@@QEAA@AEBV0@@Z`, `??0exception@@QEAA@XZ`, `??1exception@@UEAA@XZ`, `??1type_info@@UEAA@XZ`, `?what@exception@@UEBAPEBDXZ`, `_CxxThrowException`, `_XcptFilter`, `__C_specific_handler`, `__CxxFrameHandler3`, `__dllonexit`, `_amsg_exit`, `_callnewh`, `_initterm`, `_iob`, `_lock`, `_onexit`, `_purecall`, `_unlock`, `_wcsdup`, `_wcsicmp`, `fprintf`, `free`, `ldiv`, `malloc`, `memcmp`, `memcpy`, `memcpy_s`, `memmove_s`, `memset`, `towlower`, `vfprintf`, `wcschr`
- `ntdll.dll` (3 names): `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`
- `ole32.dll` (1 names): `CoCreateInstance`
- Exports: `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`

## `bin/pt-BR/DiagnosticsTap.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/pt-BR/F12.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/pt-BR/F12Resources.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/pt-BR/F12Tools.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/pt-BR/iedvtool.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/pt-BR/ieinstal.exe.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/pt-BR/iexplore.exe.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/pt-BR/jsdbgui.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/pt-BR/jsprofilerui.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/pt-BR/networkinspection.dll.mui`

Architecture: `i386`; entry: `0x00000000`; CLR metadata: **False**.

- No named imports recovered (resource-only image or parser limitation).
- Exports: none recovered.

## `bin/sqmapi.dll`

Architecture: `i386:x86-64`; entry: `0x00000001800014d4`; CLR metadata: **False**.

- `ADVAPI32.dll` (36 names): `ConvertSidToStringSidW	800019f0`, `ConvertStringSecurityDescriptorToSecurityDescriptorW	80004330`, `CreateWellKnownSid	800013a0`, `CryptAcquireContextW	800021a0`, `CryptGenRandom	80001360`, `CryptReleaseContext	80001370`, `GetFileSecurityW	80006340`, `GetSecurityDescriptorDacl	80001350`, `GetSecurityDescriptorOwner	800064e0`, `GetTokenInformation	80001250`, `GetTraceEnableFlags	001f`, `GetTraceEnableLevel	0022`, `GetTraceLoggerHandle	0023`, `ImpersonateLoggedOnUser	80001510`, `InitializeSecurityDescriptor	800012f0`, `OpenProcessToken	80001270`, `OpenThreadToken	80001220`, `RegCloseKey	800013b0`, `RegCreateKeyExW	80001cf0`, `RegDeleteKeyW	80006fe0`, `RegDeleteValueW	80001470`, `RegEnumKeyExW	80001bd0`, `RegEnumKeyW	800014d0`, `RegEnumValueW	80001c40`, `RegOpenKeyExW	800013d0`, `RegQueryInfoKeyW	80001ad0`, `RegQueryValueExW	800013f0`, `RegSetValueExW	80001d50`, `RegisterTraceGuidsW	0021`, `RevertToSelf	80001230`, `SetEntriesInAclW	80006190`, `SetFileSecurityW	80006320`, `SetNamedSecurityInfoW	8000cdb0`, `SetSecurityDescriptorDacl	80001300`, `TraceMessage	ffffffff`, `UnregisterTraceGuids	0020`
- `KERNEL32.dll` (97 names): `CloseHandle	8000152c`, `CompareFileTime	80002ecc`, `CompareStringW	80001b20`, `CopyFileW	8000d1a4`, `CreateDirectoryW	80003608`, `CreateEventW	80002e6c`, `CreateFileMappingW	80003030`, `CreateFileW	80002e54`, `CreateMutexW	80001988`, `CreateThread	80001dac`, `DelayLoadFailureHook	8004da0c`, `DeleteCriticalSection	0056`, `DeleteFileW	800035e0`, `DisableThreadLibraryCalls	80001cd0`, `DuplicateHandle	80002d5c`, `EnterCriticalSection	ffffffff`, `ExpandEnvironmentStringsW	80001c5c`, `FileTimeToSystemTime	80003400`, `FindClose	80002db8`, `FindFirstFileW	80002dc4`, `FindNextFileW	80002dd0`, `FindResourceW	800033b8`, `FreeLibrary	80001b98`, `FreeLibraryAndExitThread	80004870`, `FreeResource	8000d0f0`, `GetCurrentProcess	800013b0`, `GetCurrentProcessId	80001410`, `GetCurrentThread	800013e0`, `GetCurrentThreadId	80001250`, `GetEnvironmentVariableW	80003510`, `GetFileAttributesExW	80003424`, `GetFileAttributesW	80003418`, `GetFileSize	80002ea0`, `GetFileSizeEx	8000334c`, `GetLastError	800014e0`, `GetLongPathNameW	800096e0`, `GetModuleFileNameW	80001cf0`, `GetModuleHandleExW	80002d80`, `GetNativeSystemInfo	80003590`, `GetProcAddress	80001d30`, `GetSystemDefaultLCID	80002e0c`, `GetSystemDirectoryW	80002b08`, `GetSystemTime	80001be0`, `GetSystemTimeAsFileTime	80001550`, `GetSystemWow64DirectoryW	800265d4`, `GetTempFileNameW	8003e408`, `GetTempPathW	8000d020`, `GetThreadPriority	80001b68`, `GetTickCount	80001230`, `GetUserGeoID	80045330`, `GetVersionExW	800019b0`, `GlobalFree	80002f80`, `InitializeCriticalSection	0049`, `InitializeCriticalSectionAndSpinCount	80001448`, `LeaveCriticalSection	005f`, `LoadLibraryExA	80003564`, `LoadLibraryExW	80002ebc`, `LoadLibraryW	80003550`, `LoadResource	80003388`, `LocalAlloc	80001350`, `LocalFree	80001340`, `LockResource	80003398`, `MapViewOfFile	80001d70`, `OpenFileMappingW	80003378`, `OpenMutexW	80025030`, `OutputDebugStringA	80001cb4`, `QueryPerformanceCounter	80001390`, `ReadFile	80002e60`, `ReleaseMutex	80001020`, `ResetEvent	80001460`, `RtlCaptureContext	8003e3e0`, `RtlLookupFunctionEntry	8003e390`, `RtlVirtualUnwind	8003e3a4`, `SetErrorMode	800035b8`, `SetEvent	80001454`, `SetFileAttributesW	80003614`, `SetFilePointer	80002e84`, `SetFilePointerEx	80024e10`, `SetLastError	800014f0`, `SetThreadPriority	80001a80`, `SetUnhandledExceptionFilter	80002be4`, `SizeofResource	800033a8`, `Sleep	80001010`, `SystemTimeToFileTime	80001bf0`, `TerminateProcess	80003900`, `UnhandledExceptionFilter	8005b774`, `UnmapViewOfFile	800013c0`, `VerSetConditionMask	0054`, `VerifyVersionInfoW	800028fc`, `VirtualAlloc	800013f0`, `VirtualFree	80001bb8`, `VirtualProtect	80001a90`, `WaitForMultipleObjectsEx	80001abc`, `WaitForSingleObject	8000102c`, `WideCharToMultiByte	80002d20`, `WriteFile	80002e78`, `lstrlenW	80001510`
- `RPCRT4.dll` (3 names): `RpcStringFreeW	8000af94`, `UuidCreateSequential	800305b0`, `UuidToStringW	8000b000`
- `USER32.dll` (5 names): `DispatchMessageW	80001520`, `GetSystemMetrics	800035a0`, `MsgWaitForMultipleObjects	80003090`, `PeekMessageW	800010c0`, `TranslateMessage	800011c0`
- `msvcrt.dll` (52 names): `??1type_info@@UEAA@XZ	10154180`, `_CxxThrowException	10124198`, `_XcptFilter	1015fefc`, `__C_specific_handler	ffffffff`, `__CxxFrameHandler	10124734`, `__badioinfo	1018f5e0`, `__mb_cur_max	1018ef48`, `__pioinfo	1018e620`, `_amsg_exit	101677e4`, `_callnewh	10156f5c`, `_errno	101035bc`, `_fileno	101019d0`, `_initterm	10103cd0`, `_purecall	10161710`, `_read	10113698`, `_strtoui64	10129ad0`, `_vsnprintf	10104794`, `_vsnwprintf	101034b0`, `_wcsicmp	101019f0`, `_wcsnicmp	10103900`, `_wfopen	10116514`, `_wtoi	10106458`, `_wtoi64	1010fccc`, `calloc	10103c5c`, `ceilf	101014d0`, `fclose	10109c80`, `fread	101166a0`, `free	101011a0`, `fseek	10116920`, `fwprintf	10128fb8`, `fwrite	10115244`, `isdigit	10106550`, `isleadbyte	1010d1c8`, `iswalpha	10103cc0`, `iswctype	101039c0`, `isxdigit	1012a154`, `localeconv	1010919c`, `malloc	10101364`, `mbtowc	10106710`, `memcpy	10101100`, `memset	10101060`, `rand	10101694`, `realloc	1010387c`, `srand	101052ec`, `time	1010536c`, `ungetc	10176db4`, `wcschr	10103990`, `wcsncmp	10103650`, `wcsrchr	10103c28`, `wcsstr	101022b8`, `wcstombs	1012a40c`, `wctomb	1014d164`
- `ntdll.dll` (4 names): `NtQuerySystemTime	80003140`, `RtlAllocateHeap	80005630`, `RtlFreeHeap	800054c0`, `RtlGetVersion	80014cb8`
- Exports: `SqmAddToAverage`, `SqmAddToStream`, `SqmAddToStreamDWord`, `SqmAddToStreamDWord64`, `SqmAddToStreamString`, `SqmAddToStreamV`, `SqmCheckEscalationAddToStreamDWord`, `SqmCheckEscalationAddToStreamDWord64`, `SqmCheckEscalationAddToStreamString`, `SqmCheckEscalationSetDWord`, `SqmCheckEscalationSetDWord64`, `SqmCheckEscalationSetString`, `SqmCleanup`, `SqmClearFlags`, `SqmCreateNewId`, `SqmEndSession`, `SqmEndSessionEx`, `SqmFlushSession`, `SqmGetEnabled`, `SqmGetEscalationRuleStatus`, `SqmGetFlags`, `SqmGetInstrumentationProperty`, `SqmGetLastUploadTime`, `SqmGetMachineId`, `SqmGetSession`, `SqmGetSessionStartTime`, `SqmGetUserId`, `SqmIncrement`, `SqmIsNamespaceEnabled`, `SqmIsWindowsOptedIn`, `SqmLoadEscalationManifest`, `SqmReadSharedMachineId`, `SqmReadSharedUserId`, `SqmSet`, `SqmSetAppId`, `SqmSetAppVersion`, `SqmSetBits`, `SqmSetBool`, `SqmSetCurrentTimeAsUploadTime`, `SqmSetDWord64`, `SqmSetEnabled`, `SqmSetEscalationInfo`, `SqmSetFlags`, `SqmSetIfMax`, `SqmSetIfMin`, `SqmSetMachineId`, `SqmSetString`, `SqmSetUserId`, `SqmStartSession`, `SqmStartUpload`, `SqmStartUploadEx`, `SqmSysprepCleanup`, `SqmSysprepGeneralize`, `SqmSysprepSpecialize`, `SqmTimerAccumulate`, `SqmTimerAddToAverage`, `SqmTimerRecord`, `SqmTimerStart`, `SqmUnattendedSetup`, `SqmUnloadEscalationManifest`, `SqmWaitForUploadComplete`, `SqmWriteSharedMachineId`, `SqmWriteSharedUserId`

