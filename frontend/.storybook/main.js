module.exports = {
    core: {
        builder: "webpack5",
    },
    stories: ["../src/**/*.stories.@(ts|tsx|js|jsx)"],
    addons: ["@storybook/addon-links", "@storybook/addon-essentials"],
};
