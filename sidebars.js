/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    {
      type: 'doc',
      id: 'index',
      label: 'Overview',
    },
    {
      type: 'doc',
      id: 'requirements',
      label: 'System Requirements',
    },
    {
      type: 'category',
      label: 'Installation',
      collapsed: false,
      items: [
        'windows',
        'macos',
        'linux',
        'installation',
      ],
    },
    {
      type: 'category',
      label: 'Developer & Source',
      collapsed: false,
      items: [
        'github-install',
      ],
    },
    {
      type: 'doc',
      id: 'troubleshooting',
      label: 'Troubleshooting & FAQ',
    },
  ],
};

export default sidebars;
