---
title: Files and folders
description: Where FireClient keeps your worlds, profiles, mods, logs and HUD settings, including the .fireclient folder and config/fireclient/client.json.
group: Reference
order: 19
---
Everything lives in one `.fireclient` folder in your home directory.

| System | Path |
|---|---|
| Windows | `%USERPROFILE%\.fireclient` |
| macOS and Linux | `~/.fireclient` |

## HUD settings

HUD positions, visibility and the sprint toggle are saved inside the game folder:

```text
config/fireclient/client.json
```

Copy this file to keep your layout.

## Logs

Logs and crash logs stay local. Use the copy-diagnostics button when you need help, and share only what you are happy to share.

## Backups

Copy the `.fireclient` folder, or just your world folders, before big changes.
