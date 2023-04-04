from flask import render_template, url_for, flash, redirect
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog import app
from flaskblog.models import User, Post


posts = [
    {
        "author": "Nole_19",
        "title": "First post",
        "content": "Why Flask?",
        "date": "29.03.2023"
    },
    {
        "author": "Kain",
        "title": "Second post",
        "content": "Ideas for site",
        "date": "30.03.2023"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}, 'success")
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)
