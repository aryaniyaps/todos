const path = require("path");
const HTMLWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: "./src/index",
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "bundle.js",
    },
    stats: "minimal",
    resolve: {
        extensions: [".ts", ".tsx", ".js", ".json"],
    },
    devServer: {
        client: {
            overlay: true,
            progress: true,
        },
        static: {
            directory: path.resolve(__dirname, "public"),
        },
        compress: true,
        port: 3000,
    },
    plugins: [
        new HTMLWebpackPlugin({
            template: path.resolve(__dirname, "public/index.html"),
        }),
    ],
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                exclude: [/\.test.tsx?$/],
                user: ["babel-loader", "ts-loader"],
            },
            {
                test: /\.jsx?$/,
                exclude: [/node_modules/, /\.test.jsx?$/],
                use: ["babel-loader"],
            },

            {
                test: /\.css$/,
                exclude: /node_modules/,
                use: ["style-loader", "css-loader"],
            },
            {
                test: /\.svg$/,
                use: ["svg-inline-loader"],
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/i,
                type: "asset/resource",
            },
        ],
    },
};
