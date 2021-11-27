import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import SpinnerComponent from "../components/Spinner";

export default {
    title: "Components/Spinner",
    component: SpinnerComponent,
} as ComponentMeta<typeof SpinnerComponent>;

const Template: ComponentStory<typeof SpinnerComponent> = (props) => {
    return <SpinnerComponent {...props} />;
};

export const Big = Template.bind({});
Big.args = {
    size: "big",
};

export const Small = Template.bind({});
Small.args = {
    size: "small",
};
