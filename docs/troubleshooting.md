---
id: troubleshooting
title: Troubleshooting & FAQ
sidebar_label: Troubleshooting & FAQ
---

# Troubleshooting & Frequently Asked Questions

Common solutions for installation prompts, Java selection, GPU drivers, and launcher errors across **Windows**, **macOS**, and **Linux**.

---

## 🛑 Common Errors & Solutions

### 1. Game Crashes with "Exit Code: 1"
* **Symptom:** Minecraft closes shortly after clicking **Play**.
* **Solution:**
  1. Open FireClient **Console** to view the exact error line.
  2. In **Settings** ➔ **Java**, ensure Automatic Java is enabled (or select a 64-bit **Java 21** runtime for Minecraft 1.20.5+, **Java 17** for 1.18–1.20.4).
  3. Update your GPU drivers (NVIDIA, AMD, Intel, or Mesa on Linux) so OpenGL 4.4+ is available.

### 2. Windows Defender SmartScreen Alert
* **Symptom:** Windows displays *"Windows protected your PC"* on a newly released installer.
* **Solution:**
  1. Verify your download came from [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases) or [fireclient.net](https://fireclient.net).
  2. Check its SHA-256 hash: `Get-FileHash "$HOME\Downloads\FireClient-Setup.exe" -Algorithm SHA256`.
  3. Click **More info** ➔ **Run anyway**.

### 3. macOS Gatekeeper ("Developer Cannot Be Verified")
* **Symptom:** macOS blocks `FireClient.app` on first launch after manual `.dmg` drag-and-drop.
* **Solution:**
  * Run the 1-line installer (`curl -fsSL https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-macos.sh | bash`), **or** clear quarantine manually:
    ```bash
    xattr -dr com.apple.quarantine /Applications/FireClient.app
    ```
  * Alternatively, go to **System Settings** ➔ **Privacy & Security** and click **Open Anyway**.

### 4. Linux AppImage Does Not Open (`dlopen(): error loading libfuse.so.2`)
* **Symptom:** Double-clicking `FireClient-Linux-x86_64.AppImage` on Ubuntu 22.04+ / 24.04+ exits silently.
* **Solution:**
  * Install FUSE 2 (`sudo apt install -y libfuse2t64` on Ubuntu 24.04+, or `sudo apt install -y libfuse2`), **or** run without FUSE:
    ```bash
    ./FireClient-Linux-x86_64.AppImage --appimage-extract-and-run
    ```
  * On Ubuntu/Debian, you can also install the native `.deb` package (`sudo apt install ./FireClient-Linux-amd64.deb`).

### 5. In-Game Menu (`Right Shift`) Does Not Open
* **Symptom:** Pressing `Right Shift` in-game does nothing.
* **Solution:**
  1. Open Minecraft **Options** ➔ **Controls** ➔ **Key Binds**.
  2. Find **FireClient: Open Menu** and rebind it if another mod conflicts with `Right Shift`.

### 6. Fabric / Forge Mixin Conflict Crash
* **Symptom:** Crash log mentions `MixinTransformerError`.
* **Solution:**
  1. Open the **Mods** tab in FireClient.
  2. Toggle off duplicate third-party HUD or custom title-screen mods that patch the same screens.

---

## ❓ Frequently Asked Questions

#### Is FireClient free to use?
Yes! FireClient is completely free to download and play in both **Offline Mode** and **Online Mode** (Microsoft account). See the repository `LICENSE` for redistribution terms.

#### Where are my worlds, mods, and profiles stored?
Everything lives in `.fireclient` inside your user home folder:
* **Windows:** `%USERPROFILE%\.fireclient` (`C:\Users\<You>\.fireclient`)
* **macOS:** `~/.fireclient` (`/Users/<you>/.fireclient`)
* **Linux:** `~/.fireclient` (`/home/<you>/.fireclient`)

Uninstalling or updating FireClient never deletes your worlds, saves, or profiles.

#### Can I use FireClient on multiplayer servers?
Yes. FireClient is a quality-of-life HUD and performance client and contains zero cheat modules. Always check individual server rules regarding HUD indicators such as armor or effect timers.
