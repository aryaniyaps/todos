const packageConfig = require("./package");

module.exports = {
    sourceMaps: true,
    sourceType: "module",
    retainLines: true,
    presets: [
        "@babel/preset-typescript",
        [
            "@babel/preset-env",
            {
                useBuiltIns: "usage",
                corejs: 3.18,
                targets: packageConfig.browserslist,
                shippedProposals: true,
            },
        ],
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
