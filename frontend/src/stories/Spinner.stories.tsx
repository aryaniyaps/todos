import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import { Spinner } from "../components/Spinner";

export default {
    title: "Components/Spinner",
    component: Spinner,
} as ComponentMeta<typeof Spinner>;

const Template: ComponentStory<typeof Spinner> = (props) => {
    return <Spinner {...props} />;
};

export const Big = Template.bind({});
Big.args = {
    size: "big",
};

export const Small = Template.bind({});
Small.args = {
    size: "small",
};
