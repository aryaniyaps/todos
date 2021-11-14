import React from "react";
import { Helmet } from "react-helmet";
import { BaseLayout } from "../layouts/BaseLayout";

interface HomePageProps {}

export const HomePage: React.FC<HomePageProps> = () => {
    return (
        <BaseLayout>
            <Helmet>
                <title>Home | Todos</title>
            </Helmet>
            Hello world!
            {/* children*/}
        </BaseLayout>
    );
};
