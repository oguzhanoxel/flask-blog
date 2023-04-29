from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<p>Hello, Home Page</p>"


@app.route("/about")
def about():
    return "<p>About Page</p>"


if __name__ == '__main__':
    app.run(debug=True)
