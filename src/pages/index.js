import React, { useState } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

const VERIFIED_RELEASE_BASE = 'https://github.com/untitledinfo/verifed-fireclient/releases/latest/download';
const RAW_SCRIPT_BASE = 'https://raw.githubusercontent.com/untitledinfo/verifed-fireclient/main/scripts';

const PlatformCards = [
  {
    title: '🪟 Windows 10 / 11',
    tag: 'x64 • Native C++20',
    description:
      'Ultra-lightweight WebView2 native desktop host with Authenticode verification, SHA-256 auto-updater, and portable ZIP option.',
    primaryLabel: 'Download .exe',
    primaryHref: `${VERIFIED_RELEASE_BASE}/FireClient-Setup.exe`,
    guideTo: '/docs/windows',
  },
  {
    title: '🍎 macOS 12+',
    tag: 'Apple Silicon & Intel',
    description:
      'Universal, arm64 (M1–M4), and Intel x64 DMG packages with native Adoptium aarch64 Java 21 and macOS Keychain encryption.',
    primaryLabel: 'Download .dmg',
    primaryHref: `${VERIFIED_RELEASE_BASE}/FireClient-macOS-universal.dmg`,
    guideTo: '/docs/macos',
  },
  {
    title: '🐧 Linux (64-bit)',
    tag: 'AppImage • .deb • .tar.gz',
    description:
      'Ready for Ubuntu, Debian, Fedora, Arch, Mint, and SteamOS with libsecret token storage and automatic desktop integration.',
    primaryLabel: 'Download .AppImage',
    primaryHref: `${VERIFIED_RELEASE_BASE}/FireClient-Linux-x86_64.AppImage`,
    guideTo: '/docs/linux',
  },
];

const QuickStartCommands = {
  windows: {
    label: 'Windows (PowerShell)',
    shellTitle: 'PowerShell — Verified 1-Line Install',
    oneLiner: `irm ${RAW_SCRIPT_BASE}/install-windows.ps1 | iex`,
    snippet: `# Option A: Official 1-line verified installer (checks SHA-256 + Authenticode)
irm ${RAW_SCRIPT_BASE}/install-windows.ps1 | iex

# Option B: Manual download & SHA-256 verification
Invoke-WebRequest -Uri "${VERIFIED_RELEASE_BASE}/FireClient-Setup.exe" -OutFile "$HOME\\Downloads\\FireClient-Setup.exe"
Get-FileHash -Path "$HOME\\Downloads\\FireClient-Setup.exe" -Algorithm SHA256
Start-Process "$HOME\\Downloads\\FireClient-Setup.exe"`,
  },
  macos: {
    label: 'macOS (Terminal)',
    shellTitle: 'zsh / bash — Apple Silicon & Intel',
    oneLiner: `curl -fsSL ${RAW_SCRIPT_BASE}/install-macos.sh | bash`,
    snippet: `# Option A: Official 1-line macOS installer (verifies SHA-256 & installs to /Applications)
curl -fsSL ${RAW_SCRIPT_BASE}/install-macos.sh | bash

# Option B: Manual Universal DMG download & checksum verification
curl -fL "${VERIFIED_RELEASE_BASE}/FireClient-macOS-universal.dmg" -o ~/Downloads/FireClient-macOS-universal.dmg
shasum -a 256 ~/Downloads/FireClient-macOS-universal.dmg
open ~/Downloads/FireClient-macOS-universal.dmg`,
  },
  linux: {
    label: 'Linux (Bash)',
    shellTitle: 'bash — Ubuntu / Debian / Fedora / Arch',
    oneLiner: `curl -fsSL ${RAW_SCRIPT_BASE}/install-linux.sh | bash`,
    snippet: `# Option A: Official 1-line Linux installer (.deb on Debian/Ubuntu, .AppImage elsewhere)
curl -fsSL ${RAW_SCRIPT_BASE}/install-linux.sh | bash

# Option B: Universal AppImage
curl -fL "${VERIFIED_RELEASE_BASE}/FireClient-Linux-x86_64.AppImage" -o ~/Downloads/FireClient-Linux-x86_64.AppImage
chmod +x ~/Downloads/FireClient-Linux-x86_64.AppImage
~/Downloads/FireClient-Linux-x86_64.AppImage`,
  },
};

function HeroSection() {
  return (
    <header className={clsx('hero hero--dark', styles.heroBanner)}>
      <div className="container">
        <div className={styles.badge}>
          <span>🔥 FireClient • Windows, macOS &amp; Linux</span>
        </div>
        <h1 className={styles.heroTitle}>
          Next-Generation Minecraft <br />
          <span className={styles.gradientText}>Client &amp; Launcher</span>
        </h1>
        <p className={styles.heroSubtitle}>
          A fast, lightweight Minecraft Java launcher and bundled in-game client engineered
          for peak FPS, draggable HUD widgets, local PaperMC server hosting, and one-click Modrinth mods.
        </p>

        <div className={styles.buttons}>
          <Link className="button button--primary button--lg" to="/docs/windows">
            Windows (.exe)
          </Link>
          <Link className="button button--secondary button--lg" to="/docs/macos">
            macOS (.dmg)
          </Link>
          <Link className="button button--secondary button--lg" to="/docs/linux">
            Linux (.AppImage / .deb)
          </Link>
          <Link
            className="button button--outline button--lg"
            href="https://github.com/untitledinfo/verifed-fireclient/releases">
            Verified Releases
          </Link>
        </div>
      </div>
    </header>
  );
}

