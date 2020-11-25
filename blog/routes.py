from flask import Flask, render_template, url_for, flash, redirect
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post



posts = [
    {
        'author': 'Gitika Jha',
        'title': 'Blog Post 1',
        'content':'First Blog Post content',
        'date_posted': 'September 11, 2020'
    },
    {
        'author': 'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second Blog Post content',
        'date_posted': 'September 10, 2020'
    }
]

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('homepage.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Your account has been created. Please log in now', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Login failed. Please enter valid details', 'danger')
    return render_template('login.html', title='Login', form=form)

