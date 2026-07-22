async function login(email, password) {

    const response = await apiRequest(
        "/auth/login",
        "POST",
        {
            email,
            password
        }
    );

    await chrome.storage.local.set({
        token: response.access_token
    });

    return response;

}


async function getToken() {

    const result = await chrome.storage.local.get("token");

    return result.token || null;

}


async function isLoggedIn() {

    const token = await getToken();

    if (!token) {
        return false;
    }

    try {

        await apiRequest(
            "/user/me",
            "GET",
            null,
            token
        );

        return true;

    } catch (error) {

        await chrome.storage.local.remove("token");

        return false;

    }

}


async function logout() {

    await chrome.storage.local.remove("token");

}