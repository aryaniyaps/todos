import React from "react";
import "./styles/app.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { HomeContainer } from "./containers/HomeContainer";

export const App: React.FC = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomeContainer />} />
            </Routes>
        </BrowserRouter>
    );
};
