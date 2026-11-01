---
id: installation
title: Multi-Platform Installation Guide
sidebar_label: Multi-Platform Install
description: Complete installation guide for FireClient launcher, Fabric client, and building from source.
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FireClient Installation

**FireClient** is a fast, lightweight Minecraft Java Edition launcher and bundled client designed for performance, custom HUD modules, and multiplayer optimization.

---

## 🚀 Choose Your Installation Method

<Tabs groupId="install-type">
<TabItem value="launcher" label="Desktop Launcher" default>

### Option A: Standalone Desktop Launcher

The desktop launcher automatically manages Minecraft installations, Java runtimes, Fabric dependencies, and automatic client updates.

<Tabs groupId="operating-systems">
<TabItem value="windows" label="Windows (10 / 11)" default>

See our dedicated [Windows Installation Guide](./windows) for full details.

1. Download **`FireClient-Setup.exe`** from the [GitHub Releases](https://github.com/Fire-Client/FireClient/releases).
2. Run the installer (Click **More info** ➔ **Run anyway** if prompted by SmartScreen).
3. Follow the setup wizard and launch the client.

</TabItem>
<TabItem value="linux" label="Linux">

1. Download the **`FireClient.AppImage`**:
   ```bash
   wget https://github.com/Fire-Client/FireClient/releases/latest/download/FireClient.AppImage
   ```
2. Make the file executable:
   ```bash
   chmod +x FireClient.AppImage
   ```
3. Run FireClient:
   ```bash
   ./FireClient.AppImage
   ```

</TabItem>
<TabItem value="macos" label="macOS">

1. Download **`FireClient.dmg`** (Apple Silicon or Intel).
2. Open the disk image and drag **FireClient** into your **Applications** folder.
3. If macOS blocks opening the app:
   * Open **System Settings** ➔ **Privacy & Security**.
   * Scroll down to **Security** and click **Open Anyway**.

</TabItem>
</Tabs>

</TabItem>
<TabItem value="fabric-mod" label="Existing Launcher / Mod Loader">

### Option B: Fabric Mod (Prism, CurseForge, Vanilla Launcher)

If you already use an existing launcher and only want the FireClient in-game client features (HUD, CPS/FPS counter, SMP kits):

1. **Install Fabric Loader:** Ensure you have **Fabric 1.21+** installed on your target profile.
2. **Install Fabric API:** Download the matching version of [Fabric API](https://modrinth.com/mod/fabric-api) and place it into your `.minecraft/mods` directory.
3. **Download FireClient Mod:**
   * Get the latest `.jar` from the [GitHub Releases](https://github.com/Fire-Client/FireClient/releases) or [Modrinth](https://modrinth.com/mod/fireclient).
   * Copy `fireclient-<version>.jar` into your `.minecraft/mods` directory.
4. **Launch Profile:** Start your Minecraft profile using Fabric Loader.

</TabItem>
<TabItem value="mobile" label="Mobile (PojavLauncher)">

### Option C: Mobile Setup (Android)

FireClient can be loaded on mobile devices using Java wrappers like **PojavLauncher**:

1. Install **PojavLauncher** from GitHub or Google Play.
2. Create a new profile selecting **Fabric Loader** on Minecraft **1.21.1**.
3. Under the instance folder, navigate to:
   ```text
   /sdcard/Android/data/net.kdt.pojavlaunch/files/.minecraft/mods/
   ```
4. Place `fireclient-<version>.jar` into the `mods` folder.
5. In PojavLauncher settings, set allocated memory to at least **1500 MB - 2048 MB**.
6. Launch and play.

</TabItem>
</Tabs>
