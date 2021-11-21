import { FC } from "react";
import { Helmet } from "react-helmet";
import { Formik, Form } from "formik";
import { Button } from "../components/Button";
import { FormField } from "../components/FormField";
import { BaseLayout } from "../layouts/BaseLayout";

const LoginForm: FC = () => {
    return (
        <Formik
            initialValues={{ email: "", password: "" }}
            onSubmit={({ email, password }) => {}}
        >
            {({ handleSubmit, isSubmitting }) => (
                <Form className="flex flex-col max-w-sm w-full p-6 bg-primary-600 rounded border border-primary-800">
                    {/* form header */}
                    <div className="mb-6 mx-auto text-center">
                        <h3>Welcome back</h3>
                        <p className="text-sm text-primary-200">
                            We're excited to see you again!
                        </p>
                    </div>
                    <FormField
                        name="email"
                        placeholder="email"
                        type="email"
                        spellCheck={false}
                    />
                    <FormField name="password" placeholder="password" type="password" />
                    <Button
                        title="login"
                        onClick={() => handleSubmit()}
                        loading={isSubmitting}
                        className="mt-2"
                    >
                        login
                    </Button>
                    <a className="mt-4 mx-auto" href="/">
                        I need an account
                    </a>
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
            <div className="flex flex-col self-center h-full w-full justify-center items-center">
                <LoginForm />
            </div>
        </BaseLayout>
    );
};
