import { FC } from "react";
import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";
import * as yup from "yup";
import BaseLayout from "../layouts/BaseLayout";

const registerSchema = yup.object().shape({
    email: yup.string().email().required(),
    password: yup.string().required().min(8),
});

type RegisterInput = {
    email: string;
    password: string;
};

const RegisterForm: FC = () => {
    const onSubmit = (data: RegisterInput) => {};
    return (
        <div className="flex flex-col max-w-sm w-full items-center">
            {/* form header */}
            <div className="mb-6 mx-auto text-center">
                <h2>Welcome aboard</h2>
                <p>
                    By creating an account, you agree to our
                    <br /> <a>terms of service</a> and <a>privacy policy</a>.
                </p>
            </div>
            {/* form body */}
            <Form
                onSubmit={onSubmit}
                className="flex flex-col w-full p-6 bg-primary-100 rounded-md shadow"
            >
                {({ handleSubmit, submitting }) => (
                    <form onSubmit={handleSubmit}>
                        <TextField name="email" placeholder="email" type="email" />
                        <TextField
                            name="password"
                            placeholder="password"
                            type="password"
                        />
                        <Button type="submit" loading={submitting} className="mt-2">
                            register
                        </Button>
                    </form>
                )}
            </Form>
            {/* form footer */}
            <div className="mt-4">
                Already have an account? <Link to="/login">login</Link>
            </div>
        </div>
    );
};

RegisterForm.displayName = "RegisterForm";

const RegisterPage: FC = () => {
    return (
        <BaseLayout>
            <Helmet>
                <title>Register | Todos</title>
            </Helmet>
            <div className="flex flex-grow justify-center items-center">
                <RegisterForm />
            </div>
        </BaseLayout>
    );
};

RegisterPage.displayName = "RegisterPage";
export default RegisterPage;
