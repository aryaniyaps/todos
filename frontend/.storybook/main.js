module.exports = {
    core: {
        builder: "webpack5",
    },
    stories: ["../src/**/*.stories.@(ts|tsx)"],
    addons: ["@storybook/addon-essentials", "@storybook/addon-links"],
};
