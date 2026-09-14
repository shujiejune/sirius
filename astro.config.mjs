// @ts-check

import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import { defineConfig } from "astro/config";

import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  site: "https://jieniu.jetzt",
  integrations: [mdx(), sitemap()],

  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    shikiConfig: {
      // Choose your preferred dark theme
      // Popular options: 'tokyo-night', 'dracula', 'vitesse-dark', 'github-dark', 'kanagawa-wave'
      theme: "kanagawa-wave",
      wrap: true, // Wraps long lines of code
    },
  },
});
