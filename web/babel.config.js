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
                loose: true,
                targets: packageConfig.browserslist,
                shippedProposals: true,
            },
        ],
        [
            "@babel/preset-react",
            {
                runtime: "automatic",
            },
        ],
    ],
};
