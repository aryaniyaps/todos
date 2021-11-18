module.exports = {
    testEnvironment: "jsdom",
    moduleNameMapper: {
        "\\.(jpg|jpeg|png|svg|woff|woff2)$": "<rootDir>/src/__mocks__/fileMock.ts",
        "\\.css$": "<rootDir>/src/__mocks__/styleMock.ts",
    },
    collectCoverageFrom: ["src/**/*.{js,jsx,ts,tsx}", "!**/*.stories.*"],
    coverageDirectory: "<rootDir>/coverage/",
    setupFilesAfterEnv: ["<rootDir>/src/setupTests.ts"],
    verbose: true,
};
