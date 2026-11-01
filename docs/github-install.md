---
id: github-install
title: GitHub Source & Developer Build
sidebar_label: GitHub Developer Setup
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Full GitHub Installation & Build from Source

This guide covers cloning, building, and running FireClient directly from the GitHub repository.

---

## 1. Toolchain & Prerequisites

Ensure the following dependencies are installed on your workstation:

| Tool | Required Version | Verification Command | Notes |
| :--- | :--- | :--- | :--- |
| **Git** | `2.40+` | `git --version` | Source control |
| **Node.js** | `v20 LTS` or `v22` | `node -v` | Launcher desktop UI & packaging |
| **npm** / **pnpm** | `npm 10+` or `pnpm 9+` | `npm -v` | Package manager |
| **Java JDK** | `Java 21 (Temurin)` | `java -version` | Fabric client compilation & Minecraft runtime |
| **Gradle** | `8.8+` (or `./gradlew`) | `gradle -v` | In-game mod build lifecycle |

---

## 2. Clone the Repository

Clone the project from the official repository:

```bash
# Clone the repository
git clone https://github.com/Fire-Client/FireClient.git

# Enter project root
cd FireClient

# Fetch all branches and submodules (if present)
git submodule update --init --recursive
```

---

## 3. Project Architecture

The repository is organized into two primary components:

```text
FireClient/
├── launcher/                  # Desktop launcher application (Electron / Node.js)
│   ├── src/                   # Main process, renderer, auth flow
│   ├── package.json
│   └── electron-builder.yml   # Windows NSIS installer configuration
├── client-mod/                # In-game Fabric utility client (Java 21)
│   ├── src/main/java/         # Fabric mixins, HUD rendering, Modrinth API
│   ├── build.gradle           # Fabric Loom build configuration
│   └── gradle.properties
└── package.json
```

---

## 4. Building the In-Game Fabric Client

Before bundling the launcher, compile the internal Minecraft client mod:

```bash
cd client-mod

# Generate Fabric Loom sources & mappings
./gradlew genSources

# Compile and package the remapped Fabric jar
./gradlew build
```

The output jar will be located at:
```text
client-mod/build/libs/fireclient-mod-1.21.1.jar
```

To test the in-game client in a local development environment:
```bash
./gradlew runClient
```

---

## 5. Building & Running the Desktop Launcher

Return to the launcher root and install Node dependencies:

```bash
cd ../launcher

# Install dependencies
npm install
```

### Running in Development Mode
Launch the application with live reload enabled:
```bash
npm run dev
```

### Packaging the Full Installer (`FireClient-Setup.exe`)
Compile the renderer, bundle the assets, and generate the Windows NSIS installer:

```bash
# Package production binaries for Windows (x64)
npm run build:win
```

The compiled binaries will be output to:
```text
dist/
├── FireClient-Setup.exe        # Standalone NSIS installer
├── FireClient-portable.exe     # Standalone portable executable
└── win-unpacked/               # Unpacked application folder
```

---

## 6. GitHub Actions CI/CD Pipeline

To automate the compilation and release packaging on your own fork, add `.github/workflows/release.yml`:

```yaml
name: Build & Release FireClient

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  build-client:
    name: Build Fabric Client Mod
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Java 21
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '21'

      - name: Grant Gradlew Permission
        run: chmod +x client-mod/gradlew

      - name: Build Mod with Gradle
        working-directory: ./client-mod
        run: ./gradlew build

      - name: Upload Mod Artifact
        uses: actions/upload-artifact@v4
        with:
          name: client-mod-jar
          path: client-mod/build/libs/*.jar

  build-launcher:
    name: Build Windows Launcher
    needs: build-client
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js 20
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Download Mod Artifact
        uses: actions/download-artifact@v4
        with:
          name: client-mod-jar
          path: launcher/assets/runtime/

      - name: Install Dependencies
        working-directory: ./launcher
        run: npm ci

      - name: Build Windows Installer
        working-directory: ./launcher
        run: npm run build:win

      - name: Compute SHA-256 Checksum
        run: |
          Get-FileHash launcher/dist/FireClient-Setup.exe -Algorithm SHA256 | Out-File checksums.txt

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        if: startsWith(github.ref, 'refs/tags/')
        with:
          files: |
            launcher/dist/FireClient-Setup.exe
            checksums.txt
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
