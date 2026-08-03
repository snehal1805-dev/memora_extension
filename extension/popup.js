document.addEventListener("DOMContentLoaded", async () => {

    const loginSection = document.getElementById("loginSection");
    const dashboardSection = document.getElementById("dashboardSection");

    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");

    const loginBtn = document.getElementById("loginBtn");
    const saveBtn = document.getElementById("saveBtn");
    const logoutBtn = document.getElementById("logoutBtn");

    const pageTitle = document.getElementById("pageTitle");
    const pageUrl = document.getElementById("pageUrl");

    const status = document.getElementById("status");

    // -------- USER CARD --------

    const userCard = document.getElementById("userCard");
    const avatar = document.getElementById("avatar");
    const userName = document.getElementById("userName");
    const userEmail = document.getElementById("userEmail");

    // ---------- CHECK LOGIN ----------

    if (await isLoggedIn()) {

        loginSection.style.display = "none";
        dashboardSection.style.display = "block";

        await loadUser();
        await loadCurrentPage();

    } else {

        loginSection.style.display = "block";
        dashboardSection.style.display = "none";

    }

    // ---------- LOGIN ----------

    loginBtn.addEventListener("click", async () => {

        status.innerText = "";

        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        if (!email || !password) {

            status.style.color = "red";
            status.innerText = "Enter email and password.";

            return;

        }

        loginBtn.disabled = true;
        loginBtn.innerText = "Logging in...";

        try {

            await login(email, password);

            loginSection.style.display = "none";
            dashboardSection.style.display = "block";

            await loadUser();
            await loadCurrentPage();

            status.style.color = "#22c55e";
            status.innerText = "✅ Login Successful";

        } catch (error) {

            console.error(error);

            status.style.color = "red";
            status.innerText = error.message;

            if (error.message === "Session expired. Please login again.") {

                loginSection.style.display = "block";
                dashboardSection.style.display = "none";

            }

        } finally {

            loginBtn.disabled = false;
            loginBtn.innerText = "Login";

        }

    });

    // ---------- SAVE ----------

    saveBtn.addEventListener("click", async () => {

        status.style.color = "white";
        status.innerText = "Saving...";

        saveBtn.disabled = true;

        try {

            await saveCurrentPage();

            status.style.color = "#22c55e";
            status.innerText = "✅ Memory Saved Successfully";

        } catch (error) {

            console.error(error);

            status.style.color = "red";
            status.innerText = error.message;

            if (error.message === "Session expired. Please login again.") {

                loginSection.style.display = "block";
                dashboardSection.style.display = "none";

            }

        } finally {

            saveBtn.disabled = false;

        }

    });

    // ---------- LOGOUT ----------

    logoutBtn.addEventListener("click", async () => {

        await logout();

        loginSection.style.display = "block";
        dashboardSection.style.display = "none";

        userCard.style.display = "none";

        emailInput.value = "";
        passwordInput.value = "";

        status.style.color = "#22c55e";
        status.innerText = "Logged out successfully.";

    });

    // ---------- LOAD USER ----------

    async function loadUser() {

        const result = await chrome.storage.local.get("user");

        if (!result.user) {

            userCard.style.display = "none";
            return;

        }

        userCard.style.display = "flex";

        avatar.innerText =
            result.user.full_name.charAt(0).toUpperCase();

        userName.innerText =
            result.user.full_name;

        userEmail.innerText =
            result.user.email;

    }

    // ---------- LOAD CURRENT PAGE ----------

    async function loadCurrentPage() {

        const [tab] = await chrome.tabs.query({
            active: true,
            currentWindow: true
        });

        if (!tab) return;

        pageTitle.innerText = tab.title || "No Title";
        pageUrl.innerText = tab.url || "";

    }

});