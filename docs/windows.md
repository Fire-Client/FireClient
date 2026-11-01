---
id: windows
title: Windows Installation & Setup
sidebar_label: Windows
description: Step-by-step installation and optimization guide for FireClient on Windows 10 and 11 (64-bit).
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Installing FireClient on Windows

This guide provides end-to-end instructions for installing, configuring, and optimizing **FireClient** on **Windows 10** and **Windows 11 (64-bit)**.

---

## 📥 Download Options

Select your preferred distribution from the official release channels:

| Package | Format | Best For | Link |
| :--- | :--- | :--- | :--- |
| **Windows Installer** | `.exe` (NSIS) | Standard automatic setup & desktop shortcuts | [Download .exe](https://github.com/Fire-Client/FireClient/releases/latest) |
| **Portable Edition** | `.zip` | USB drives, restricted user accounts (no admin) | [Download .zip](https://github.com/Fire-Client/FireClient/releases/latest) |

---

## 🛡️ Step 1: Verify Checksum (Recommended)

To ensure the installer has not been tampered with or corrupted during download, verify its SHA-256 hash using Windows PowerShell:

1. Press `Win + X` and select **Terminal** or **Windows PowerShell**.
2. Run the following command:

```powershell
Get-FileHash -Path "$HOME\Downloads\FireClient-Setup.exe" -Algorithm SHA256
```

3. Compare the printed hash against the release signature published on [GitHub Releases](https://github.com/Fire-Client/FireClient/releases).

---

## 💻 Step 2: Running the Installer & SmartScreen

<Tabs groupId="install-flavor">
<TabItem value="installer" label="Standard Installer (.exe)" default>

1. Double-click **`FireClient-Setup.exe`**.
2. **Bypassing Windows Defender SmartScreen:**
   Because early releases do not yet possess an EV code-signing certificate, Windows SmartScreen will display:
   > *"Windows protected your PC"*
   
   * Click **More info**.
   * Click **Run anyway**.

   :::note Why does this happen?
   SmartScreen flags newer executables based on certificate age, not malicious intent. FireClient is completely open-source, contains zero trackers, and never captures your credentials.
   :::

3. Choose your installation path (default: `%LocalAppData%\Programs\FireClient`).
4. Select whether to create a Desktop and Start Menu shortcut.
5. Click **Install**, then **Finish** to start FireClient.

</TabItem>
<TabItem value="portable" label="Portable Edition (.zip)">

1. Download **`FireClient-portable.zip`**.
2. Right-click the `.zip` file and select **Extract All...**.
3. Choose a persistent directory (e.g., `D:\Games\FireClient` or `C:\FireClient`).
4. Run `FireClient.exe` directly. All data, instances, and configurations will be stored locally in the portable directory.

</TabItem>
</Tabs>

---

## ⚡ Step 3: Configure Dedicated GPU (High Performance)

Ensure Windows assigns your dedicated graphics card (NVIDIA / AMD) to FireClient and Minecraft rather than integrated Intel graphics:

1. Open **Windows Settings** (`Win + I`) ➔ **System** ➔ **Display** ➔ **Graphics**.
2. Under "Custom options for apps", click **Browse**.
3. Select the FireClient executable:
   ```text
   %LocalAppData%\Programs\FireClient\FireClient.exe
   ```
4. Click **Options** on the newly added item.
5. Select **High performance** (your dedicated GPU) and click **Save**.

---

## 🛡️ Step 4: Windows Defender & Antivirus Exclusions

If you experience stuttering or slow instance launches, add an exclusion for FireClient’s working folder:

Run this command in an **Administrator PowerShell** window:

```powershell
Add-MpPreference -ExclusionPath "$env:APPDATA\.fireclient"
```

*Or manually via Windows Security:*
1. Open **Windows Security** ➔ **Virus & threat protection**.
2. Under *Virus & threat protection settings*, click **Manage settings**.
3. Scroll to **Exclusions** and click **Add or remove exclusions**.
4. Choose **Folder** and select `%AppData%\.fireclient`.

---

## 🎮 Step 5: First Launch & In-Game Controls

1. **Sign In:** Click **Sign In with Microsoft**. A secure OAuth window will authenticate your account directly with Mojang/Xbox Live.
2. **Allocate RAM:** Go to **Settings** ➔ **Memory**:
   * Minimum: `2048 MB`
   * Maximum: `4096 MB` (4 GB recommended for 1.21+)
3. Click **Play** to start Minecraft.
4. **Open Client Menu:** Once in-game, press **`Right Shift`** to customize your HUD modules, enable keystrokes, and manage mods.
