from flask import Blueprint, render_template, request, jsonify
import requests

views = Blueprint('views', __name__)
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
LLM_NAME = "mistral-7b-instruct-v0.3"


@views.route('/', methods=['GET'])
def view():
    return render_template('base.html')


@views.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')

    if not user_input:
        return jsonify({'error': 'No user_input'}), 400

    data = {
        "model": LLM_NAME,
        "messages": [{"role": "user", "content": user_input}]
    }

    response = requests.post(LM_STUDIO_URL, json=data)

    response.raise_for_status()

    response_data = response.json()
    answer = response_data['choices'][0]['message']['content']

    return jsonify({'response': answer})


