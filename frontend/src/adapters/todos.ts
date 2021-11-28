import client from "../lib/httpClient";

const fetchTodos = async () => {
    return await client.get("/todos");
};

const fetchTodo = async (todoId: number) => {
    return await client.get(`/todos/${todoId}`);
};

const createTodo = async (data: { content: string; completed?: boolean }) => {
    return await client.post("/todos", data);
};

const updateTodo = async (
    todoId: number,
    data: {
        content?: string;
        completed?: boolean;
    }
) => {
    return await client.patch(`/todos/${todoId}`, data);
};

const deleteTodo = async (todoId: number) => {
    return await client.delete(`/todos/${todoId}`);
};

export default { fetchTodos, fetchTodo, createTodo, updateTodo, deleteTodo };
