import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

function HeroSection() {
  return (
    <header className={clsx('hero hero--dark', styles.heroBanner)}>
      <div className="container">
        <div className={styles.badge}>
          <span>🔥 FireClient 1.21.1 Early Access</span>
        </div>
        <h1 className={styles.heroTitle}>
          Next-Generation Minecraft <br />
          <span className={styles.gradientText}>Client & Launcher</span>
        </h1>
        <p className={styles.heroSubtitle}>
          A modern, lightweight Minecraft Java launcher and bundled Fabric client designed 
          for peak FPS, draggable HUD widgets, and seamless Modrinth integration.
        </p>

        <div className={styles.buttons}>
          <Link
            className="button button--primary button--lg"
            to="/docs/windows">
            Download for Windows (.exe)
          </Link>
          <Link
            className="button button--secondary button--lg"
            to="/docs/installation">
            Full Installation Guide
          </Link>
          <Link
            className="button button--outline button--lg"
            href="https://github.com/Fire-Client/FireClient">
            GitHub Repository
          </Link>
        </div>
      </div>
    </header>
  );
}

const FeatureList = [
  {
    title: '⚡ Lightning Fast & Lightweight',
    description: (
      'Built from the ground up for minimal memory overhead and ultra-fast launch times compared to bloated launchers.'
    ),
  },
  {
    title: '🎨 Modular Draggable HUD',
    description: (
      'In-game HUD editor accessible via Right Shift. Position your FPS, CPS, Armor Status, Keystrokes, and Coordinates anywhere.'
    ),
  },
  {
    title: '📦 Modrinth Ecosystem',
    description: (
      'Browse, install, and update Fabric mods directly inside the launcher without manual web browsing or folder management.'
    ),
  },
  {
    title: '🛡️ Safe & Zero Telemetry',
    description: (
      'Official Microsoft OAuth 2.0 authentication. Sensitive tokens are encrypted using Windows DPAPI. Zero trackers.'
    ),
  },
  {
    title: '💻 Full GitHub Build Toolchain',
    description: (
      '100% open-source under GPL-3.0. Clone, build from source using Gradle and Fabric Loom, and automate builds via CI/CD.'
    ),
  },
  {
    title: '🚀 Multi-Platform Ready',
    description: (
      'First-class support for Windows 10/11 (64-bit) with companion packaging for Linux AppImages and macOS.'
    ),
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

function WindowsQuickStart() {
  return (
    <section className={styles.quickStartSection}>
      <div className="container">
        <div className={styles.terminalBox}>
          <div className={styles.terminalHeader}>
            <span className={styles.dot}></span>
            <span className={styles.dot}></span>
            <span className={styles.dot}></span>
            <span className={styles.terminalTitle}>PowerShell - Quick Verify & Install</span>
          </div>
          <pre className={styles.codeBlock}>
            <code>
{`# 1. Download official release installer
Invoke-WebRequest -Uri "https://github.com/Fire-Client/FireClient/releases/latest/download/FireClient-Setup.exe" -OutFile "$HOME\\Downloads\\FireClient-Setup.exe"

# 2. Verify SHA-256 integrity
Get-FileHash -Path "$HOME\\Downloads\\FireClient-Setup.exe" -Algorithm SHA256

# 3. Launch the installer
Start-Process "$HOME\\Downloads\\FireClient-Setup.exe"`}
            </code>
          </pre>
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title} - Official Docs`}
      description="Documentation, installation guides, and source builds for FireClient.">
      <HeroSection />
      <main>
        <FeaturesSection />
        <WindowsQuickStart />
      </main>
    </Layout>
  );
}
