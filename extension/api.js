const BASE_URL = "http://127.0.0.1:8000";

async function apiRequest(
    endpoint,
    method = "GET",
    body = null,
    token = null
) {

    const headers = {
        "Content-Type": "application/json"
    };

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    const options = {
        method: method,
        headers: headers
    };

    if (body) {
        options.body = JSON.stringify(body);
    }

    try {

        const response = await fetch(
            `${BASE_URL}${endpoint}`,
            options
        );

        const data = await response.json();

        if (!response.ok) {

            throw new Error(
                data.detail || "Request Failed"
            );

        }

        return data;

    } catch (error) {

        console.error("API ERROR:", error);

        throw error;
    }

}