import { client } from "../lib/httpClient";

export const authenticate = async (data: { email: string; password: string }) => {
    return await client.post("/auth/login", data);
};

export const unauthenticate = async () => {
    return await client.post("/auth/logout");
};
