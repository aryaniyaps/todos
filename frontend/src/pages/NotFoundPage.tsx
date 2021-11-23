import { FC } from "react";
import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";
import { Button } from "../components/Button";
import { BaseLayout } from "../layouts/BaseLayout";

export const NotFoundPage: FC = () => {
    return (
        <BaseLayout>
            <Helmet>
                <title>Not found | Todos</title>
            </Helmet>
            <div className="flex flex-col text-center flex-grow justify-center items-center p-2">
                <h1>Page not found</h1>
                <p>Sorry, we couldn't find the page you were looking for.</p>
                <Link to="/">
                    <Button color="accent" className="mt-4">
                        Go back home
                    </Button>
                </Link>
            </div>
        </BaseLayout>
    );
};
