import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        react({
            babel: {
                presets: [
                    [
                        "@babel/preset-react",
                        {
                            runtime: "automatic",
                            importSource: "@emotion/react",
                        },
                    ],
                ],
                plugins: ["@emotion/babel-plugin"],
            },
        }),
    ],
    server: {
        watch: {
            usePolling: true,
        },
    },
});
