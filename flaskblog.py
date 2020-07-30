from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'April 21, 2018',
    },
    {
        'author': 'Ahmed Jan',
        'title': 'Special Blog post',
        'content':'Special Post Content',
        'date_posted': 'July 30, 2020'
    }

    ]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)
@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
    app.run(debug=True)
