from flask import render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'tyc'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', posts=posts, title='Home', user=user)


@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', title='login', form=login_form)
