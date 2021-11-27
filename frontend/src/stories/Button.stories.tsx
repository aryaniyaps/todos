import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import ButtonComponent from "../components/Button";

export default {
    title: "Components/Button",
    component: ButtonComponent,
} as ComponentMeta<typeof ButtonComponent>;

const Template: ComponentStory<typeof ButtonComponent> = ({
    children = "sample label",
    ...props
}) => {
    return <ButtonComponent {...props}>{children}</ButtonComponent>;
};

export const Primary = Template.bind({});
Primary.args = {
    color: "primary",
};

export const Accent = Template.bind({});
Accent.args = {
    color: "accent",
};

export const Transparent = Template.bind({});
Transparent.args = {
    color: "transparent",
};

export const Big = Template.bind({});
Big.args = {
    size: "big",
};

export const Small = Template.bind({});
Small.args = {
    size: "small",
};

export const Tiny = Template.bind({});
Tiny.args = {
    size: "tiny",
};

export const Loading = Template.bind({});
Loading.args = {
    loading: true,
};
