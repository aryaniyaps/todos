import { ComponentStory, ComponentMeta } from "@storybook/react";

import NavbarComponent from "../components/Navbar";

export default {
    title: "Components/Navbar",
    component: NavbarComponent,
} as ComponentMeta<typeof NavbarComponent>;

const Template: ComponentStory<typeof NavbarComponent> = (props) => {
    return <NavbarComponent {...props} />;
};

export const Navbar = Template.bind({});
