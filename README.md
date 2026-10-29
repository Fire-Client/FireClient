# Assets used by the FireClient site

All paths are relative to the site root. Nothing here is generated at runtime.

| File | Used for | Notes |
|---|---|---|
| `logo.svg` | Header/footer brand mark, SVG favicon | Red flame "F" mark from the project. |
| `icon.png` | PNG favicon, Apple touch icon | 512x512. |
| `ingame-menu.jpg` / `-960.jpg` / `-960.webp` | Hero, home gallery, Screenshots page | FireClient title screen, 1.21.1. Window bar and OS watermark removed. |
| `ingame-hud.jpg` (+ `-960`) | Home gallery, HUD guide, Screenshots page | The in-game FireClient menu (Mods, Settings, Keybinds, Mod List, profiles). |
| `ingame-gameplay.jpg` (+ `-960`) | Home gallery, HUD guide, Screenshots page | HUD elements in a singleplayer world. |
| `launcher-home.jpg` (+ `-960`) | Home gallery, social card, blog covers | Launcher home page. |
| `launcher-mods.jpg` (+ `-960`) | Home gallery, blog covers | Launcher Mods page. |
| `launcher-versions`, `-modrinth`, `-library`, `-resource-packs`, `-shaders`, `-worlds`, `-accounts`, `-skins`, `-usage` | Screenshots page | Launcher pages. `-accounts` has the UUID and a third party's saved account blurred. |
| `og-image.png` | Open Graph / Twitter card | 1200x630. The framed screenshot is `launcher-home.jpg`. |

## Replacing things

- **Screenshots:** before publishing, check each one for personal data: account names, UUIDs, file paths containing a Windows username, IP addresses, third-party logos, and the Windows "Activate Windows" watermark. Export a 1600 px `.jpg`, a 960 px `.jpg` and a 960 px `.webp`. Add the image to `SHOTS` in `lib/render.mjs` (Screenshots page) and its `-960` size to `IMG_DIMS`; the gallery on `index.html` is edited by hand. Declared width/height must match the real file (a test checks this).
- **Fonts:** none are loaded. The site uses system fonts (Bahnschrift / Segoe UI on Windows) so nothing can fail to download.
- **Colors:** every color lives in the `:root` block at the top of `style.css`. `--red`, `--red-hot` and `--red-deep` drive the theme.



