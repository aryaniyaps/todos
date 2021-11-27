import { FC } from "react";
import { Helmet } from "react-helmet";
import { AppLayout } from "../layouts/AppLayout";

export const HomePage: FC = () => {
    return (
        <AppLayout>
            <Helmet>
                <title>Home | Todos</title>
            </Helmet>
            home page content
        </AppLayout>
    );
};
