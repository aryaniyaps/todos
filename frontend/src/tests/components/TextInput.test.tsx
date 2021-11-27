import { render } from "@testing-library/react";
import TextInput from "../../components/TextInput";

describe("TextInput tests", () => {
    it("should render a text input", () => {
        const { getByTestId } = render(<TextInput />);
        const textInput = getByTestId("text-input");
        expect(textInput).toBeVisible();
    });

    it("should match snapshot", () => {
        const { getByTestId } = render(<TextInput />);
        const textInput = getByTestId("text-input");
        expect(textInput).toMatchSnapshot();
    });
});
