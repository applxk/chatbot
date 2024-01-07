from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Default greeting message
    default_message = "Hello! I'm a chatbot. How can I assist you today?"
    return render_template('index.html', default_message=default_message)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    response = generate_response(user_message)
    return {'bot_message': response}

def generate_response(user_message):
    # Convert user message to lowercase for case-insensitive matching
    user_message_lower = user_message.lower()

    if any(greeting in user_message_lower for greeting in ['hi', 'hello', 'hey']):
        return "Greetings! How can I help you?"

    elif 'how are you' in user_message_lower:
        return "I'm just a chatbot, but thanks for asking!"

    elif 'language' in user_message_lower:
        return "I currently understand only English. Please use Google Translate if needed."

    elif 'paper bag' in user_message_lower:
        reference_link = 'https://www.example.com/products/paper-bag'
        return f"Sure! You can find details about the paper bag [here]({reference_link}).\n\nAre there any other inquiries?"

    elif 'polymailer' in user_message_lower:
        reference_link = 'https://www.example.com/products/polymailer'
        return f"Sure! You can find details about the polymailer [here]({reference_link}).\n\nAre there any other inquiries?"

    elif 'plastic bag' in user_message_lower:
        reference_link = 'https://www.example.com/products/plastic-bag'
        return f"Sure! You can find details about the plastic bag [here]({reference_link}).\n\nAre there any other inquiries?"

    else:
        # Check if the message is not in English
        if not is_english(user_message_lower):
            return "Sorry, I only understand English. Please use Google Translate to English and send in the response. Thank you."

        return "I'm not sure how to respond to that. Can you please be more specific?"

def is_english(text):
    # This function checks if the text is in English
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

if __name__ == '__main__':
    app.run(debug=True)
