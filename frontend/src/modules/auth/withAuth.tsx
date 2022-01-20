import { ComponentType } from "react";

const withAuth = (Component: ComponentType) => {
    return (props: any) => {
        return <Component {...props} />;
    };
};

export default withAuth;
