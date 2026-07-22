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

        let data = {};

        try {
            data = await response.json();
        } catch {
            data = {};
        }

        // -------- TOKEN EXPIRED --------

        if (response.status === 401) {

            await chrome.storage.local.remove("token");

            throw new Error(
                "Session expired. Please login again."
            );

        }

        // -------- OTHER ERRORS --------

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