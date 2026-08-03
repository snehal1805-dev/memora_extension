// ---------------- LOGIN ----------------

async function login(email, password) {

    const response = await apiRequest(
        "/auth/login",
        "POST",
        {
            email,
            password
        }
    );

    const token = response.access_token;

    // Save JWT
    await chrome.storage.local.set({
        token: token
    });

    // Fetch logged-in user
    const user = await apiRequest(
        "/user/me",
        "GET",
        null,
        token
    );

    // Save user profile
    await chrome.storage.local.set({
        user: user
    });

    return response;

}

// ---------------- GET TOKEN ----------------

async function getToken() {

    const result = await chrome.storage.local.get("token");

    return result.token || null;

}

// ---------------- CHECK LOGIN ----------------

async function isLoggedIn() {

    const token = await getToken();

    if (!token) {
        return false;
    }

    try {

        // Verify token
        await apiRequest(
            "/user/me",
            "GET",
            null,
            token
        );

        return true;

    } catch (error) {

        console.error(error);

        // Remove invalid session
        await chrome.storage.local.remove([
            "token",
            "user"
        ]);

        return false;

    }

}

// ---------------- LOGOUT ----------------

async function logout() {

    await chrome.storage.local.remove([
        "token",
        "user"
    ]);

}