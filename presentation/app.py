# encoding: utf-8

from flask import Flask, render_template, url_for

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

if __name__ == "__main__":
    app.debug = True
    app.run()
