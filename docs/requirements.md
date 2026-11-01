---
id: requirements
title: System Requirements
sidebar_label: Requirements
---

# System Requirements

FireClient is engineered for minimal idle memory overhead and smooth multi-threaded rendering across **Windows**, **macOS**, and **Linux**.

---

## 💻 Hardware & OS Specifications

| Component | Minimum Requirements | Recommended Specifications |
| :--- | :--- | :--- |
| **Windows** | Windows 10 64-bit (1903+) + WebView2 Runtime | Windows 11 64-bit (22H2+) |
| **macOS** | macOS 12 Monterey (`arm64` Apple Silicon or `x64` Intel) | macOS 14 Sonoma / macOS 15 Sequoia (Apple M1–M4) |
| **Linux** | Ubuntu 20.04+, Debian 11+, Fedora 38+, Arch (`x86_64` / `arm64`, glibc 2.31+) | Modern 64-bit Linux desktop with Mesa 23+ or NVIDIA 535+ |
| **Java Runtime** | Java 8 / 17 / 21 (managed automatically by FireClient) | Bundled Adoptium Temurin 64-bit (`x64` / `aarch64`) |
| **Processor (CPU)** | Intel Core i3-3210 / AMD A8-7600 / Apple M1 | Intel Core i5-10400 / AMD Ryzen 5 3600 / Apple M1 Pro+ |
| **Memory (RAM)** | 4 GB system RAM (2 GB allocated to Minecraft) | 8 GB–16 GB+ system RAM (4 GB allocated to Minecraft) |
| **Graphics (GPU)** | Intel HD 4000 / AMD Radeon R5 / Apple GPU (OpenGL 3.2–4.4+) | NVIDIA GeForce GTX 1060 / AMD Radeon RX 580 / Apple M-series |
| **Storage** | 1.5 GB free storage | 4 GB+ NVMe / SATA SSD |

---

## ☕ Automatic Java Compatibility Matrix

FireClient automatically downloads and isolates the exact 64-bit **Eclipse Adoptium Temurin** JDK required for each Minecraft version inside `~/.fireclient/java` (`%USERPROFILE%\.fireclient\java` on Windows):

| Minecraft Version | Required Java Version | Architecture |
| :--- | :--- | :--- |
| **1.20.5 – 1.21.4+** | **Java 21** | Native `x64` or `aarch64` (Apple Silicon / ARM64) |
| **1.18 – 1.20.4** | **Java 17** | Native `x64` or `aarch64` |
| **1.8.9 – 1.16.5** | **Java 8 / Java 17** | Native `x64` (or `aarch64` with LWJGL natives) |

* If you use the **FireClient Mod JAR** manually inside a third-party launcher (Prism, MultiMC, or Vanilla), ensure your profile selects a 64-bit **Java 21** runtime for Minecraft 1.20.5+.
