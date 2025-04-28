import gradio as gr
import requests

gradio_port = None

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
LLM_NAME = "mistral-7b-instruct-v0.3"


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


demo = gr.Interface(fn=chat,
                    inputs=gr.components.Textbox(label='User'),
                    outputs=gr.components.Textbox(label='Chat'))

