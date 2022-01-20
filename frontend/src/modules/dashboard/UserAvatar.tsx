import { FC } from "react";

const UserAvatar: FC = () => {
    return (
        <img
            className="rounded-full shadow max-h-7"
            src="https://picsum.photos/200"
            title="your avatar"
        />
    );
};

UserAvatar.displayName = "UserAvatar";
export default UserAvatar;
