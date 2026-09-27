const status = document.querySelector("#status");
document.querySelector("#save").addEventListener("click", async () => {
  await chrome.storage.local.set({savedAt: Date.now()});
  status.textContent = "Saved.";
});
