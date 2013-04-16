from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/next')
def next():
    return render_template('next.html')


if __name__ == '__main__':
    app.run(debug = True)
