from click import prompt
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app=Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():
    prompts = story.prompts
    return render_template("homepage.html", prompts = prompts)

@app.route("/story")
def make_story():       
    your_story = story.generate(request.args)
    return render_template("story.html", your_story = your_story)
