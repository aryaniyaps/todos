import { FC } from "react";
import { Helmet } from "react-helmet";
import withAuth from "../auth/withAuth";
import AppLayout from "../../layouts/AppLayout";
import TodoList from "./TodoList";

const DashboardPage: FC = () => {
    return (
        <AppLayout>
            <Helmet>
                <title>Dashboard | Todos</title>
            </Helmet>
            <TodoList />
        </AppLayout>
    );
};

DashboardPage.displayName = "DashboardPage";
export default withAuth(DashboardPage);
