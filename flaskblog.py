from flask import Flask, render_template, url_for, flash, redirect
from forms import (
    RegistrationForm,
    LoginForm
)

app = Flask(__name__)

app.config['SECRET_KEY'] = '8d2a6521f03ceedca671b1ced60c31c1'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@example.com' and form.password.data == '123456':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
