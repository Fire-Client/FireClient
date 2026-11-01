---
id: index
title: Welcome to FireClient Docs
sidebar_label: Overview
slug: /
---

# Welcome to FireClient Documentation

**FireClient** is a modern, lightweight, high-performance Minecraft Java Edition launcher and bundled in-game client for **Windows 10/11**, **macOS 12+ (Apple Silicon & Intel)**, and **Linux (`x86_64` & `arm64`)**. It delivers ultra-fast launches, draggable HUD widgets for SMP and PvP, local PaperMC server hosting, and seamless Modrinth integration.

---

## 🌟 Key Highlights

* **Multi-Platform Desktop Hosts:** Native C++20/WebView2 runtime on Windows 10/11 plus native Apple Silicon & Intel `.dmg` builds on macOS and `.AppImage` / `.deb` / `.tar.gz` packages on Linux.
* **Integrated Modrinth & Server Suite:** Browse, install, and toggle mods, shaders, and resource packs in one click, or host and manage local PaperMC servers directly inside the launcher.
* **Modular In-Game HUD:** Customize your screen with draggable widgets—FPS, CPS, Ping, Coordinates, Armor Status, Keystrokes, and Effects—via the in-game GUI (`Right Shift`).
* **Verified Auto-Updater & Safe Auth:** Official Microsoft OAuth 2.0 + Offline Mode. Refresh tokens are encrypted locally via **Windows DPAPI**, **macOS Keychain**, or **Linux `libsecret`**, and every update is SHA-256 verified before launch.

---

## 🧭 Navigation

* [**Windows Installation Guide**](./windows): 1-line PowerShell setup, `.exe` & portable `.zip` downloads, SHA-256 verification, SmartScreen, and GPU tuning.
* [**macOS Installation Guide**](./macos): 1-line Terminal setup, Universal / Apple Silicon / Intel `.dmg` downloads, Gatekeeper approval, and Keychain notes.
* [**Linux Installation Guide**](./linux): 1-line Terminal setup, `.AppImage`, `.deb`, and `.tar.gz` packages, FUSE 2 tips, and NVIDIA PRIME offload.
* [**Multi-Platform Overview**](./installation): Unified comparison across Desktop Launcher, third-party Fabric/Forge profiles, and PojavLauncher.
* [**System Requirements**](./requirements): Hardware prerequisites and automatic Java 8 / 17 / 21 runtime matrix across Windows, macOS, and Linux.
* [**Architecture & Build Guide**](./github-install): Multi-platform build toolchain (`native/`, `desktop/`, `web/`, client mods, and GitHub Actions release verification).
* [**Troubleshooting & FAQ**](./troubleshooting): Fixes for Exit Code 1, SmartScreen, macOS Gatekeeper, Linux FUSE, and mixin conflicts.
