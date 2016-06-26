from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Test'}
    posts = [
    {
        'author': {'nickname': 'John'},
        'body': 'first'
    },
    {
        'author': {'nickname': 'Susan'},
        'body': 'second'
    }



    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
