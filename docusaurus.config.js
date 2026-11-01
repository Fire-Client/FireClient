// @ts-check
import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'FireClient Docs',
  tagline: 'Fast, lightweight Minecraft Java launcher and in-game client for Windows, macOS, and Linux.',
  favicon: 'img/logo.svg',

  url: 'https://docs.fireclient.net',
  baseUrl: '/',

  organizationName: 'Fire-Client',
  projectName: 'FireClient',

  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: 'docs',
          editUrl: 'https://github.com/Fire-Client/FireClient/tree/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'FireClient Docs',
        logo: {
          alt: 'FireClient Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'docsSidebar',
            position: 'left',
            label: 'Documentation',
          },
          {
            to: '/docs/windows',
            label: 'Windows',
            position: 'left',
          },
          {
            to: '/docs/macos',
            label: 'macOS',
            position: 'left',
          },
          {
            to: '/docs/linux',
            label: 'Linux',
            position: 'left',
          },
          {
            to: '/docs/github-install',
            label: 'Build & Releases',
            position: 'left',
          },
          {
            href: 'https://fireclient.net',
            label: 'Official Site',
            position: 'right',
          },
          {
            href: 'https://github.com/untitledinfo/verifed-fireclient/releases',
            label: 'Releases',
            position: 'right',
          },
          {
            href: 'https://github.com/Fire-Client/FireClient',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Installation',
            items: [
              { label: 'Overview', to: '/docs/' },
              { label: 'Windows Setup (.exe / .zip)', to: '/docs/windows' },
              { label: 'macOS Setup (.dmg)', to: '/docs/macos' },
              { label: 'Linux Setup (.AppImage / .deb)', to: '/docs/linux' },
              { label: 'Multi-Platform Guide', to: '/docs/installation' },
            ],
          },
          {
            title: 'Resources',
            items: [
              { label: 'System Requirements', to: '/docs/requirements' },
              { label: 'Architecture & Build', to: '/docs/github-install' },
              { label: 'Troubleshooting & FAQ', to: '/docs/troubleshooting' },
            ],
          },
          {
            title: 'Community',
            items: [
              { label: 'Website', href: 'https://fireclient.net' },
              { label: 'Verified Releases', href: 'https://github.com/untitledinfo/verifed-fireclient/releases' },
              { label: 'Discord', href: 'https://discord.gg/jK74ZtrDFm' },
              { label: 'Modrinth', href: 'https://modrinth.com/mod/fireclient' },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} FireClient. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['powershell', 'bash', 'java', 'gradle', 'json'],
      },
    }),
};

export default config;