function PlatformDownloadsSection() {
  return (
    <section className={styles.platformSection}>
      <div className="container">
        <div className={styles.platformGrid}>
          {PlatformCards.map((card) => (
            <article key={card.title} className={styles.platformCard}>
              <div className={styles.platformHeader}>
                <h2 className={styles.platformTitle}>{card.title}</h2>
                <span className={styles.platformTag}>{card.tag}</span>
              </div>
              <p className={styles.platformDesc}>{card.description}</p>
              <div className={styles.platformActions}>
                <Link className="button button--primary button--sm" href={card.primaryHref}>
                  {card.primaryLabel}
                </Link>
                <Link className="button button--secondary button--sm" to={card.guideTo}>
                  Setup Guide
                </Link>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

const FeatureList = [
  {
    title: '⚡ Lightning Fast & Lightweight',
    description:
      'Built from the ground up for minimal memory overhead, automatic Java 8/17/21 isolation, and instant profile launches.',
  },
  {
    title: '🎨 Modular Draggable HUD',
    description:
      'In-game HUD editor accessible via Right Shift. Position FPS, CPS, Ping, Armor Status, Keystrokes, and Coordinates anywhere.',
  },
  {
    title: '📦 Modrinth & Server Hosting',
    description:
      'Install Fabric, Forge, and NeoForge mods, shaders, and resource packs in one click, or host local PaperMC servers directly in-app.',
  },
  {
    title: '🛡️ Safe & OS-Encrypted Auth',
    description:
      'Play Offline or sign in with Microsoft OAuth 2.0. Tokens stay encrypted via Windows DPAPI, macOS Keychain, or Linux libsecret.',
  },
  {
    title: '🔄 Verified SHA-256 Updater',
    description:
      'Redesigned glassmorphic updater verifies cryptographic SHA-256 hashes and release notes before applying updates across platforms.',
  },
  {
    title: '🚀 True Cross-Platform Support',
    description:
      'First-class installers and 1-line terminal scripts for Windows 10/11, macOS 12+ (Apple Silicon & Intel), and 64-bit Linux.',
  },
];

function Feature({ title, description }) {
  return (
    <div className={clsx('col col--4', styles.featureCol)}>
      <div className={styles.featureCard}>
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

function FeaturesSection() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

function MultiPlatformQuickStart() {
  const [activeOs, setActiveOs] = useState('windows');
  const [copied, setCopied] = useState(false);
  const current = QuickStartCommands[activeOs];

  const handleCopy = () => {
    if (typeof navigator !== 'undefined' && navigator.clipboard) {
      navigator.clipboard.writeText(current.oneLiner).then(() => {
        setCopied(true);
        setTimeout(() => setCopied(false), 1800);
      });
    }
  };

  return (
    <section className={styles.quickStartSection}>
      <div className="container">
        <div className={styles.terminalBox}>
          <div className={styles.terminalHeader}>
            <div className={styles.dotsGroup} aria-hidden="true">
              <span className={styles.dot}></span>
              <span className={styles.dot}></span>
              <span className={styles.dot}></span>
            </div>
            <div className={styles.osTabs} role="tablist" aria-label="Select operating system">
              {Object.entries(QuickStartCommands).map(([key, item]) => (
                <button
                  key={key}
                  type="button"
                  role="tab"
                  id={`quickstart-tab-${key}`}
                  aria-selected={activeOs === key}
                  aria-controls={`quickstart-panel-${key}`}
                  className={clsx(styles.osTab, activeOs === key && styles.osTabActive)}
                  onClick={() => {
                    setActiveOs(key);
                    setCopied(false);
                  }}>
                  {item.label}
                </button>
              ))}
            </div>
            <div className={styles.terminalMeta}>
              <span className={styles.terminalTitle}>{current.shellTitle}</span>
              <button type="button" className={styles.copyBtn} onClick={handleCopy}>
                {copied ? 'Copied 1-Liner!' : 'Copy 1-Liner'}
              </button>
            </div>
          </div>
          <div
            role="tabpanel"
            id={`quickstart-panel-${activeOs}`}
            aria-labelledby={`quickstart-tab-${activeOs}`}>
            <pre className={styles.codeBlock}>
              <code>{current.snippet}</code>
            </pre>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title} - Official Multi-Platform Docs`}
      description="Official Windows, macOS, and Linux installation guides and documentation for FireClient.">
      <HeroSection />
      <main>
        <PlatformDownloadsSection />
        <FeaturesSection />
        <MultiPlatformQuickStart />
      </main>
    </Layout>
  );
}
