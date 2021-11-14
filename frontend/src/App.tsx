import "./styles/app.css";
import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { HomePage } from "./pages/HomePage";

export const App: React.FC = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route caseSensitive path="/" element={<HomePage />} />
            </Routes>
        </BrowserRouter>
    );
};
