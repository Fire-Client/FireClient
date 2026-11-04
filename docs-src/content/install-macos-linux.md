---
title: Install FireClient on macOS and Linux
description: Install FireClient on macOS 12 or later and on 64-bit Linux using the DMG, AppImage, deb package or the official install scripts.
group: Get started
order: 4
---
> **Note:** The FireClient GitHub README lists macOS and Linux support. The website still marks them as not available. Confirm the files exist on the [download page](download.md) before you start.

## macOS 12 or later

Works on Apple Silicon (M1 to M4) and Intel.

1. Download `FireClient-macOS-universal.dmg`.
2. Open the DMG and drag **FireClient** into **Applications**.
3. If Gatekeeper blocks it, open **System Settings**, then **Privacy & Security**, and approve it.

Or use the script:

```bash
curl -fsSL https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-macos.sh | bash
```

## Linux

Listed for Ubuntu, Debian, Fedora, Arch, Mint and SteamOS. Pick one file:

- `FireClient-Linux-x86_64.AppImage`. Make it executable (`chmod +x`) and run it.
- `FireClient-Linux-amd64.deb`. Install with your package manager.
- `FireClient-Linux-x86_64.tar.gz`. Extract and run.

Or use the script:

```bash
curl -fsSL https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts/install-linux.sh | bash
```

> **Warning:** Piping a script into `bash` runs it with your permissions. Read it first if you want to be sure.

On macOS and Linux your login token is stored with the system keychain or `libsecret`. See [Accounts](accounts.md).
