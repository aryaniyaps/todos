import MockAdapter from "axios-mock-adapter";
import client from "../../lib/httpClient";
import todosAdapter from "../../adapters/todos";

describe("Todos adapter tests", () => {
    let mock: MockAdapter;

    beforeAll(() => {
        mock = new MockAdapter(client);
    });

    afterEach(() => {
        mock.reset();
    });

    it("fetches an existing todo", async () => {});

    it("fetches the current user's todos", async () => {});

    it("creates a new todo", async () => {});

    it("updates an existing todo", async () => {});

    it("deletes an existing todo", async () => {});
});
