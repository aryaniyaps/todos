import React, { forwardRef, HTMLProps } from "react";

export interface TextInputInputProps
    extends Omit<HTMLProps<HTMLInputElement>, "prefix" | "size"> {
    invalid?: boolean;
}

export const TextInput = forwardRef<HTMLInputElement, TextInputInputProps>(
    ({ className = "", invalid, ...props }, ref) => {
        const border = invalid ? "border-danger" : "border-primary-800";
        const styles = `w-full py-2 px-3 rounded text-primary-300 placeholder-primary-400 border ${border} transition-colors duration-300 ease-in-out bg-input  ${className}`;

        return <input className={styles} ref={ref} data-testid="input" {...props} />;
    }
);

TextInput.displayName = "TextInput";
