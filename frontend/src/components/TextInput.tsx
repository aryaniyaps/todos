import { forwardRef, HTMLProps } from "react";

export interface TextInputInputProps
    extends Omit<HTMLProps<HTMLInputElement>, "prefix" | "size"> {
    invalid?: boolean;
}

const TextInput = forwardRef<HTMLInputElement, TextInputInputProps>(
    ({ className = "", invalid, ...props }, ref) => {
        const border = invalid ? "border-danger" : "border-primary-400";
        const styles = `relative w-full py-2 px-3 shadow-sm rounded-md placeholder-primary-500 border ${border} bg-transparent  ${className}`;

        return <input className={styles} ref={ref} data-testid="input" {...props} />;
    }
);

TextInput.displayName = "TextInput";
export default TextInput;
