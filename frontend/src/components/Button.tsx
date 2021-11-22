import { FC, ButtonHTMLAttributes, DetailedHTMLProps } from "react";
import { Spinner } from "./Spinner";

const sizeMap = {
    big: "py-2 px-6 text-md rounded-lg",
    small: "px-2 py-1 text-base rounded-md",
    tiny: "px-1 text-sm rounded-sm",
};

const colorMap = {
    accent:
        "text-primary-100 bg-accent hover:bg-accent-hover disabled:bg-accent-disabled",
    primary:
        "text-primary-100 bg-primary-600 hover:bg-primary-500 disabled:bg-primary-500",
    transparent: "bg-transparent",
};

interface ButtonProps
    extends DetailedHTMLProps<
        ButtonHTMLAttributes<HTMLButtonElement>,
        HTMLButtonElement
    > {
    /** How big is the button? */
    size?: keyof typeof sizeMap;
    /** The color of the button */
    color?: keyof typeof colorMap;
    /** Is the button loading? */
    loading?: boolean;
    /** Does the button have transitions? */
    transition?: boolean;
}

export const Button: FC<ButtonProps> = ({
    children,
    disabled,
    loading,
    transition,
    className = "",
    color = "primary",
    size = "big",
    ...props
}) => {
    return (
        <button
            disabled={disabled || loading}
            data-testid="button"
            className={`flex ${sizeMap[size]} 
            ${transition ? "transition duration-200 ease-in-out" : ""} 
            ${colorMap[color]} font-semibold items-center justify-center 
            ${disabled ? "cursor-not-allowed" : ""} ${className}`}
            {...props}
        >
            <span className={loading ? "opacity-0" : `flex items-center`}>
                {children}
            </span>
            {loading ? (
                <span className="absolute">
                    <Spinner size={size === "small" ? "small" : "big"} />
                </span>
            ) : null}
        </button>
    );
};

Button.displayName = "Button";
