# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project Overview

**Sirius** is a personal blog + portfolio site built with [Astro 7](https://astro.build), deployed to GitHub Pages at `https://shujiejune.github.io/sirius/`. The site is statically generated (no SSR/framework runtime). Content is written in Markdown/MDX.

## Tooling

- **Package manager: pnpm** (do not use npm, yarn, or bun). The lockfile is `pnpm-lock.yaml` — commit changes to it whenever dependencies change.
- Node.js ≥ 22.12 (required by Astro 7).

## Commands

```sh
pnpm install          # install dependencies
pnpm dev              # local dev server at localhost:4321
pnpm build            # production build to ./dist/
pnpm preview          # preview the production build locally
pnpm astro <command>  # Astro CLI (e.g. pnpm astro check)
```

## Architecture

- `astro.config.mjs` — site config. Note `site` and `base: "/sirius"`; all internal links must respect the base path. Integrations: MDX, sitemap. Tailwind CSS v4 is wired in through the Vite plugin (`@tailwindcss/vite`), not a PostCSS config.
- `src/pages/` — file-based routing (`index.astro`, `about.astro`, `projects.astro`, `rss.xml.js`).
- `src/content/` — blog content collections; schema defined in `src/content.config.ts`.
- `src/layouts/` — `Layout.astro` (base HTML), `BlogPost.astro` (post page with Table of Contents), `Portfolio.astro`.
- `src/components/` — Astro components (header, footer, `TableOfContents`, language toggle, etc.).
- `src/styles/global.css` — Tailwind v4 entry (uses `@import "tailwindcss"` syntax, not the legacy `@tailwind` directives).
- `src/utils/` — helpers such as `formatDate.js` and `wordCount.js` (word count supports CJK characters).
- `src/assets/` — fonts and images colocated with source; referenced via Astro's asset pipeline, not `public/`.
- `public/` — static files served as-is at the site root.

## Conventions

- No UI framework (React/Vue/Svelte) — plain `.astro` components plus Tailwind.
- Markdown code blocks are highlighted with Shiki, theme `tokyo-night` (configured in `astro.config.mjs`).
- TypeScript is checked with `// @ts-check` in `.mjs` configs; `tsconfig.json` extends `astro/tsconfigs/strict`.

## Deployment

GitHub Actions workflow at `.github/workflows/deploy.yml` builds with pnpm and deploys `./dist/` to GitHub Pages on every push to `main`. Verify `pnpm build` passes locally before pushing.
