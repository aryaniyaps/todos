import { FC } from "react";
import { Helmet } from "react-helmet";
import { Formik, Form } from "formik";
import * as yup from "yup";
import { Button } from "../components/Button";
import { FormField } from "../components/FormField";
import { BaseLayout } from "../layouts/BaseLayout";

const LoginForm: FC = () => {
    const schema = yup.object().shape({
        email: yup.string().email().required(),
        password: yup.string().required(),
    });
    return (
        <Formik
            validationSchema={schema}
            initialValues={{ email: "", password: "" }}
            onSubmit={({ email, password }) => {}}
        >
            {({ handleSubmit, isSubmitting }) => (
                <Form className="flex flex-col max-w-sm w-full p-6 bg-primary-100 rounded-md shadow">
                    <FormField name="email" placeholder="email" type="email" />
                    <FormField name="password" placeholder="password" type="password" />
                    <a href="/password" className="text-right text-sm mb-4">
                        Forgot password?
                    </a>
                    <Button
                        onClick={() => handleSubmit()}
                        loading={isSubmitting}
                        className="mt-2"
                    >
                        login
                    </Button>
                </Form>
            )}
        </Formik>
    );
};

export const LoginPage: FC = () => {
    return (
        <BaseLayout>
            <Helmet>
                <title>Login | Todos</title>
            </Helmet>
            <div className="flex flex-col h-full w-full justify-center items-center">
                {/* header */}
                <div className="mb-6 mx-auto text-center">
                    <h2>Welcome back</h2>
                    <p>We're excited to see you again!</p>
                </div>
                <LoginForm />
                <div className="mt-4">
                    Don't have an account? <a href="/register">register</a>
                </div>
            </div>
        </BaseLayout>
    );
};
