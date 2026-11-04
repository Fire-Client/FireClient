---
title: Is FireClient safe?
description: How to check that a FireClient download is genuine, why Windows shows a SmartScreen warning and what the SHA-256 check does and does not prove.
group: Account and safety
order: 18
---
No installer can be promised to be 100 percent safe, so FireClient does not promise it. Here is what you can check yourself.

## Download from official places

- [fireclient.net](https://www.fireclient.net/)
- [Verified FireClient Releases](https://github.com/untitledinfo/verifed-fireclient/releases)

## Expect a SmartScreen warning

The beta installer is not code-signed yet. Windows may warn about it. Do not click through if you got the file from anywhere else.

## Compare the hash

A matching SHA-256 shows your file is the one that was published. See [Verify the download](verify-download.md). It does not prove the file is free of malware.

## Scan it

Run the file through Windows Security or another scanner if you want a second opinion.

## Read before you pipe

The one-line installers run a script as you. Read the script first. Both are in the releases repository under `scripts/`.

## What FireClient does with your data

See [Privacy](privacy.md). The project also publishes a License and Safety Facts page on its website.
