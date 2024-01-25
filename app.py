from flask import Flask, render_template

app = Flask(__name__)
# comments
@app.route('/')
def index():
    return render_template('index.html', message='HelloWorld!')

if __name__ == '__main__':
    app.run(debug=True)
