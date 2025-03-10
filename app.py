from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    post = response.json()[blog_id - 1]
    return render_template("post.html", post=post)


if __name__ == '__main__':
    app.run()
