import { FC } from "react";
import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { Input, Button } from "@nextui-org/react";
import BaseLayout from "../../layouts/BaseLayout";

type LoginInput = {
    email: string;
    password: string;
};

const LoginForm: FC = () => {
    const {
        handleSubmit,
        formState: { isSubmitting },
    } = useForm<LoginInput>();

    return (
        <div className="flex flex-col max-w-sm w-full items-center">
            {/* form header */}
            <div className="mb-6 mx-auto text-center">
                <h2>Welcome back</h2>
                <p>We're excited to see you again!</p>
            </div>
            {/* form body */}
            <form
                onSubmit={handleSubmit((data) => {})}
                className="flex flex-col w-full p-6 bg-primary-100 rounded-md shadow"
            >
                <Input name="email" placeholder="email" type="email" />
                <Input name="password" placeholder="password" type="password" />
                <Link to="/password" className="text-right text-sm mb-4">
                    Forgot password?
                </Link>
                <Button type="submit" disabled={isSubmitting} className="mt-2">
                    login
                </Button>
            </form>
            {/* form footer */}
            <div className="mt-4">
                Don't have an account? <Link to="/register">register</Link>
            </div>
        </div>
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
