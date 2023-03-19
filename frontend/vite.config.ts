import {defineConfig, loadEnv} from 'vite';
import {svelte} from '@sveltejs/vite-plugin-svelte';
import type {UserConfig as VitestUserConfigInterface} from "vitest/config";
import {resolve} from 'path';
import * as fs from 'fs';

function collectEntrypoints(): string[] {
  const entrypoints = new Array<string>();
  const entrypointDir = resolve(__dirname, 'src/entrypoints');
  for (const entrypoint of fs.readdirSync(entrypointDir)) {
    if (entrypoint.endsWith('.ts')) {
      entrypoints.push(
        resolve(entrypointDir, entrypoint)
      );
    }
  }
  return entrypoints;
}

const vitestConfig: VitestUserConfigInterface = {
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: "src/tests/setup.ts",
    include: [
      "./src/tests/*.{spec,test}.{js,mjs,cjs,ts,mts,cts,jsx,tsx}",
    ],
    css: true,
    coverage: {
      provider: "c8",
      reporter: ["html", "lcov", "text"],
      src: ["src"],
      exclude: [
        "**/src/tests/**",
        "**/src/entrypoints/**",
        "**/src/config/**",
        "**/src/vite-env.d.ts"
      ],
      all: true,
    },
  },
};

// https://vitejs.dev/config/

export default ({mode}) => {
  process.env = {...process.env, ...loadEnv(mode, process.cwd())};

  const isDockerized = process.env.DOCKER === "true";
  const backendOutputDir = "../backend/core/static/frontend";
  const boundVolume = "build";
  const outputDir = isDockerized ? boundVolume : backendOutputDir;

  const entrypoints = collectEntrypoints();

  return defineConfig({
    plugins: [svelte()],
    test: vitestConfig.test,
    build: {
      rollupOptions: {
        input: entrypoints,
        output: {
          entryFileNames: '[name].js',
          assetFileNames: '[name].[ext]',
          chunkFileNames: '[name].js',
          dir: outputDir,
        },
      },
      emptyOutDir: true,
    }
  });
}
