import React, { forwardRef, HTMLProps } from "react";

export interface InputProps
    extends Omit<HTMLProps<HTMLInputElement>, "prefix" | "size"> {
    invalid?: boolean;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
    ({ className = "", invalid, ...props }, ref) => {
        const border = invalid ? "border-danger" : "border-primary-800";
        const styles = `w-full text-lg inline-block cursor-text py-3 px-4 rounded text-primary-300 placeholder-primary-400 border ${border} transition-colors duration-300 ease-in-out bg-input focus:outline-none ${
            props.disabled ? "cursor-not-allowed" : ""
        } ${className}`;

        return <input className={styles} ref={ref} data-testid="input" {...props} />;
    }
);
