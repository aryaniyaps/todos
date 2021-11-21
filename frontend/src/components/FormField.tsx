import React, { DetailedHTMLProps, InputHTMLAttributes } from "react";
import { useField } from "formik";
import { Input } from "./Input";

export const FormField: React.FC<
    DetailedHTMLProps<InputHTMLAttributes<HTMLInputElement>, HTMLInputElement> & {
        name: string;
    }
> = ({ ref: _, ...props }) => {
    const [field, meta] = useField(props);
    return (
        <div className="flex flex-col mb-2 text-lg text-left">
            {meta.error && meta.touched && (
                <span className="italic text-danger">
                    <span className="mx-1">-</span>
                    {meta.error}
                </span>
            )}
            <Input {...field} {...props} invalid={!!meta.error} />
        </div>
    );
};
