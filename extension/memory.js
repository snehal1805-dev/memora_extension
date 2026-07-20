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

    let page;

    try {

        page = await chrome.tabs.sendMessage(
            tab.id,
            {
                type: "EXTRACT_PAGE"
            }
        );

    } catch (error) {

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

    return await apiRequest(
        "/memory/save",
        "POST",
        memory,
        token
    );

}