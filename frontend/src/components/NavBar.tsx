import { FC } from "react";

export const NavBar: FC = () => {
    return (
        <div className="bg-primary-300 shadow-sm w-full">
            <div className="max-w-7xl mx-auto p-4 font-semibold">navbar</div>
        </div>
    );
};

NavBar.displayName = "NavBar";
