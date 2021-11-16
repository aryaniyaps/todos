var path = require("path");

module.exports = {
    // Change to your "entry-point".
    entry: "./src/index",
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "bundle.js",
    },
    resolve: {
        extensions: [".ts", ".tsx", ".js", ".json"],
    },
    devServer: {
        static: {
            directory: path.resolve(__dirname, "public"),
        },
        compress: true,
        port: 3000,
    },
    module: {
        rules: [
            {
                test: /\.(ts|js)x?$/,
                exclude: /node_modules/,
                loader: "babel-loader",
            },

            {
                test: /\.(scss|sass|css)$/,
                exclude: /node_modules/,
                use: [
                    // Translates CSS into CommonJS
                    "css-loader",
                ],
            },
            {
                test: /\.svg$/,
                loader: "svg-inline-loader",
            },
        ],
    },
};
