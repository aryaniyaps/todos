import React from "react";
import { NavBar } from "../components/NavBar";

export const BaseLayout: React.FC = (props) => {
    return (
        <div className="flex flex-col h-full w-full bg-primary-800">
            <NavBar />
            <div className="overflow-y-auto">
                <div className="p-4 flex-grow mx-auto w-full flex max-w-7xl">
                    {props.children}
                </div>
            </div>
        </div>
    );
};
