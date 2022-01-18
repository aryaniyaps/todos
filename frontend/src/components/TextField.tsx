import { FC, InputHTMLAttributes, DetailedHTMLProps } from "react";
import { Field } from "react-final-form";
import TextInput from "./TextInput";

interface TextFieldProps {
    name: string;
}

const TextField: FC<
    DetailedHTMLProps<InputHTMLAttributes<HTMLInputElement>, HTMLInputElement> &
        TextFieldProps
> = ({ name, ...props }) => {
    return (
        <Field name={name} {...props}>
            {({ input, meta }) => {
                const error = meta.error || meta.submitError;
                return (
                    <div className="flex flex-col mb-4">
                        <TextInput {...input} error={error} />
                        {error && meta.touched && (
                            <span className="mt-0.5 italic text-danger">
                                {meta.error}
                            </span>
                        )}
                    </div>
                );
            }}
        </Field>
    );
};

TextField.displayName = "TextField";
export default TextField;
