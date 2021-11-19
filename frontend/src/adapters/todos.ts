import { client } from "../lib/httpClient";

export const fetchTodos = async () => {
    return await client.get("/todos");
};

export const createTodo = async (data: { content: string; completed?: boolean }) => {
    return await client.post("/todos", data);
};

export const updateTodo = async (
    todoId: number,
    data: {
        content?: string;
        completed?: boolean;
    }
) => {
    return await client.patch(`/todos/${todoId}`, data);
};

export const deleteTodo = async (todoId: number) => {
    return await client.delete(`/todos/${todoId}`);
};
