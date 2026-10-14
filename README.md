<p align="center">
  <img src="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/assets/logo.png" alt="FireClient" width="140" height="140">
</p>

<h1 align="center">FireClient</h1>

<p align="center"><b>Minecraft, Your Way.</b></p>

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

## Why we made it

We wanted a Minecraft launcher that gets out of your way. Install it, pick a version, and play. No account wall, no pile of bundled junk, and no mystery about where your worlds and settings end up.

FireClient is a launcher and an in-game client in one. It handles the boring parts (Java, versions, mod loaders, updates) and gives you a clean in-game menu once you're in.

It is **not open source**. This repo is the home for the README, the license and the release info. More on that [below](#license).

## Play your way: offline or online

You don't have to sign in to use FireClient.

**Offline Mode** works with no account at all. You get singleplayer, servers that run in offline mode, and local skins you pick yourself.

**Online Mode** signs you in with your Microsoft account. You need a real Minecraft account for this, and it's what you'll use to join servers that check accounts. Your login token is stored on your PC and encrypted with Windows DPAPI.

Switching between them never touches your worlds, profiles or mods. They all live in the same place either way.

## What's in it

**The launcher**
- Installs Minecraft versions and the right Java for each one
- Separate profiles, each with its own version, mods, resource packs and worlds
- Fabric, Forge and NeoForge
- Checks for launcher, version and loader updates
- Discord Rich Presence if you want it (shows your version and server)

**Mods, packs and shaders**
- Search and install from Modrinth without leaving the launcher
- Mod library scan that matches your installed mods to their Modrinth pages
- PaperMC downloads for running a local server

**In-game**
- Fabric and Forge versions of the client mod
- A custom title menu: an icon-button grid along the bottom instead of the vanilla menu
- A HUD and client settings screen

**Community (optional)**
- Profile, friends, messages, server listings and marketplace
- Nothing is sent unless you actually use these

**Your files, your call**
- Everything lives in one `.fireclient` folder on your PC
- Logs and crash logs stay local. The launcher never uploads them
- A copy-diagnostics button for when you need help. You decide where to paste it
- Uninstalling leaves your worlds and game data alone

## What we're working on next

These are planned, not shipped. They'll land in future releases, and the [Releases](https://github.com/untitledinfo/fireclient-launcher/releases) page is where they'll show up first.

- More in-game HUD modules and layout options
- Per-profile performance settings
- Backup and restore for worlds, with one click
- Import profiles from other launchers
- Launcher themes beyond the default red
- More Minecraft versions for both loaders

Got an idea? Drop it in the [Discord](https://discord.gg/jK74ZtrDFm).

## Install

1. Grab [`FireClient-Setup.exe`](https://github.com/untitledinfo/fireclient-launcher/releases/download/v1.0/FireClient-Setup.exe).
2. Run it and read the Terms & Privacy notice.
3. Hit **I Agree** to install.
4. Open FireClient and choose Offline Mode, or sign in for Online Mode.

You need Windows 10 or 11 (64-bit) and an internet connection for game files and updates.

Heads up: Windows SmartScreen might warn you about a new installer. Only download from this page or [fireclient.net](https://fireclient.net), never from re-uploads.

## Privacy

FireClient only talks to a service when you use the feature that needs it.

- **Signing in** goes to Microsoft, Xbox and Minecraft services.
- **Downloads and update checks** go to the provider of whatever you're getting: Mojang/Microsoft, Adoptium, Fabric, Forge, NeoForge, Modrinth, PaperMC, GitHub and their CDNs. They see your IP and normal request info, like any download.
- **Mod library scan** sends file hashes to Modrinth so it can recognise your mods.
- **Community features** connect to justiceclient.org.
- **Discord presence** only goes to your local Discord app.

Back up important worlds before restoring or changing game files. The full terms are in the installer.

## License

FireClient is proprietary and all rights are reserved.

You can download it and use it yourself. You can't publish, sell, sublicense or redistribute FireClient's source, artwork or branding. Full text in [LICENSE](LICENSE).

**A note on upstream code.** Parts of this project are based on Justice Launcher source. That upstream source has no published license, and permission is needed before anyone redistributes it. We don't claim ownership of upstream or third-party work, and we can't grant permission on its authors' behalf. If you're thinking of redistributing a build, make sure you have the rights for every piece in it.

Minecraft, Microsoft, Mojang, Fabric, Forge, NeoForge, Modrinth, PaperMC, Discord and other names and marks belong to their owners. FireClient is independent and isn't endorsed by Mojang or Microsoft.

## Help

Questions or problems? Ask in the [Discord](https://discord.gg/jK74ZtrDFm). Please don't post access tokens, account files, private messages or unredacted logs in public.

## Made by

**FirePDX** and **Sajjad Ahmed**.

<p align="center"><sub>&copy; 2026 FireClient. All rights reserved.</sub></p>
