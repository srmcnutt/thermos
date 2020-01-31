from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/test')

def index():
    title = "title rendered from template"
    text = "text rendered from template"
    return render_template("index.html", text=text, title=title)


if __name__ == '__main__':
    app.run(debug="true")

