---
id: github-install
title: Multi-Platform Architecture & Build Guide
sidebar_label: Architecture & Build
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Multi-Platform Architecture & Release Pipeline

This guide documents FireClient's multi-platform desktop architecture, release verification workflow, and packaging commands across **Windows**, **macOS**, and **Linux**.

---

## 1. Toolchain & Prerequisites

| Tool | Required Version | Verification Command | Purpose |
| :--- | :--- | :--- | :--- |
| **CMake + MSVC (VS 2022)** | `CMake 3.24+`, C++20 | `cmake --version` | Native Windows C++20 / WebView2 host (`FireClient.exe`) |
| **NSIS** | `3.09+` | `makensis /VERSION` | Windows user-scoped installer (`FireClient-Setup.exe`) |
| **Node.js & npm** | `Node 20 LTS` or `v22` | `node -v` | macOS & Linux Electron Desktop host (`desktop/`) & docs |
| **Java JDK** | `Java 21 (Temurin)` | `java -version` | Fabric / Forge in-game client mod compilation |
| **Gradle** | `8.8+` (`./gradlew`) | `./gradlew -v` | Fabric Loom & ForgeGradle build lifecycle |

---

## 2. Project Architecture

FireClient shares a single unified UI (`web/`) across a lightweight native Windows C++20/WebView2 executable and a cross-platform Electron host for macOS and Linux:

```text
FireClient/
├── native/                     # Windows 10/11 C++20 + WebView2 Host & Frameless Updater
│   ├── src/                    # Launcher core, Mojang/Adoptium downloader, SHA-256 updater
│   └── CMakeLists.txt
├── desktop/                    # macOS & Linux Electron Host (Apple Silicon, Intel, Linux x64/arm64)
│   ├── main.js                 # Full IPC parity, Modrinth manager, PaperMC host, Keychain/libsecret vault
│   ├── preload.js              # Context-isolated window.electronAPI bridge
│   ├── entitlements.mac.plist  # macOS Hardened Runtime & JIT entitlements
│   └── package.json            # electron-builder config (.dmg, .zip, .AppImage, .deb, .tar.gz)
├── web/                        # Shared Launcher Frontend & Glassmorphic Standalone Updater
│   ├── index.html              # Main launcher UI + Multi-OS Install Hub modal
│   └── updater.html            # Frameless verified update & release-notes window
├── mod/ & mod-forge/           # Bundled in-game FireClient HUD & PvP/SMP client mods
├── scripts/                    # 1-line OS installers & Authenticode / Defender verification suite
│   ├── install-windows.ps1
│   ├── install-macos.sh
│   ├── install-linux.sh
│   ├── Sign-And-Generate-Yml.ps1
│   └── Verify-Windows-Release.ps1
└── installer.nsi               # Windows NSIS installer script (asInvoker)
```

---

## 3. Building by Target Platform

<Tabs groupId="build-platform">
<TabItem value="windows" label="Windows (Native C++20 + NSIS)" default>

```powershell
# 1. Configure & compile native C++20 / WebView2 Release binary (x64)
cmake -S native -B native/build -A x64
cmake --build native/build --config Release

# 2. Package NSIS installer (FireClient-Setup.exe)
& "C:\Program Files (x86)\NSIS\makensis.exe" /V2 "/DVERSION=2.2.7" installer.nsi
```

Outputs:
* `native/build/Release/FireClient.exe`
* `dist-native/FireClient-Setup.exe`
* `dist-native/FireClient-portable.zip`

</TabItem>
<TabItem value="macos" label="macOS (.dmg Universal / arm64 / x64)">

```bash
cd desktop
npm ci

# Build Universal, Apple Silicon (arm64), and Intel (x64) DMG & ZIP artifacts
npm run dist:mac
```

Outputs in `dist-desktop/`:
* `FireClient-macOS-universal.dmg`
* `FireClient-macOS-arm64.dmg`
* `FireClient-macOS-x64.dmg`

</TabItem>
<TabItem value="linux" label="Linux (.AppImage / .deb / .tar.gz)">

```bash
cd desktop
npm ci

# Build AppImage, Debian package, and portable tarball
npm run dist:linux
```

Outputs in `dist-desktop/`:
* `FireClient-Linux-x86_64.AppImage`
* `FireClient-Linux-amd64.deb`
* `FireClient-Linux-x86_64.tar.gz`

</TabItem>
</Tabs>

---

## 4. Verified Release & Checksum Pipeline

Official binary releases are signed, scanned with Microsoft Defender, hashed (`SHA-256` & `SHA-512`), and published to [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases) via `.github/workflows/sign-release.yml`:

1. **`sign-windows`**: Authenticode-signs `FireClient-Setup.exe` with RFC 3161 timestamp fallback, verifies PE mitigations (`NX_COMPAT`, `DYNAMIC_BASE`) and `asInvoker` UAC manifest, scans with `MpCmdRun.exe`, and emits `latest.yml` + `FireClient-Setup.exe.sha256`.
2. **`build-macos`**: Packages Universal, `arm64`, and `x64` `.dmg`/`.zip` bundles on `macos-latest`.
3. **`build-linux`**: Packages `.AppImage`, `.deb`, and `.tar.gz` bundles on `ubuntu-latest`.
4. **`publish-release`**: Merges all platform hashes into `SHA256SUMS.txt` and publishes the verified GitHub Release consumed by FireClient's built-in updater and one-line installer scripts.
