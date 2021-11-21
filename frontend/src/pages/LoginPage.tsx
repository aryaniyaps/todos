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
                <Form className="flex flex-col gap-4 p-8 bg-primary-600 rounded-md max-w-sm">
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
                        className="mt-3"
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
            <LoginForm />
        </BaseLayout>
    );
};
