import { FC } from "react";
import Spinner from "./Spinner";

const Fallback: FC = () => {
    return (
        <div className="flex flex-grow justify-center items-center">
            <Spinner />
        </div>
    );
};

Fallback.displayName = "Fallback";
export default Fallback;