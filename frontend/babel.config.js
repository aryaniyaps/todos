module.exports = {
    sourceMaps: true,
    sourceType: "module",
    retainLines: true,
    presets: [
        "@babel/preset-typescript",
        [
            "@babel/preset-react",
            {
                runtime: "automatic",
                importSource: "@emotion/react",
            },
        ],
    ],
    plugins: ["@emotion/babel-plugin"],
};
