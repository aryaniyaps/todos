module.exports = {
    content: ["./src/**/*.tsx"],
    theme: {
        fontFamily: {
            sans: ["Inter", "Segoe UI", "Roboto", "sans-serif"],
            mono: ["Menlo", "Monaco", "Courier New", "monospace"],
        },
        fontSize: {
            tiny: "0.625rem",
            xs: ".75rem",
            sm: ".875rem",
            base: "1rem",
            lg: "1.125rem",
            xl: "1.25rem",
            "2xl": "1.5rem",
            "3xl": "1.875rem",
            "4xl": "2.25rem",
            "5xl": "3rem",
            "6xl": "4rem",
            "7xl": "5rem",
        },
        colors: {
            transparent: "transparent",
            "header-text": "var(--color-header-text)",
            floating: "var(--color-floating)",
            primary: {
                100: "var(--color-primary-100)",
                200: "var(--color-primary-200)",
                300: "var(--color-primary-300)",
                400: "var(--color-primary-400)",
                500: "var(--color-primary-500)",
                600: "var(--color-primary-600)",
            },
            accent: {
                DEFAULT: "var(--color-accent)",
                disabled: "var(--color-accent-disabled)",
                hover: "var(--color-accent-hover)",
            },
            danger: {
                DEFAULT: "var(--color-danger)",
                disabled: "var(--color-danger-disabled)",
                hover: "var(--color-danger-hover)",
            },
        },
        extend: {},
    },
    plugins: [],
};
