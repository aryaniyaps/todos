import { FC } from "react";
import SettingsIcon from "../icons/SettingsIcon";
import Button from "./Button";

const Navbar: FC = () => {
    return (
        <div className="bg-primary-300 shadow-md w-full z-20">
            <div className="max-w-7xl mx-auto py-2 flex justify-between items-center">
                <span className="font-semibold">navbar</span>
                <Button color="transparent" size="tiny" title="settings">
                    <SettingsIcon />
                </Button>
            </div>
        </div>
    );
};

Navbar.displayName = "Navbar";
export default Navbar;
