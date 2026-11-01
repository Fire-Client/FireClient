// @ts-check
import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'FireClient Docs',
  tagline: 'Fast, lightweight Minecraft Java launcher and in-game Fabric client.',
  favicon: 'img/logo.svg',

  url: 'https://docs.fireclient.net',
  baseUrl: '/',

  organizationName: 'Fire-Client',
  projectName: 'FireClient',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

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
          editUrl: 'https://github.com/Fire-Client/FireClient/tree/main/docs/',
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
            label: 'Windows Install',
            position: 'left',
          },
          {
            to: '/docs/github-install',
            label: 'GitHub & Build',
            position: 'left',
          },
          {
            href: 'https://fireclient.net',
            label: 'Official Site',
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
            title: 'Docs',
            items: [
              { label: 'Introduction', to: '/docs/' },
              { label: 'Windows Setup', to: '/docs/windows' },
              { label: 'Full Installation', to: '/docs/installation' },
              { label: 'GitHub Build', to: '/docs/github-install' },
            ],
          },
          {
            title: 'Community',
            items: [
              { label: 'Website', href: 'https://fireclient.net' },
              { label: 'GitHub Releases', href: 'https://github.com/untitledinfo/verifed-fireclient/releases' },
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
