import { render } from "@testing-library/react";
import Spinner from "../../components/Spinner";

describe("Spinner tests", () => {
    it("should render a spinner", () => {
        const { getByTestId } = render(<Spinner />);
        const spinner = getByTestId("spinner");
        expect(spinner).toBeVisible();
    });

    it("should match snapshot", () => {
        const { getByTestId } = render(<Spinner />);
        const spinner = getByTestId("spinner");
        expect(spinner).toMatchSnapshot();
    });
});
