import threading

from Task1Pract2025.website.gradio_frontend import demo
from website import create_app

app = create_app()


def run_gradio():
    demo.launch(server_name="localhost", server_port=7860, share=False)


if __name__ == '__main__':
    threading.Thread(target=run_gradio).start()
    app.run(debug=False)
