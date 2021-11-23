import React from "react";
import { NavBar } from "../components/NavBar";
import { BaseLayout } from "./BaseLayout";

export const AppLayout: React.FC = (props) => {
    return (
        <BaseLayout>
            <NavBar />
            <div className="overflow-y-auto">
                <div className="p-4 flex-grow mx-auto flex max-w-7xl">
                    {props.children}
                </div>
            </div>
        </BaseLayout>
    );
};
