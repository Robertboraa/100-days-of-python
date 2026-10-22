from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('index.html', posts=all_posts)

    return render_template("index.html")
@app.route('/post/<int:post_id>')
def post(post_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    for post in all_posts :
        if post['id'] == post_id:
            return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)
