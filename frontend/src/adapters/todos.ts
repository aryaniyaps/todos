import { client } from "../lib/axiosClient";

export const fetchTodos = async () => {
    return await client.get("/todos");
};

export const createTodo = async (data: any) => {
    return await client.post("/todos", data);
};

export const updateTodo = async (todoID: number, data: any) => {
    return await client.patch(`/todos/${todoID}`, data);
};

export const deleteTodo = async (todoID: number) => {
    return await client.delete(`/todos/${todoID}`);
};
