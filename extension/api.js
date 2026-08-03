const BASE_URL = "https://memoraextension-production.up.railway.app";

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
        method,
        headers
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

        if (response.status === 401) {

            await chrome.storage.local.remove("token");

            throw new Error(
                "Session expired. Please login again."
            );

        }

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

export { apiRequest };