---
title: Offline and online mode
description: Play FireClient with no account in Offline Mode or sign in with Microsoft in Online Mode. How login tokens are stored on Windows, macOS and Linux.
group: Account and safety
order: 16
---
You do not need to sign in to use FireClient.

## Offline Mode

Works with no account at all. You get singleplayer, servers that run in offline mode, and local skins you pick yourself.

## Online Mode

Signs you in with your Microsoft account. You need a real Minecraft Java Edition account. Use it to join servers that check accounts.

## Switching

Switching between the two never touches your worlds, profiles or mods. They live in the same place either way.

## Where your login token goes

The token is stored on your machine only, encrypted with the system store:

- Windows: DPAPI
- macOS: Keychain
- Linux: `libsecret`

> **Warning:** Never share access tokens or account files with anyone, including in Discord help channels.
