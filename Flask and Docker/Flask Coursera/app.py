#FLASK API (COURSERA)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', out=text)

@app.route('/', methods=['POST'])
def index1():
    text = request.form['text']
    return render_template('index.html', out='text')


if __name__ == '__main__':
    app.run(debug=True)