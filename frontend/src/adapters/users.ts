import client from "../lib/httpClient";

const fetchCurrentUser = async () => {
    return await client.get("/users/me");
};

const createUser = async (data: { email: string; password: string }) => {
    return await client.post("/users", data);
};

export default { fetchCurrentUser, createUser };
