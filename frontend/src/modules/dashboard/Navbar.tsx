import { FC } from "react";
import SettingsIcon from "../../icons/SettingsIcon";
import UserAvatar from "./UserAvatar";

const Navbar: FC = () => {
    return (
        <div className="bg-primary-300 shadow-md w-full z-20">
            <div className="py-2 mx-auto max-w-7xl flex justify-between items-center">
                <span className="font-semibold">navbar</span>
                <div className="flex items-center gap-2">
                    <UserAvatar />
                    <Button color="transparent" size="tiny" title="settings">
                        <SettingsIcon />
                    </Button>
                </div>
            </div>
        </div>
    );
};

Navbar.displayName = "Navbar";
export default Navbar;
