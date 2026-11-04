---
id: macos
title: macOS Installation & Setup
sidebar_label: macOS
description: Step-by-step installation guide for FireClient on macOS 12 Monterey and newer (Apple Silicon M1–M4 & Intel).
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Installing FireClient on macOS

This guide covers installing, verifying, and running **FireClient** on **macOS 12 Monterey or newer**, supporting both **Apple Silicon (`arm64` — M1, M2, M3, M4)** and **Intel (`x64`)** Macs.

---

## ⚡ Quick One-Line Terminal Install (Recommended)

Open **Terminal** (`Cmd + Space` ➔ type `Terminal`) and run the official installer script. It automatically detects your Mac architecture, downloads the latest verified `.dmg`, verifies its `SHA-256` checksum, installs `FireClient.app` to `/Applications` (or `~/Applications`), and clears Gatekeeper quarantine attributes:

```bash
curl -fsSL https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-macos.sh | bash
```

---

## 📥 Direct Download Options

Prefer installing manually? Download the disk image matching your Mac from [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases):

| Package | Architecture | Best For | Link |
| :--- | :--- | :--- | :--- |
| **Universal Disk Image** | `universal` (`arm64` + `x64`) | Any Mac (Apple Silicon or Intel) | [FireClient-macOS-universal.dmg](https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-macOS-universal.dmg) |
| **Apple Silicon Disk Image** | `arm64` (M1 / M2 / M3 / M4) | Smallest download on Apple Silicon Macs | [FireClient-macOS-arm64.dmg](https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-macOS-arm64.dmg) |
| **Intel Disk Image** | `x64` | Intel-based MacBook / iMac / Mac Pro | [FireClient-macOS-x64.dmg](https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-macOS-x64.dmg) |

---

## 🛡️ Step 1: Verify SHA-256 Checksum

Before mounting a manually downloaded `.dmg`, verify its integrity in **Terminal**:

```bash
shasum -a 256 ~/Downloads/FireClient-macOS-universal.dmg
```

Compare the output hash against `SHA256SUMS.txt` on the [Verified Releases](https://github.com/untitledinfo/verifed-fireclient/releases/latest) page.

---

## 🍎 Step 2: Install & Gatekeeper Approval

<Tabs groupId="macos-install-method">
<TabItem value="dmg" label="Manual DMG Setup" default>

1. Double-click **`FireClient-macOS-universal.dmg`** in `~/Downloads`.
2. Drag **FireClient** into the **Applications** folder shortcut.
3. Eject the mounted `FireClient` volume from Finder.
4. Open **FireClient** from **Launchpad** or `/Applications/FireClient.app`.

</TabItem>
<TabItem value="gatekeeper" label="Gatekeeper / Unidentified Developer Fix">

If macOS displays *"FireClient cannot be opened because the developer cannot be verified"* or *"FireClient is damaged and can't be opened"*:

**Option A — Via System Settings:**
1. Open **System Settings** ➔ **Privacy & Security**.
2. Scroll down to the **Security** section.
3. Click **Open Anyway** next to the FireClient message and authenticate with Touch ID or your password.

**Option B — Via Terminal (Instant):**
```bash
xattr -dr com.apple.quarantine /Applications/FireClient.app
open -a /Applications/FireClient.app
```

</TabItem>
</Tabs>

---

## 🔐 Keychain & Data Locations on macOS

* **Application Bundle:** `/Applications/FireClient.app` (or `~/Applications/FireClient.app` for non-admin accounts)
* **Game Data, Profiles, Mods & Worlds:** `~/.fireclient`
* **Bundled Java Runtimes:** `~/.fireclient/java` (native `aarch64` Temurin JDK 21 on Apple Silicon for full native FPS without Rosetta overhead)
* **Account Encryption:** Microsoft OAuth refresh tokens are encrypted locally via **macOS Keychain** (`safeStorage`) and never leave your Mac.

---

## 🎮 Step 3: First Launch

1. Choose **Offline Mode** or click **Sign In with Microsoft** for Online Mode.
2. Select your Minecraft version and loader (**Fabric**, **Forge**, **NeoForge**, or **Vanilla**).
3. Allocate memory in **Settings** ➔ **Memory** (`4096 MB` recommended for 1.21+).
4. Click **Play** — once in-game, press **`Right Shift`** to open the draggable FireClient HUD editor.
