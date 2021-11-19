import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import { HomePage } from "../pages/HomePage";

export default {
    title: "Pages/HomePage",
    component: HomePage,
} as ComponentMeta<typeof HomePage>;

const Template: ComponentStory<typeof HomePage> = (props) => {
    return <HomePage {...props} />;
};

export const Default = Template.bind({});
