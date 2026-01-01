function sendMessage() {
    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    const message = input.value.trim();
    if (message === "") return;

    // User message
    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.innerText = message;
    chatBox.appendChild(userDiv);

    input.value = "";

    // Bot reply (dummy for now)
    setTimeout(() => {
        const botDiv = document.createElement("div");
        botDiv.className = "bot-message";
        botDiv.innerText = "📊 I'm analyzing the stock data... (ML coming soon!)";
        chatBox.appendChild(botDiv);

        chatBox.scrollTop = chatBox.scrollHeight;
    }, 600);
}
