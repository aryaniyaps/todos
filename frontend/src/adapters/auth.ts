import { client } from "../lib/axiosClient";

export const authenticate = async (data: any) => {
    return await client.post("/auth/login", data);
};

export const unauthenticate = async () => {
    return await client.post("/auth/logout");
};
