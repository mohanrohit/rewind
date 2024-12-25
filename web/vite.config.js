import { defineConfig } from "vite";

export default defineConfig({
    root: ".",

    base: "./",

    build: {
        outDir: "./public", // relative to root

        sourcemap: true,
        manifest: true,
        emptyOutDir: false, // there are other things besides
        // the assets in the outdir

        rollupOptions: {
            input: {
                main: "./main.js",
            },
        }
    },

    server: {
        watch: {
            // Include the app/components folder for live updates
            ignored: ["!**/app/components/**"],
        },
    },
});
