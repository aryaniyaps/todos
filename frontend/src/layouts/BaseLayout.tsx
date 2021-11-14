import React from "react";
import { NavBar } from "../components/NavBar";

export const BaseLayout: React.FC = (props) => {
    return (
        <div>
            <NavBar />
            {props.children}
        </div>
    );
};
