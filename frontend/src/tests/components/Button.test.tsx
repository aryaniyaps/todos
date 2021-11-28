import { render } from "@testing-library/react";
import Button from "../../components/Button";

describe("Button component tests", () => {
    it("should render a button", () => {
        const { getByText } = render(<Button>sample label</Button>);
        const text = getByText("sample label");
        expect(text).toBeVisible();
    });

    it("should render a disabled button when loading", () => {
        const { getByText } = render(<Button loading>sample label</Button>);
        const button = getByText("sample label").closest("button");
        expect(button).toBeDisabled();
    });

    it("should render a disabled button when disabled", () => {
        const { getByText } = render(<Button disabled>sample label</Button>);
        const button = getByText("sample label").closest("button");
        expect(button).toBeDisabled();
    });

    it("should match snapshot", () => {
        const { getByTestId } = render(<Button>sample label</Button>);
        const button = getByTestId("button");
        expect(button).toMatchSnapshot();
    });
});
