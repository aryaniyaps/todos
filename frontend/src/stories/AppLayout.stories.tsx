import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import { AppLayout } from "../layouts/AppLayout";

export default {
    title: "Layouts/AppLayout",
    component: AppLayout,
} as ComponentMeta<typeof AppLayout>;

const Template: ComponentStory<typeof AppLayout> = ({ children, ...props }) => {
    return <AppLayout {...props}>{children}</AppLayout>;
};

export const Default = Template.bind({});
