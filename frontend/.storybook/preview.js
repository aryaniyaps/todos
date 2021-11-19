import "../src/styles/main.css";

export const parameters = {
    actions: { argTypesRegex: "^on[A-Z].*" },
    controls: {
        matchers: {
            color: /(background|color)$/i,
            date: /Date$/,
        },
    },
    backgrounds: {
        default: "midnight",
        values: [
            {
                name: "midnight",
                value: "#0b0e11",
            },
            {
                name: "lights-off",
                value: "#000",
            },
        ],
    },
};
