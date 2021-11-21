import React from "react";

export const BaseLayout: React.FC = (props) => {
    return <div className="flex flex-col h-full w-full">{props.children}</div>;
};
