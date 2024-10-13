function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    if (userInput.trim() === "") {
        return;
    }
    document.getElementById("userInput").value = "";  // Clear input

    // Add user message to the chatbox
    let chatbox = document.getElementById("chatbox");
    let userMessage = `<p><strong>You:</strong> ${userInput}</p>`;
    chatbox.innerHTML += userMessage;

    // Send user input to Flask server for response
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = `<p><strong>Bot:</strong> ${data.response}</p>`;
        chatbox.innerHTML += botMessage;
        chatbox.scrollTop = chatbox.scrollHeight;  // Auto-scroll to the bottom
    });
}
