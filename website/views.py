from flask import Blueprint, render_template, redirect
import requests

views = Blueprint('views', __name__)

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
# LLM_NAME = "mistral-7b-instruct-v0.3"
LLM_NAME = "llama-3.2-1b-instruct"


@views.route('/', methods=['GET'])
def view():
    return render_template('base.html')


@views.route('/gradio')
def gradio():
    return redirect("http://localhost:7860")


def chat(user_input):
    if not user_input:
        return "error: No user_input"

    data = {
        "model": LLM_NAME,
        "messages": [{"role": "user", "content": user_input}]
    }

    try:
        response = requests.post(LM_STUDIO_URL, json=data)

        response.raise_for_status()

        response_data = response.json()
        answer = response_data['choices'][0]['message']['content']

        return answer
    except Exception as e:
        return f"Exception: {str(e)}"
