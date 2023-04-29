from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Oğuzhan Öksel',
        'title': 'An Title',
        'content': 'an content about nothing',
        'date_posted': 'April 29, 2023',
    },
    {
        'author': 'Elfo',
        'title': 'Hi I\'m Elfo',
        'content': 'an content about Elfo',
        'date_posted': 'November 19, 2022',
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
