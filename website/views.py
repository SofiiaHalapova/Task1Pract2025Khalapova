from flask import Blueprint, render_template, redirect

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def view():
    return render_template('base.html')


@views.route('/gradio')
def gradio():
    return redirect("http://localhost:7860")