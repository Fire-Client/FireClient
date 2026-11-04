---
title: Versions, profiles and Java
description: How FireClient installs Minecraft versions, picks the right Java runtime and keeps separate profiles with Fabric, Forge or NeoForge.
group: Launcher
order: 8
---
## Versions

The Versions page installs Minecraft versions. The launcher can start other versions, but the in-game client (menu and HUD) is built for Minecraft 1.21.1 on Fabric. Other versions and loaders get in-game features once a matching mod build exists.

## Loaders

Fabric, Forge and NeoForge are supported by the launcher. The GitHub README says the in-game client runs on Fabric and Forge. The website says 1.21.1 on Fabric only. When in doubt, use 1.21.1 with Fabric.

## Java

You do not need to install Java. The launcher downloads the Adoptium runtime each version needs, either `x64` or native Apple Silicon `aarch64`. Minecraft 1.21.1 uses Java 21.

## Profiles

A profile is a separate setup. Each one has its own version, mods, resource packs and worlds. Use one profile for PvP, one for building and one for testing mods, and nothing leaks between them.

> **Tip:** Make a new profile before you try a big mod pack. If it breaks, delete the profile and your main setup is untouched.
