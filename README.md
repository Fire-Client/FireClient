<p align="center">
  <img src="assets/logo.png" alt="FireClient" width="140" height="140">
</p>

<h1 align="center">FireClient</h1>

<p align="center"><b>Minecraft, Your Way.</b></p>

<p align="center">
  A Windows launcher and in-game client for Minecraft.<br>
  Play offline with no account, or sign in and play online. Same launcher, your choice.
</p>

<p align="center">
  <a href="https://github.com/untitledinfo/fireclient-launcher/releases/download/v1.0/FireClient-Setup.exe"><img src="https://img.shields.io/badge/Download%20for%20Windows-FireClient--Setup.exe-E11D2E?style=for-the-badge" alt="Download FireClient-Setup.exe"></a>
</p>

<p align="center">
  <a href="https://github.com/untitledinfo/fireclient-launcher/releases"><img src="https://img.shields.io/github/downloads/untitledinfo/fireclient-launcher/total?style=flat-square&color=E11D2E&label=total%20downloads" alt="Total downloads"></a>
  <a href="https://github.com/untitledinfo/fireclient-launcher/releases/tag/v1.0"><img src="https://img.shields.io/github/downloads/untitledinfo/fireclient-launcher/v1.0/FireClient-Setup.exe?style=flat-square&color=E11D2E&label=v1.0%20installer" alt="Installer downloads"></a>
  <a href="https://github.com/untitledinfo/fireclient-launcher/releases/latest"><img src="https://img.shields.io/github/v/release/untitledinfo/fireclient-launcher?style=flat-square&color=E11D2E&label=latest" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/platform-Windows-1f1f23?style=flat-square" alt="Windows">
  <img src="https://img.shields.io/badge/license-proprietary-1f1f23?style=flat-square" alt="Proprietary license">
</p>

<p align="center">
  <a href="https://fireclient.net">Website</a> &nbsp;|&nbsp;
  <a href="https://github.com/untitledinfo/fireclient-launcher/releases">Releases</a> &nbsp;|&nbsp;
  <a href="https://discord.gg/jK74ZtrDFm">Discord</a> &nbsp;|&nbsp;
  <a href="LICENSE">License</a>
</p>

---

## What it is

FireClient installs and launches Minecraft, keeps your profiles, mods and resource packs organised, and ships an in-game client with its own menu and settings. It runs on Windows, stores everything in a folder you control, and doesn't require an account to get started.

> **Source status:** FireClient is **not open source**. This repository holds the README, license and release information. See [License](#license).

## Offline Mode and Online Mode

|  | Offline Mode | Online Mode |
|---|---|---|
| Account required | No | Microsoft account with Minecraft |
| Singleplayer | Yes | Yes |
| Servers that verify accounts | No | Yes |
| Servers running in offline mode | Yes | Yes |
| Skin | Local offline skins | Your account skin |
| Stored credentials | None | Token kept locally, encrypted with Windows DPAPI |

Switching between the two does not touch your worlds, profiles or mods.

Online Mode signs in through Microsoft, Xbox and Minecraft services. To join servers that verify accounts you need a legitimate Minecraft account.

## Features

**Launcher**
- Installs Minecraft versions and the Java runtime they need
- Profiles with separate versions, mods, resource packs and worlds
- Fabric, Forge and NeoForge support
- Update checks for the launcher, versions and loaders
- Optional Discord Rich Presence showing your version and server

**Mods, packs and shaders**
- Browse and install mods, resource packs and shaders from Modrinth
- Mod library lookup that identifies installed mods against public Modrinth projects
- Server downloads through PaperMC for local servers

**In-game client**
- Fabric and Forge builds of the client mod
- Custom title menu with a bottom icon-button grid in place of the vanilla menu
- HUD and client settings screen

**Community (optional)**
- Account profile, friends, messages, server listings and marketplace
- Entirely opt-in; nothing is sent unless you use it

**Your data, your machine**
- Preferences, profiles, worlds, screenshots, logs and skins live in one local `.fireclient` folder
- Game logs and crash logs stay on your PC
- One-click copy-diagnostics action for support, shared only when you paste it
- Uninstalling never deletes your worlds or game data

## Install

1. Download [`FireClient-Setup.exe`](https://github.com/untitledinfo/fireclient-launcher/releases/download/v1.0/FireClient-Setup.exe).
2. Run it and read the Terms & Privacy notice.
3. Choose **I Agree** to install.
4. Open FireClient and pick **Offline Mode**, or sign in for **Online Mode**.

**Requirements:** Windows 10 or 11 (64-bit) and an internet connection for game files and updates.

Windows SmartScreen may warn about a new or unsigned installer. Only download from the links on this page or [fireclient.net](https://fireclient.net).

## Privacy

FireClient only contacts a service when you use the feature that needs it.

| Feature | Who receives data |
|---|---|
| Online sign-in | Microsoft, Xbox, Minecraft services |
| Game, Java, loader and mod downloads | Mojang/Microsoft, Adoptium, Fabric, Forge, NeoForge, Modrinth, PaperMC, GitHub and their CDNs |
| Mod library lookup | Modrinth (local file hashes) |
| Community features | justiceclient.org |
| Discord Rich Presence | Your local Discord app |

Crash logs are never uploaded by the launcher. Back up important worlds before restoring or changing game files. Full terms are shown in the installer.

## License

FireClient is **proprietary, all rights reserved**. It is not open source.

- Allowed: download and use the installer for personal use.
- Not allowed: publish, sell, sublicense or redistribute FireClient-authored source, artwork or branding.

Read the full [LICENSE](LICENSE).

**Third-party notice.** This project is based in part on Justice Launcher source. The upstream source has no published license and permission is required before redistribution. FireClient does not claim ownership of upstream or third-party work and cannot grant permission on behalf of its authors. Do not redistribute a combined build without the rights required for every component.

Minecraft, Microsoft, Mojang, Fabric, Forge, NeoForge, Modrinth, PaperMC, Discord and other names and marks belong to their owners. FireClient is independent and is not endorsed by Mojang or Microsoft.

## Support

Ask in the [FireClient Discord](https://discord.gg/jK74ZtrDFm). Never post access tokens, account files, private messages or unredacted logs publicly.

## Credits

Created by **FirePDX** and **Sajjad Ahmed**.

<p align="center"><sub>&copy; 2026 FireClient. All rights reserved.</sub></p>
