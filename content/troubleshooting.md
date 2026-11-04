---
title: Troubleshooting
description: Fixes for common FireClient problems, including SmartScreen warnings, the Right Shift menu not opening, a version that will not launch and friends who cannot join your server.
group: Reference
order: 23
---
## Windows warns about the installer

The installer is unsigned, so SmartScreen may warn. Download only from official places and [check the hash](verify-download.md).

## Right Shift does nothing

The menu only exists for Minecraft 1.21.1 on Fabric. Check your version on the Versions page and relaunch.

## The game will not launch

1. Open the live console and read the last error.
2. Try a fresh profile with no mods.
3. Switch mods off one by one on the Library page.
4. Use the built-in crash reporter, added in 1.1, for an auto-fix.

## A mod does not load

Check that its Minecraft version and loader match your profile.

## HUD layout resets

Check that `config/fireclient/client.json` is not read-only. See [Files and folders](files-folders.md).

## Friends cannot join my server

The launcher does not forward ports. See [Servers and hosting](servers.md).

## Still stuck

Ask in the [Discord](community.md).

> **Warning:** Do not post access tokens, account files, private messages or unredacted logs in public.
