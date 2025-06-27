set imagename=bbdq_h_BTC_30.exe
tasklist /fi "IMAGENAME eq %imagename%" | find /i "%imagename%"
if not errorlevel 1 (
	echo bbdq_h_BTC_30.exe is running
) else (
	echo bbdq_h_BTC_30.exe is NOT running...
	cd c:\1
	bbdq_h_BTC_30.exe
)

set imagename=bbdq_h_ETH_30.exe
tasklist /fi "IMAGENAME eq %imagename%" | find /i "%imagename%"
if not errorlevel 1 (
	echo bbdq_h_ETH_30.exe is running
) else (
	echo bbdq_h_ETH_30.exe is NOT running...
	cd c:\1
	bbdq_h_ETH_30.exe
)

set imagename=bbdq_h_OM_30.exe
tasklist /fi "IMAGENAME eq %imagename%" | find /i "%imagename%"
if not errorlevel 1 (
	echo bbdq_h_OM_30.exe is running
) else (
	echo bbdq_h_OM_30.exe is NOT running...
	cd c:\1
	bbdq_h_OM_30.exe
)

set imagename=bbdq_h_TRX_30.exe
tasklist /fi "IMAGENAME eq %imagename%" | find /i "%imagename%"
if not errorlevel 1 (
	echo bbdq_h_TRX_30.exe is running
) else (
	echo bbdq_h_TRX_30.exe is NOT running...
	cd c:\1
	bbdq_h_TRX_30.exe
)

set imagename=bbdq_subak.exe
tasklist /fi "IMAGENAME eq %imagename%" | find /i "%imagename%"
if not errorlevel 1 (
	echo bbdq_subak.exe is running
) else (
	echo bbdq_subak.exe is NOT running...
	cd c:\1
	bbdq_subak.exe
)

