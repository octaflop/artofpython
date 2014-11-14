# encoding: utf-8

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from flask import Flask, Response, render_template, url_for

from db import db

app = Flask(__name__)

@app.route("/")
def index():
    ctx = {}
    ctx['presentation'] = "The art of python"
    ctx['author'] = "Faris Chebib"
    template_name = "index.html"
    ctx['impress'] = url_for('static', filename='js/impress.js')
    ctx['slides'] = db['slides']
    return render_template(template_name, **ctx)

@app.route("/pygments.css")
def codecss():
    ctx = {}
    css = HtmlFormatter(style='colorful').get_style_defs()

    response = Response(css, mimetype="text/css")
    return response


if __name__ == "__main__":
    app.debug = True
    app.run()
