import React from "react";
import { Helmet } from "react-helmet";
import { BaseLayout } from "../layouts/BaseLayout";

export const HomePage: React.FC = () => {
    return (
        <BaseLayout>
            <Helmet>
                <title>Home | Todos</title>
            </Helmet>
            Hello world!
        </BaseLayout>
    );
};
