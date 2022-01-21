import client from "../lib/httpClient";

const authenticate = async (data: { email: string; password: string }) => {
    return await client.post("/auth/login", data);
};

const unauthenticate = async () => {
    return await client.post("/auth/logout");
};

export default { unauthenticate, authenticate };
