import { FC } from "react";
import SettingsIcon from "../icons/SettingsIcon";
import Button from "./Button";

const Navbar: FC = () => {
    return (
        <div className="bg-primary-300 shadow-md w-full z-20">
            <div className="max-w-7xl mx-auto py-4 flex justify-between">
                <span className="font-semibold">navbar</span>
                <Button color="transparent" size="tiny">
                    <SettingsIcon />
                </Button>
            </div>
        </div>
    );
};

Navbar.displayName = "Navbar";
export default Navbar;
