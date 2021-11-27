import { FC, DetailedHTMLProps, InputHTMLAttributes } from "react";
import { useField } from "formik";
import TextInput from "./TextInput";

const FormField: FC<
    DetailedHTMLProps<InputHTMLAttributes<HTMLInputElement>, HTMLInputElement> & {
        name: string;
    }
> = ({ ref: _, ...props }) => {
    const [field, meta] = useField(props);
    return (
        <div className="flex flex-col mb-4">
            <TextInput {...field} {...props} invalid={!!meta.error} />
            {meta.error && meta.touched && (
                <span className="mt-0.5 italic text-danger">{meta.error}</span>
            )}
        </div>
    );
};

FormField.displayName = "FormField";
export default FormField;
