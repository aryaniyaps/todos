import { FC } from "react";
import { Helmet } from "react-helmet";
import { Formik, Form } from "formik";
import { Button } from "../components/Button";
import { FormField } from "../components/FormField";
import { BaseLayout } from "../layouts/BaseLayout";

const RegisterForm: FC = () => {
    return (
        <Formik
            initialValues={{ email: "", password: "" }}
            onSubmit={({ email, password }) => {}}
        >
            {({ handleSubmit, isSubmitting }) => (
                <Form className="flex flex-col max-w-sm w-full p-6 bg-primary-100 rounded-md shadow">
                    <FormField name="email" placeholder="email" type="email" />
                    <FormField name="password" placeholder="password" type="password" />
                    <Button
                        onClick={() => handleSubmit()}
                        loading={isSubmitting}
                        className="mt-2"
                    >
                        register
                    </Button>
                </Form>
            )}
        </Formik>
    );
};

export const RegisterPage: FC = () => {
    return (
        <BaseLayout>
            <Helmet>
                <title>Register | Todos</title>
            </Helmet>
            <div className="flex flex-col h-full w-full justify-center items-center">
                {/* header */}
                <div className="mb-6 mx-auto text-center">
                    <h2>Welcome aboard</h2>
                    <p>
                        By creating an account, you agree to our
                        <br /> <a>terms of service</a> and <a>privacy policy</a>.
                    </p>
                </div>
                <RegisterForm />
                <div className="mt-4">
                    Already have an account? <a href="/login">login</a>
                </div>
            </div>
        </BaseLayout>
    );
};
