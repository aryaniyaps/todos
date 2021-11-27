import client from "../lib/httpClient";

export const fetchCurrentUser = async () => {
    return await client.get("/users/me");
};

export const createUser = async (data: { email: string; password: string }) => {
    return await client.post("/users", data);
};
