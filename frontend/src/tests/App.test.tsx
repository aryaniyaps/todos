import { render } from "@testing-library/react";
import App from "../App";

it("renders without crashing", () => {
    expect(render(<App />)).toBeTruthy();
});
