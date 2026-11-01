---
id: troubleshooting
title: Troubleshooting & FAQ
sidebar_label: Troubleshooting & FAQ
---

# Troubleshooting & Frequently Asked Questions

This page documents common solutions for setup issues, game crashes, and launcher errors.

---

## 🛑 Common Errors & Solutions

### 1. Game Crashes with "Exit Code: 1"
* **Symptom:** Minecraft closes immediately after clicking Play.
* **Solution:**
  1. Open launcher **Settings** ➔ **Java**.
  2. Verify that **Java 21 64-bit** is selected. Older Java 8 or Java 17 runtimes cannot run Minecraft 1.20.5+.
  3. Update your graphics card drivers (NVIDIA, AMD, or Intel) to support OpenGL 4.4+.

### 2. Windows Defender SmartScreen Alert
* **Symptom:** Windows warns "Windows protected your PC".
* **Solution:**
  1. Click **More info**.
  2. Click **Run anyway**.
  3. Verify the installer's SHA-256 hash using `Get-FileHash .\FireClient-Setup.exe -Algorithm SHA256`.

### 3. In-Game Menu (`Right Shift`) Does Not Open
* **Symptom:** Pressing Right Shift does nothing.
* **Solution:**
  1. Check your Minecraft controls under **Options** ➔ **Controls** ➔ **Key Binds**.
  2. Look for **FireClient: Open Menu** and rebind it to a preferred key (such as `RSHIFT` or `M`).

### 4. Fabric Mixin Conflict Crash
* **Symptom:** Crash log mentions `org.spongepowered.asm.mixin.transformer.throwables.MixinTransformerError`.
* **Solution:**
  1. Check your active mods list.
  2. Disable third-party HUD or custom GUI mods that hook into the same vanilla screens as FireClient.

---

## ❓ Frequently Asked Questions

#### Is FireClient free?
Yes. FireClient is 100% free and open-source under the GPL-3.0 license.

#### Can I use FireClient on multiplayer servers like Hypixel?
Yes. FireClient is an authorized quality-of-life client. It does not provide illegitimate gameplay advantages (such as fly, speed, or killaura). However, always review server-specific mod rules.
