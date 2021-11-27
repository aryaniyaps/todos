import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import { Fallback } from "../components/Fallback";

export default {
    title: "Components/Fallback",
    component: Fallback,
} as ComponentMeta<typeof Fallback>;

const Template: ComponentStory<typeof Fallback> = (props) => {
    return <Fallback {...props} />;
};

export const Default = Template.bind({});
