from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)