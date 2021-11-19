import { client } from "../lib/axiosClient";

export const fetchCurrentUser = async () => {
    return await client.get("/users/me");
};

export const createUser = async (data: any) => {
    return await client.post("/users", data);
};
