import React from "react";

export const BaseLayout: React.FC = (props) => {
    return <div className="flex flex-col flex-grow">{props.children}</div>;
};
