import { FC } from "react";
import { Helmet } from "react-helmet";
import withAuth from "../hocs/withAuth";
import AppLayout from "../layouts/AppLayout";
import TodoList from "../components/TodoList";

const HomePage: FC = () => {
    return (
        <AppLayout>
            <Helmet>
                <title>Home | Todos</title>
            </Helmet>
            <TodoList />
        </AppLayout>
    );
};

HomePage.displayName = "HomePage";
export default withAuth(HomePage);
