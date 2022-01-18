import { forwardRef } from "react";
import { Field } from "react-final-form";
import TextInput from "./TextInput";

interface TextFieldProps {
    name: string;
}

const TextField = forwardRef<HTMLInputElement, TextFieldProps>(({ name }, ref) => {
    return (
        <Field name={name}>
            {({ input, meta }) => {
                const error = meta.error || meta.submitError;
                return (
                    <div className="flex flex-col mb-4">
                        <TextInput {...input} ref={ref} error={error} />
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
});

TextField.displayName = "TextField";
export default TextField;
