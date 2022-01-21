import { FC } from "react";
import { CircularProgress } from "@mui/material";

const Fallback: FC = () => {
    return (
        <div className="flex flex-grow justify-center items-center">
            <CircularProgress />
        </div>
    );
};

Fallback.displayName = "Fallback";
export default Fallback;
