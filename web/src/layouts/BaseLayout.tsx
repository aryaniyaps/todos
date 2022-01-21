import React from "react";

const BaseLayout: React.FC = (props) => {
    return <div className="flex flex-col flex-grow">{props.children}</div>;
};

BaseLayout.displayName = "BaseLayout";
export default BaseLayout;
