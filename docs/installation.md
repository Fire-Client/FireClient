---
id: installation
title: Multi-Platform Installation Guide
sidebar_label: Multi-Platform Overview
description: Complete installation guide for FireClient across Windows, macOS, Linux, existing mod loaders, and mobile wrappers.
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FireClient Multi-Platform Installation

**FireClient** runs natively across **Windows 10/11**, **macOS 12+ (Apple Silicon & Intel)**, and **Linux (`x86_64` & `arm64`)**, automatically managing Minecraft versions, Adoptium Java runtimes, Fabric/Forge/NeoForge loaders, Modrinth content, and verified SHA-256 client updates.

---

## 🚀 Choose Your Installation Method

<Tabs groupId="install-type">
<TabItem value="launcher" label="Desktop Launcher (Windows / macOS / Linux)" default>

### Option A: Official Desktop Launcher

Choose your operating system below, or view the full platform guide for [Windows](./windows), [macOS](./macos), or [Linux](./linux).

<Tabs groupId="operating-systems">
<TabItem value="windows" label="Windows (10 / 11)" default>

**One-Line PowerShell Install:**
```powershell
irm https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-windows.ps1 | iex
```

**Manual Installer:**
1. Download **`FireClient-Setup.exe`** (or **`FireClient-portable.zip`**) from [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases).
2. Run `FireClient-Setup.exe` (click **More info** ➔ **Run anyway** if prompted by SmartScreen).
3. See the full [Windows Installation Guide](./windows) for SHA-256 verification and GPU tuning.

</TabItem>
<TabItem value="macos" label="macOS (Apple Silicon & Intel)">

**One-Line Terminal Install:**
```bash
curl -fsSL https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-macos.sh | bash
```

**Manual DMG Setup:**
1. Download **`FireClient-macOS-universal.dmg`** (or `arm64` / `x64`) from [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases).
2. Open the `.dmg` and drag **FireClient** to **Applications**.
3. If Gatekeeper blocks first launch, open **System Settings** ➔ **Privacy & Security** ➔ **Open Anyway** (or see the full [macOS Installation Guide](./macos)).

</TabItem>
<TabItem value="linux" label="Linux (AppImage / .deb / .tar.gz)">

**One-Line Terminal Install:**
```bash
curl -fsSL https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-linux.sh | bash
```

**Manual AppImage / Debian Setup:**
```bash
# Universal AppImage
curl -fL "https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-Linux-x86_64.AppImage" -o FireClient-Linux-x86_64.AppImage
chmod +x FireClient-Linux-x86_64.AppImage
./FireClient-Linux-x86_64.AppImage
```
Or install **`FireClient-Linux-amd64.deb`** via `sudo apt install ./FireClient-Linux-amd64.deb`. See the full [Linux Installation Guide](./linux) for distro tips and GPU offload.

</TabItem>
</Tabs>

</TabItem>
<TabItem value="fabric-mod" label="Existing Launcher / Mod Loader">

### Option B: Standalone Mod (Prism, MultiMC, Vanilla Launcher)

If you already use an existing third-party launcher and want the in-game FireClient HUD & utility mod:

1. **Install Fabric or Forge:** Create a profile with **Fabric Loader** (1.21.1 / 1.21.4) or **Forge** (1.8.9 / 1.20.1).
2. **Install Fabric API (Fabric profiles):** Download [Fabric API](https://modrinth.com/mod/fabric-api) and place it into your instance's `mods/` folder.
3. **Add FireClient Mod JAR:**
   * Obtain the latest bundled mod from [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases) or [Modrinth](https://modrinth.com/mod/fireclient).
   * Place `fireclient-<version>.jar` into your `.minecraft/mods` directory.
4. **Launch Profile:** Start Minecraft and press **`Right Shift`** in-game to open the FireClient menu.

</TabItem>
<TabItem value="mobile" label="Mobile (PojavLauncher)">

### Option C: Mobile Setup (Android)

FireClient's Fabric mod can be loaded on Android Java wrappers such as **PojavLauncher**:

1. Install **PojavLauncher** and create a **Fabric Loader 1.21.1** profile.
2. Copy `fireclient-<version>.jar` (plus matching Fabric API) into:
   ```text
   /sdcard/Android/data/net.kdt.pojavlaunch/files/.minecraft/mods/
   ```
3. Allocate at least **1536 MB – 2048 MB** of RAM in PojavLauncher settings and launch.

</TabItem>
</Tabs>
