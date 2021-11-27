import { FC } from "react";
import { Spinner } from "./Spinner";

export const Fallback: FC = () => {
    return (
        <div className="flex flex-grow justify-center items-center">
            <Spinner />
        </div>
    );
};
