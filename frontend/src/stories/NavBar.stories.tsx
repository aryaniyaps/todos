import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import { NavBar } from "../components/NavBar";

export default {
    title: "Components/NavBar",
    component: NavBar,
} as ComponentMeta<typeof NavBar>;

const Template: ComponentStory<typeof NavBar> = (props) => {
    return <NavBar {...props} />;
};

export const Main = Template.bind({});
