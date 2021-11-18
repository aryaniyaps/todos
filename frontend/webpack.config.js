const path = require("path");
const HTMLWebpackPlugin = require("html-webpack-plugin");

// path configuration
const staticPath = path.resolve(__dirname, "public");
const appHTML = path.resolve(__dirname, "index.html");
const outputPath = path.resolve(__dirname, "dist");

module.exports = function (env) {
    const __prod__ = env == "production";

    return {
        mode: __prod__ ? "production" : "development",
        entry: "./src/index",
        output: {
            path: outputPath,
            filename: "bundle.js",
            clean: __prod__,
        },
        stats: "minimal",
        resolve: {
            extensions: [".ts", ".tsx", ".js", ".jsx", ".json"],
        },
        devServer: {
            client: {
                overlay: true,
                progress: true,
            },
            static: {
                directory: staticPath,
            },
            compress: true,
            port: 3000,
        },
        plugins: [
            new HTMLWebpackPlugin({
                template: appHTML,
            }),
        ],
        module: {
            rules: [
                {
                    test: /\.tsx?$/,
                    exclude: [/\.test.tsx?$/],
                    use: ["babel-loader", "ts-loader"],
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
};
