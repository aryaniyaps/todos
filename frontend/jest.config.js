module.exports = {
    verbose: true,
    testEnvironment: "jsdom",
    testMatch: ["**/tests/**/*.[jt]s?(x)", "**/?(*.)+(spec|test).[jt]s?(x)"],
    moduleNameMapper: {
        "\\.(jpg|jpeg|png|svg|woff|woff2)$": "<rootDir>/src/mocks/fileMock.ts",
        "\\.css$": "<rootDir>/src/mocks/styleMock.ts",
    },
    setupFilesAfterEnv: ["<rootDir>/jest.setup.js"],
};
