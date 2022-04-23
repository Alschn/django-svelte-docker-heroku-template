import commonjs from "@rollup/plugin-commonjs";
import resolve from "@rollup/plugin-node-resolve";
import path from "path";
import css from "rollup-plugin-css-only";
import livereload from "rollup-plugin-livereload";
import svelte from "rollup-plugin-svelte";
import { terser } from "rollup-plugin-terser";
import preprocess from "svelte-preprocess";

const isDockerized = process.env.DOCKER === "true";

const STATIC_PATH = isDockerized ?
  path.resolve(__dirname, "public") :
  path.resolve(__dirname, "../backend/core/static/frontend");

const production = !process.env.ROLLUP_WATCH;

function serve() {
  let server;

  function toExit() {
    if (server) server.kill(0);
  }

  return {
    writeBundle() {
      if (server) return;
      server = require("child_process").spawn(
        "npm",
        ["run", "start", "--", "--dev"],
        {
          stdio: ["ignore", "inherit", "inherit"],
          shell: true,
        }
      );

      process.on("SIGTERM", toExit);
      process.on("exit", toExit);
    },
  };
}

function componentExportDetails(componentName) {
  return {
    input: `src/main-${componentName.toLowerCase()}.js`,
    output: {
      sourcemap: true,
      format: "iife",
      name: `${componentName.toLowerCase()}`,
      file: `${STATIC_PATH}/${componentName}.js`,
    },
    plugins: [
      svelte({
        compilerOptions: {
          // enable run-time checks when not in production
          dev: !production,
        },
        preprocess: preprocess(),
      }),
      // we'll extract any component CSS out into
      // a separate file - better for performance
      css({output: `${componentName}.css`}),

      // If you have external dependencies installed from
      // npm, you'll most likely need these plugins. In
      // some cases you'll need additional configuration -
      // consult the documentation for details:
      // https://github.com/rollup/plugins/tree/master/packages/commonjs
      resolve({
        browser: true,
        dedupe: ["svelte"],
      }),
      commonjs(),

      // In dev mode, call `npm run start` once
      // the bundle has been generated
      !production && serve(),

      // Watch the `public` directory and refresh the
      // browser on changes when not in production
      !production && livereload("public"),

      // If we're building for production (npm run build
      // instead of npm run dev), minify
      production && terser(),
    ],
    watch: {
      clearScreen: false,
    },
  };
}

let svelte_apps = [];

// register your components like this:
["App", "WithProps"].forEach((d) => svelte_apps.push(componentExportDetails(d)));

// export multiple components at once
export default svelte_apps;
