<p align="center">
  <img src="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/logo.png" alt="FireClient" width="140" height="140">
</p>

<h1 align="center">FireClient</h1>

<p align="center"><b>Minecraft, Your Way.</b></p>











<p align="center">
  <a href="https://github.com/untitledinfo/verifed-fireclient/releases/"><img src="https://img.shields.io/badge/Download%20for%20Windows-Verified%20Releases-E11D2E?style=for-the-badge" alt="Download FireClient for Windows"></a>
</p>

<p align="center">
  <a href="https://github.com/untitledinfo/verifed-fireclient/releases/"><img src="https://img.shields.io/github/downloads/untitledinfo/verifed-fireclient/total?style=flat-square&amp;color=E11D2E&amp;label=total%20downloads" alt="Total downloads"></a>
  <a href="https://github.com/untitledinfo/verifed-fireclient/releases/tag/v1.0.10"><img src="https://img.shields.io/github/downloads/untitledinfo/verifed-fireclient/v1.0.10/FireClient-Setup.exe?style=flat-square&amp;color=E11D2E&amp;label=v1.0.10%20installer" alt="v1.0.10 installer downloads"></a>
  <a href="https://github.com/untitledinfo/verifed-fireclient/releases/latest"><img src="https://img.shields.io/github/v/release/untitledinfo/verifed-fireclient?style=flat-square&amp;color=E11D2E&amp;label=latest" alt="Latest release"></a>
  <a href="https://discord.gg/jK74ZtrDFm"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdiscord.com%2Fapi%2Fv10%2Finvites%2FjK74ZtrDFm%3Fwith_counts%3Dtrue&amp;query=%24.approximate_member_count&amp;label=Discord%20members&amp;logo=discord&amp;logoColor=white&amp;color=5865F2&amp;style=flat-square" alt="Discord total members"></a>
  <img src="https://img.shields.io/badge/platform-Windows-1f1f23?style=flat-square" alt="Windows">
  <img src="https://img.shields.io/badge/license-proprietary-1f1f23?style=flat-square" alt="Proprietary license">
</p>

<p align="center">
  <a href="https://fireclient.net">Website</a> &nbsp;|&nbsp;
  <a href="https://github.com/untitledinfo/verifed-fireclient/releases/">Verified Releases</a> &nbsp;|&nbsp;
  <a href="https://discord.gg/jK74ZtrDFm">Discord</a> &nbsp;|&nbsp;
  <a href="LICENSE">License</a>
</p>

---

## Why we made it

We wanted a Minecraft launcher that gets out of your way. Install it, pick a version, and play. No account wall, no pile of bundled junk, and no mystery about where your worlds and settings end up.

FireClient is a launcher and an in-game client in one. It handles the boring parts (Java, versions, mod loaders, updates) and gives you a clean in-game menu once you're in. It's a Windows beta, so expect it to keep changing.

It is **not open source**. This repository contains the README and license information. Downloadable builds are published separately on the [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases/) page. More on the license [below](#license).

## Screenshots

**The launcher.** Home screen with your account, version, loader and memory, plus quick links and a live look at the FireClient Discord.

<p align="center">
  <a href="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/screenshot-launcher-home.jpg"><img src="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/screenshot-launcher-home.jpg" alt="Launcher home" width="860"></a>
</p>

**Mods.** Search Modrinth, install in one click, jump to your folders, or grab a curated pack.

<p align="center">
  <a href="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/screenshot-launcher-mods.jpg"><img src="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/screenshot-launcher-mods.jpg" alt="Launcher mods page" width="860"></a>
</p>

**The in-game menu.** The FireClient title screen, running on Minecraft 1.21.1 with Fabric.

<p align="center">
  <a href="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/screenshot-ingame-menu.jpg"><img src="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/screenshot-ingame-menu.jpg" alt="FireClient in-game title screen" width="860"></a>
</p>

**HUD settings.** Turn each HUD element on or off, then drag them where you want them.

<p align="center">
  <a href="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/screenshot-ingame-hud.jpg"><img src="https://raw.githubusercontent.com/Fire-Client/Fireclient/main/screenshot-ingame-hud.jpg" alt="FireClient HUD settings" width="860"></a>
</p>

<sub>Click any screenshot to see it full size.</sub>

## Play your way: offline or online

You don't have to sign in to use FireClient.

**Offline Mode** works with no account at all. You get singleplayer, servers that run in offline mode, and local skins you pick yourself.

**Online Mode** signs you in with your Microsoft account. You need a real Minecraft account for this, and it's what you'll use to join servers that check accounts. Your login token is stored on your PC and encrypted with Windows DPAPI.

Switching between them never touches your worlds, profiles or mods. They all live in the same place either way.

## What's in it

**The launcher**
- Home, Versions, Worlds, Servers, Screenshots, Accounts and Skins pages in one sidebar
- Installs Minecraft versions and the right Java for each one
- Separate profiles, each with its own version, mods, resource packs and worlds
- Fabric, Forge and NeoForge
- A live console that shows install and launch progress, game output and errors as they happen
- A Performance page and a Usage page
- Host Server page for running a local server (PaperMC)
- Live FireClient Discord member count, with join and copy-invite buttons
- Favorite servers: star up to 10 on the Servers page and they show on Home
- Discord Rich Presence if you want it (shows your version and server)

**Mods, packs and shaders**
- Search and install from Modrinth without leaving the launcher
- Drag and drop `.jar` mod files to install them
- Curated one-click packs: Performance, Visuals, Utility and PvP
- Toggle or remove installed mods from the same page
- Resource Packs and Shaders pages
- Mod library scan that matches your installed mods to their Modrinth pages
- Quick-access buttons for your instance, mods, screenshots, saves and shaders folders

**In-game (Fabric, shown on 1.21.1)**
- A custom FireClient title screen and FireClient Menu button
- HUD elements you can switch on or off: watermark, FPS, ping, coordinates, direction, memory, clock, keystrokes, armor, effects and CPS
- Edit HUD positions to put everything where you want it
- Settings tabs for HUD, Features, Theme and About

**Community (optional)**
- Profile, friends, messages, server listings and marketplace
- Nothing is sent unless you actually use these

**Your files, your call**
- Everything lives in one `.fireclient` folder on your PC
- Logs and crash logs stay local. The launcher never uploads them
- A copy-diagnostics button for when you need help. You decide where to paste it
- Uninstalling leaves your worlds and game data alone

## What we're working on next

These are planned, not shipped. The [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases/) page is where updates will be published first.

- More in-game HUD modules and layout options
- Backup and restore for worlds, with one click
- Import profiles from other launchers
- More Minecraft versions for the in-game client

Got an idea? Drop it in the [Discord](https://discord.gg/jK74ZtrDFm).

## Install

Download the latest Windows installer from the [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases/) page.

1. Open the downloaded installer and read the Terms & Privacy notice.
2. Hit **I Agree** to install.
3. Open FireClient and choose Offline Mode, or sign in for Online Mode.

You need Windows 10 or 11 (64-bit) and an internet connection for game files and updates.

Heads up: Windows SmartScreen might warn you about a new installer. Only download from the [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases/) page or [fireclient.net](https://fireclient.net), never from re-uploads.

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
