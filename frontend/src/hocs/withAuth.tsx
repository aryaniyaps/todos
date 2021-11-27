import { ComponentType } from "react";

const withAuth = (Component: ComponentType) => {
    return (props: any) => {
        <Component {...props} />;
    };
};

export default withAuth;
