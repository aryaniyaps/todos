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

    it("fetches an existing todo", async () => {
        const todo: any = {
            id: 1,
            content: "sample content",
            completed: false,
        };

        mock.onGet(`/todos/${todo.id}`).reply(200, todo);
        const { data } = await todosAdapter.fetchTodo(todo.id);
        expect(data).toEqual(todo);
    });

    it("fetches the current user's todos", async () => {});

    it("creates a new todo", async () => {});

    it("updates a new todo", async () => {});

    it("deletes a new todo", async () => {});
});
