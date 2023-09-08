from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def home():
    return "leocabbage2008 mem folda"


@app.route("/images")
def images():
    return render_template("index.html")


@app.route("/read/<text>")
def nanny(text):
    return f"""lemme read you a bed time story kid
  once upon a time,
  {escape(text)}"""


if __name__ == "__main__":
    app.run(debug=True)
