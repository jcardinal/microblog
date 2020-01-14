from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Justin'}
    posts = [
        {
            'author': {'username': 'Jen'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Lindsi'},
            'body': 'I like New Orleans'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Little Women movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
