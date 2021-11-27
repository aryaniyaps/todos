import React from "react";
import Navbar from "../components/Navbar";
import BaseLayout from "./BaseLayout";

const AppLayout: React.FC = (props) => {
    return (
        <BaseLayout>
            <Navbar />
            <div className="overflow-y-auto">
                <div className="p-4 flex-grow mx-auto flex max-w-7xl">
                    {props.children}
                </div>
            </div>
        </BaseLayout>
    );
};

AppLayout.displayName = "AppLayout";
export default AppLayout;
