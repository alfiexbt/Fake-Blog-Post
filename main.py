from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_data = requests.get(blog_url)
blog_post = blog_data.json()


@app.route('/')
def home():
    return render_template("index.html", blog_post=blog_post)


@app.route('/post/<int:num>')
def get_post(num):
    return render_template("post.html", num=num, blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
