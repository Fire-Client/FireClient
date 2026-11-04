---
title: Install FireClient on Windows
description: Install the FireClient Minecraft launcher on Windows 10 or 11. Requirements, installer steps, the one-line PowerShell install and how to handle the SmartScreen warning.
group: Get started
order: 3
---
FireClient installs like any other Windows program. It takes a couple of minutes.

## Requirements

- Windows 10 or 11, 64-bit
- A Minecraft Java Edition account if you want to play online. Offline mode needs no account.
- Minecraft 1.21.1 with Fabric if you want the in-game menu and HUD

You do not need to install Java yourself. The launcher installs the runtime each version needs.

## Install with the installer

1. Download `FireClient-Setup.exe` from the [download page](download.md).
2. Optional: [check the file hash](verify-download.md).
3. Run the installer and accept the terms. Allow the Windows prompt if you trust the source.
4. Open FireClient and pick [offline or online mode](accounts.md).
5. Launch Minecraft 1.21.1 on Fabric. Press <kbd>Right Shift</kbd> to open the in-game menu.

## Install without the installer

Download `FireClient-portable.zip`, unzip it somewhere you control and run the launcher from there.

## One-line install

The project also publishes a PowerShell script:

```powershell
irm https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-windows.ps1 | iex
```

> **Warning:** This runs a script from the internet on your PC. Open the URL in a browser and read it first if you are not sure.

## SmartScreen warning

The installer is not code-signed yet. Windows SmartScreen may warn about a newly published build. This is expected for now, so check the [safety page](safety.md) and compare the hash before you continue.
