// @ts-check

import { satteri } from "@astrojs/markdown-satteri";
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
    // Smart punctuation is on by default; keep dashes/ellipses but stop
    // converting straight quotes ("...") into curly quotes (“...”).
    processor: satteri({ features: { smartPunctuation: { quotes: false } } }),
    shikiConfig: {
      // Choose your preferred dark theme
      // Popular options: 'tokyo-night', 'dracula', 'vitesse-dark', 'github-dark', 'kanagawa-wave'
      theme: "kanagawa-wave",
      wrap: true, // Wraps long lines of code
    },
  },
});
