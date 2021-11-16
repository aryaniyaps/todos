import React from "react";
import { NavBar } from "../components/NavBar";

export const BaseLayout: React.FC = (props) => {
    return (
        <div
            css={{
                display: "flex",
                flexDirection: "column",
                height: "100%",
                width: "100%",
                background: "black",
            }}
        >
            <NavBar />
            <div css={{ overflowY: "auto", display: "flex" }} className="flex-grow">
                <div
                    css={{ display: "flex" }}
                    className="p-4 flex-grow mx-auto max-w-7xl"
                >
                    {props.children}
                </div>
            </div>
        </div>
    );
};
