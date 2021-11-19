import React from "react";

interface ButtonProps {
    primary?: boolean;
    size?: "small" | "medium" | "large";
    backgroundColor?: string;
}

export const Button: React.FC<ButtonProps> = ({
    children,
    primary = true,
    size = "medium",
    ...props
}) => {
    return <button {...props}>{children}</button>;
};
