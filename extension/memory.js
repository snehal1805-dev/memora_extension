async function saveCurrentPage() {

    const token = await getToken();

    if (!token) {
        throw new Error("Please login first.");
    }

    const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    if (!tab || !tab.id) {
        throw new Error("No active tab found.");
    }

    let page = null;

    try {

        page = await chrome.tabs.sendMessage(
            tab.id,
            {
                type: "EXTRACT_PAGE"
            }
        );

    } catch (error) {

        console.log("Injecting content script...");

        await chrome.scripting.executeScript({
            target: {
                tabId: tab.id
            },
            files: [
                "content.js"
            ]
        });

        page = await chrome.tabs.sendMessage(
            tab.id,
            {
                type: "EXTRACT_PAGE"
            }
        );

    }

    if (!page) {
        throw new Error("Unable to read page content.");
    }

    const memory = {
        title: page.title,
        url: page.url,
        favicon: page.favicon,
        raw_content: page.content
    };

    try {

        const response = await apiRequest(
            "/memory/save",
            "POST",
            memory,
            token
        );

        return response;

    } catch (error) {

        console.error("Save Memory Error:", error);

        throw error;

    }

}