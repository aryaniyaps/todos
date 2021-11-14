import React from "react";
import { NavBar } from "../components/NavBar";

interface BaseLayoutProps {}

export const BaseLayout: React.FC<BaseLayoutProps> = () => {
    return (
        <div css={{ background: "black" }}>
            <NavBar />
        </div>
    );
};
