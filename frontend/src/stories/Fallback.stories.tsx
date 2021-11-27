import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import FallbackComponent from "../components/Fallback";

export default {
    title: "Components/Fallback",
    component: FallbackComponent,
} as ComponentMeta<typeof FallbackComponent>;

const Template: ComponentStory<typeof FallbackComponent> = (props) => {
    return <FallbackComponent {...props} />;
};

export const Fallback = Template.bind({});
