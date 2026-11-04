---
id: windows
title: Windows Installation & Setup
sidebar_label: Windows
description: Step-by-step installation and optimization guide for FireClient on Windows 10 and 11 (64-bit).
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Installing FireClient on Windows

This guide provides end-to-end instructions for installing, verifying, and optimizing **FireClient** on **Windows 10** and **Windows 11 (64-bit)**.

---

## ⚡ Quick One-Line PowerShell Install

Open **Windows PowerShell** or **Windows Terminal** and run:

```powershell
irm https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-windows.ps1 | iex
```

The script downloads `FireClient-Setup.exe` from the official verified feed, verifies its `SHA-256` hash against `SHA256SUMS.txt`, inspects the Authenticode signature, and runs the user-scoped installer automatically.

---

## 📥 Direct Download Options

Select your preferred distribution from [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases):

| Package | Format | Best For | Link |
| :--- | :--- | :--- | :--- |
| **Windows Installer** | `.exe` (NSIS) | Standard automatic setup, updater & desktop shortcuts | [FireClient-Setup.exe](https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-Setup.exe) |
| **Portable Edition** | `.zip` | USB drives, restricted user accounts (no installer needed) | [FireClient-portable.zip](https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-portable.zip) |

---

## 🛡️ Step 1: Verify Checksum (Recommended)

To ensure the installer has not been tampered with or corrupted during download, verify its SHA-256 hash using Windows PowerShell:

1. Press `Win + X` and select **Terminal** or **Windows PowerShell**.
2. Run the following command:

```powershell
Get-FileHash -Path "$HOME\Downloads\FireClient-Setup.exe" -Algorithm SHA256
```

3. Compare the printed hash against `SHA256SUMS.txt` or `FireClient-Setup.exe.sha256` published on [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases/latest).

---

## 💻 Step 2: Running the Installer & SmartScreen

<Tabs groupId="install-flavor">
<TabItem value="installer" label="Standard Installer (.exe)" default>

1. Double-click **`FireClient-Setup.exe`**.
2. **Windows Defender SmartScreen:**
   If SmartScreen warns about a newly published build:
   > *"Windows protected your PC"*
   
   * Click **More info**.
   * Click **Run anyway**.

   :::note Why does this happen?
   SmartScreen reputation builds gradually for each new binary hash. Only download from [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases) or [fireclient.net](https://fireclient.net).
   :::

3. Review the Terms & Privacy notice and click **I Agree**.
4. FireClient installs cleanly into `%LocalAppData%\Programs\FireClient` without requiring Administrator elevation (`asInvoker`).
5. Launch **FireClient** from your Desktop or Start Menu shortcut.

</TabItem>
<TabItem value="portable" label="Portable Edition (.zip)">

1. Download **`FireClient-portable.zip`**.
2. Right-click the `.zip` file and select **Extract All...**.
3. Choose a persistent directory (e.g., `D:\Games\FireClient` or `C:\FireClient`).
4. Run `FireClient.exe` directly.

</TabItem>
</Tabs>

---

## ⚡ Step 3: Configure Dedicated GPU (High Performance)

FireClient automatically requests high-performance GPU preference for spawned Java processes, and you can also pin `FireClient.exe` in Windows Graphics settings:

1. Open **Windows Settings** (`Win + I`) ➔ **System** ➔ **Display** ➔ **Graphics**.
2. Under "Custom options for apps", click **Browse**.
3. Select the FireClient executable:
   ```text
   %LocalAppData%\Programs\FireClient\FireClient.exe
   ```
4. Click **Options** on the newly added item.
5. Select **High performance** (your dedicated NVIDIA / AMD GPU) and click **Save**.

---

## 🛡️ Step 4: Windows Defender & Antivirus Exclusions

If real-time asset scanning slows down first-time Minecraft library extraction, you can exclude FireClient's data and program directories in an **Administrator PowerShell** window:

```powershell
Add-MpPreference -ExclusionPath "$HOME\.fireclient"
Add-MpPreference -ExclusionPath "$env:LOCALAPPDATA\Programs\FireClient"
```

*Or manually via Windows Security:*
1. Open **Windows Security** ➔ **Virus & threat protection**.
2. Under *Virus & threat protection settings*, click **Manage settings**.
3. Scroll to **Exclusions** and click **Add or remove exclusions**.
4. Choose **Folder** and select `%USERPROFILE%\.fireclient`.

---

## 🎮 Step 5: First Launch & In-Game Controls

1. **Choose Mode:** Play immediately in **Offline Mode**, or click **Sign In with Microsoft** for Online Mode (tokens are encrypted locally with Windows DPAPI).
2. **Allocate RAM:** Go to **Settings** ➔ **Memory**:
   * Minimum: `2048 MB`
   * Maximum: `4096 MB` (4 GB recommended for 1.21+)
3. Click **Play** to start Minecraft.
4. **Open Client Menu:** Once in-game, press **`Right Shift`** to customize your HUD modules, enable keystrokes, and manage widgets.
