import gradio as gr

from Task1Pract2025.website.views import chat

gradio_port = None

demo = gr.Interface(fn=chat,
                    inputs=gr.components.Textbox(label='User'),
                    outputs=gr.components.Textbox(label='Chat'))

demo.launch()