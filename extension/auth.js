async function login(email, password) {

    const response = await apiRequest(
        "/auth/login",
        "POST",
        {
            email: email,
            password: password
        }
    );

    await chrome.storage.local.set({
        token: response.access_token
    });

    return response;

}


async function getToken() {

    const result = await chrome.storage.local.get(
        "token"
    );

    return result.token;

}


async function isLoggedIn() {

    const token = await getToken();

    return !!token;

}


async function logout() {

    await chrome.storage.local.remove(
        "token"
    );

}