---
title: Verify the download
description: Check the SHA-256 hash of the FireClient installer with PowerShell, macOS or Linux before you run it.
group: Get started
order: 5
---
Checking the hash is optional. It tells you whether the file on your disk is the one that was published.

## Windows

Open PowerShell in the folder with the file:

```powershell
Get-FileHash .\FireClient-Setup.exe -Algorithm SHA256
```

## macOS and Linux

```bash
shasum -a 256 FireClient-macOS-universal.dmg
sha256sum FireClient-Linux-x86_64.AppImage
```

## Compare

Match the result with the SHA-256 shown on the [download page](https://www.fireclient.net/download/). The page only shows one when GitHub publishes it.

## What a match means

A match means the file is the one that was published. It does not prove the file is free of malware. Scan it with your usual security tool if you want another opinion.

The launcher's [updater](updater.md) also checks SHA-256 hashes when it installs updates.
