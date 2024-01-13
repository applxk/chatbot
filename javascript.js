function toggleChat() {
    var chatContainer = document.getElementById('chat-container');

    // Toggle the 'visible' class to control visibility
    chatContainer.classList.toggle('visible');

    // Clear chat when closing
    if (!chatContainer.classList.contains('visible')) {
        $('#chat-body').empty();
    }
}

function sendMessage() {
    var userInput = $('input[name="user_message"]').val();

    if (userInput) {
        var chatBody = $('#chat-body');
        var userMessage = '<div class="message user-message"><span class="user-icon">👤</span>' + userInput + '</div>';
        chatBody.append(userMessage);

        // You can implement logic to send the message via AJAX to your Flask server
        $.ajax({
            type: 'POST',
            url: '/chat',
            data: { user_message: userInput },
            success: function (response) {
                if (response) {
                    var botMessage = '<div class="message bot-message"><span class="bot-icon">🤖</span>' + response + '</div>';
                    chatBody.append(botMessage);
                }
            },
            error: function (error) {
                console.error('Error sending message:', error);
            }
        });

        // Clear input field after sending message
        $('input[name="user_message"]').val('');
    }
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent form submission
        sendMessage();
    }
}
