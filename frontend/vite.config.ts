import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        react({
            babel: {
                presets: [
                    "@babel/preset-typescript",
                    ["@babel/preset-react", { runtime: "automatic" }],
                ],
            },
        }),
    ],
    server: {
        host: "0.0.0.0",
        port: 3000,
        watch: {
            usePolling: true,
        },
    },
});
