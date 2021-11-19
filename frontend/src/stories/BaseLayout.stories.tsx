import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import { BaseLayout } from "../layouts/BaseLayout";

export default {
    title: "Layouts/BaseLayout",
    component: BaseLayout,
} as ComponentMeta<typeof BaseLayout>;

const Template: ComponentStory<typeof BaseLayout> = ({ children, ...props }) => {
    return <BaseLayout {...props}>{children}</BaseLayout>;
};

export const Default = Template.bind({});
