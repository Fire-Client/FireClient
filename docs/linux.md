---
id: linux
title: Linux Installation & Setup
sidebar_label: Linux
description: Step-by-step installation guide for FireClient on Ubuntu, Debian, Fedora, Arch Linux, Linux Mint, and SteamOS.
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Installing FireClient on Linux

**FireClient** runs natively on modern 64-bit Linux distributions (`x86_64` and `arm64`), including **Ubuntu**, **Debian**, **Linux Mint**, **Pop!_OS**, **Fedora**, **Arch Linux**, **openSUSE**, and **SteamOS**.

---

## ⚡ Quick One-Line Terminal Install (Recommended)

Run the official Linux installer script. It detects your distribution and architecture, downloads the optimal package (`.deb` on Debian/Ubuntu with `apt`, or `.AppImage` into `~/.local/opt/fireclient`), verifies `SHA-256` checksums, creates `~/.local/bin/fireclient`, and registers the desktop launcher entry:

```bash
curl -fsSL https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-linux.sh | bash
```

To force a specific format (`appimage`, `deb`, or `tar`), pass `--method`:

```bash
curl -fsSL https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-linux.sh | bash -s -- --method appimage
```

---

## 📥 Direct Download Options

Download packages directly from [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases):

| Package | Format | Best For | Link |
| :--- | :--- | :--- | :--- |
| **Universal AppImage** | `.AppImage` (`x86_64`) | All distros, SteamOS, immutable desktops, no root needed | [FireClient-Linux-x86_64.AppImage](https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-Linux-x86_64.AppImage) |
| **Debian / Ubuntu Package** | `.deb` (`amd64`) | Ubuntu 20.04+, Debian 11+, Linux Mint, Pop!_OS | [FireClient-Linux-amd64.deb](https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-Linux-amd64.deb) |
| **Portable Tarball** | `.tar.gz` (`x86_64`) | Arch Linux, Fedora, NixOS, custom `/opt` installs | [FireClient-Linux-x86_64.tar.gz](https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-Linux-x86_64.tar.gz) |

---

## 🛡️ Step 1: Verify SHA-256 Checksum

Verify your downloaded package against `SHA256SUMS.txt` on the [Verified Releases](https://github.com/untitledinfo/verifed-fireclient/releases/latest) page:

```bash
sha256sum ~/Downloads/FireClient-Linux-x86_64.AppImage
```

---

## 🐧 Step 2: Install by Package Format

<Tabs groupId="linux-package-format">
<TabItem value="appimage" label="AppImage (Universal)" default>

```bash
# 1. Download the latest AppImage
curl -fL "https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-Linux-x86_64.AppImage" \
  -o "$HOME/Downloads/FireClient-Linux-x86_64.AppImage"

# 2. Mark executable
chmod +x "$HOME/Downloads/FireClient-Linux-x86_64.AppImage"

# 3. Launch FireClient
"$HOME/Downloads/FireClient-Linux-x86_64.AppImage"
```

:::tip Missing `libfuse.so.2` on Ubuntu 22.04+ / 24.04+?
AppImages use FUSE 2, or can run without FUSE using `--appimage-extract-and-run`:
```bash
# Option A: Install FUSE 2 (Ubuntu 24.04+: libfuse2t64, Ubuntu 22.04: libfuse2)
sudo apt update && sudo apt install -y libfuse2t64 || sudo apt install -y libfuse2

# Option B: Run without FUSE
./FireClient-Linux-x86_64.AppImage --appimage-extract-and-run
```
:::

</TabItem>
<TabItem value="deb" label="Ubuntu / Debian (.deb)">

```bash
# 1. Download the .deb package
curl -fL "https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-Linux-amd64.deb" \
  -o /tmp/FireClient-Linux-amd64.deb

# 2. Install via apt (automatically resolves dependencies)
sudo apt update
sudo apt install -y /tmp/FireClient-Linux-amd64.deb

# 3. Launch from application menu or terminal
fireclient
```

</TabItem>
<TabItem value="tarball" label="Tarball (.tar.gz)">

```bash
mkdir -p ~/.local/opt/fireclient ~/.local/bin
curl -fL "https://github.com/untitledinfo/verifed-fireclient/releases/latest/download/FireClient-Linux-x86_64.tar.gz" \
  -o /tmp/FireClient-Linux-x86_64.tar.gz

tar -xzf /tmp/FireClient-Linux-x86_64.tar.gz -C ~/.local/opt/fireclient --strip-components=1
ln -sf ~/.local/opt/fireclient/fireclient ~/.local/bin/fireclient
~/.local/bin/fireclient
```

</TabItem>
</Tabs>

---

## ⚡ GPU Drivers & Wayland / X11 Tips

* **NVIDIA Hybrid Laptops (PRIME Offload):** Launch FireClient with dedicated GPU offload enabled so Minecraft uses your discrete NVIDIA GPU:
  ```bash
  __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia fireclient
  ```
* **AMD / Intel Mesa:** Ensure `mesa-utils` and up-to-date Mesa drivers (`OpenGL 4.4+`) are installed (`glxinfo -B`).
* **Data & Secret Storage:**
  * **Game Data, Mods & Worlds:** `~/.fireclient`
  * **Desktop Entry:** `~/.local/share/applications/fireclient.desktop`
  * **Account Encryption:** Microsoft OAuth tokens are encrypted locally via **`libsecret`** (GNOME Keyring / KDE Wallet).
