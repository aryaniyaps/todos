import { FC } from "react";
import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";
import { Formik, Form } from "formik";
import * as yup from "yup";
import Button from "../components/Button";
import FormField from "../components/FormField";
import BaseLayout from "../layouts/BaseLayout";

const LoginForm: FC = () => {
    const loginSchema = yup.object().shape({
        email: yup.string().email().required(),
        password: yup.string().required(),
    });

    return (
        <Formik
            validationSchema={loginSchema}
            initialValues={{ email: "", password: "" }}
            onSubmit={({ email, password }) => {}}
        >
            {({ handleSubmit, isSubmitting }) => (
                <div className="flex flex-col max-w-sm w-full items-center">
                    {/* form header */}
                    <div className="mb-6 mx-auto text-center">
                        <h2>Welcome back</h2>
                        <p>We're excited to see you again!</p>
                    </div>
                    {/* form body */}
                    <Form className="flex flex-col w-full p-6 bg-primary-100 rounded-md shadow">
                        <FormField name="email" placeholder="email" type="email" />
                        <FormField
                            name="password"
                            placeholder="password"
                            type="password"
                        />
                        <Link to="/password" className="text-right text-sm mb-4">
                            Forgot password?
                        </Link>
                        <Button
                            onClick={() => handleSubmit()}
                            loading={isSubmitting}
                            className="mt-2"
                        >
                            login
                        </Button>
                    </Form>
                    {/* form footer */}
                    <div className="mt-4">
                        Don't have an account? <Link to="/register">register</Link>
                    </div>
                </div>
            )}
        </Formik>
    );
};

LoginForm.displayName = "LoginForm";

const LoginPage: FC = () => {
    return (
        <BaseLayout>
            <Helmet>
                <title>Login | Todos</title>
            </Helmet>
            <div className="flex flex-grow justify-center items-center">
                <LoginForm />
            </div>
        </BaseLayout>
    );
};

LoginPage.displayName = "LoginPage";
export default LoginPage;
