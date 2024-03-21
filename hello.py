import fileinput

from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from markupsafe import escape
from werkzeug.utils import secure_filename


app = Flask(__name__)

# @app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid

def valid_login():
    return 'valid_login'

def log_the_user_in():
    return 'log_the_user_in'

@app.route('/upload', method=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(f"/var/www/uploads/{secure_filename(fileinput.filename())}")


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'