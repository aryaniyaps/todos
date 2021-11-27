import { FC } from "react";
import { Helmet } from "react-helmet";
import withAuth from "../hocs/withAuth";
import AppLayout from "../layouts/AppLayout";

const HomePage: FC = () => {
    return (
        <AppLayout>
            <Helmet>
                <title>Home | Todos</title>
            </Helmet>
            home page content
        </AppLayout>
    );
};

HomePage.displayName = "HomePage";
export default withAuth(HomePage);
