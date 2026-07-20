console.log("✅ Memora Content Script Loaded");

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

    if (request.type !== "EXTRACT_PAGE") {
        return;
    }

    try {

        const page = {
            title: document.title,
            url: window.location.href,
            favicon: getFavicon(),
            content: extractContent()
        };

        sendResponse(page);

    } catch (error) {

        console.error(error);

        sendResponse(null);

    }

    return true;

});


function getFavicon() {

    const icon = document.querySelector(
        "link[rel*='icon']"
    );

    if (icon) {
        return icon.href;
    }

    return "";

}


function extractContent() {

    let text = "";

    if (document.body) {
        text = document.body.innerText;
    }

    text = text.replace(/\s+/g, " ").trim();

    return text.substring(0, 15000);

}