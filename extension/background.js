chrome.runtime.onInstalled.addListener(() => {

    console.log("🧠 Memora Extension Installed");

});

chrome.runtime.onStartup.addListener(() => {

    console.log("🧠 Memora Started");

});