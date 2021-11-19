module.exports = {
    testEnvironment: "jsdom",
    moduleNameMapper: {
        "\\.(jpg|jpeg|png|svg|woff|woff2)$": "<rootDir>/src/__mocks__/fileMock.ts",
        "\\.css$": "<rootDir>/src/__mocks__/styleMock.ts",
    },
    setupFilesAfterEnv: ["<rootDir>/src/setupTests.ts"],
    verbose: true,
};
