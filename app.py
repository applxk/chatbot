from flask import Flask, render_template, request, jsonify
import random
import string
import datetime

app = Flask(__name__)

#wheel
@app.route('/wheel')
def wheel():
    return render_template('includes/wheel.html')

@app.route('/spin', methods=['POST'])
@app.route('/spin', methods=['POST'])
def spin_wheel():
    # Assuming your promo codes are alphanumeric strings of length 8
    promo_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # Append the generated promo code to the list
    generated_promo_codes.append(promo_code)

    return jsonify({'promo_code': promo_code})


#coupons

# List to store generated promo codes
generated_promo_codes = []

@app.route('/mycoupons')
def my_coupons():
    return render_template('includes/mycoupons.html', promo_codes=generated_promo_codes)


#chatbot
@app.route('/')
def home():
    # Default greeting message
    default_message = "Hello! I'm a chatbot. How can I assist you today?"
    return render_template('includes/index.html', current_url=request.path)

# List to store chat messages
chat_messages = []

# start chatbot
@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form.get('user_input')

    if user_input:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f'[{timestamp}] User: {user_input}'

        chat_messages.append(formatted_message)

        # You can add further processing or send the message to your chatbot logic here

        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Empty message'})

@app.route('/get_messages')
def get_messages():
    return jsonify({'messages': chat_messages})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    user_message_lower = user_message.lower()

    if any(greeting in user_message_lower for greeting in ['hi', 'hello', 'hey']):
        return "Greetings! How can I help you?"

    elif 'how are you' in user_message_lower:
        return "I'm just a chatbot, but thanks for asking!"

    elif any(greeting in user_message_lower for greeting in ['bye', 'goodbye']):
        return "Bye! Have a good day!"

    elif 'language' in user_message_lower:
        return "I currently understand only English. Please use Google Translate if needed."

    elif 'paper bag' in user_message_lower:
        reference_link = 'https://www.example.com/products/paper-bag'
        return f"Sure! You can find details about the paper bag [here]({reference_link}). <br> Are there any other inquiries?"

    elif 'polymailer' in user_message_lower:
        reference_link = 'https://www.example.com/products/polymailer'
        return f"Sure! You can find details about the polymailer [here]({reference_link}). <br> Are there any other inquiries?"

    elif 'plastic bag' in user_message_lower:
        reference_link = 'https://www.example.com/products/plastic-bag'
        return f"Sure! You can find details about the plastic bag [here]({reference_link}). <br> Are there any other inquiries?"

    else:
        # Check if the message is not in English
        if not is_english(user_message_lower):
            return "Sorry, I only understand English. Please use Google Translate to English and send in the response. Thank you."

        return "I'm not sure how to respond to that. Can you please be more specific?"

def is_english(text):
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


#membership
@app.route('/membership')
def membership():
    return render_template('includes/membership.html')

@app.route('/update_image', methods=['POST'])
def update_image():
    try:
        number = int(request.form.get('number'))

        # Perform any logic with the entered number (e.g., update image)
        # For demonstration purposes, we'll just check if the number is even.
        success = number % 2 == 0

        return jsonify(success=success)

    except ValueError as ve:
        return jsonify(error=f"Invalid number provided: {str(ve)}")

    except Exception as e:
        return jsonify(error=f"An error occurred: {str(e)}")

@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    try:
        current_month = datetime.datetime.now().month
        selected_month = int(request.form['month'])

        eligible = selected_month == current_month
        return jsonify({'eligible': eligible})

    except Exception as e:
        print(str(e))
        return jsonify({'error': 'An error occurred'})

if __name__ == '__main__':
    app.run(debug=True)
