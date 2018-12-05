from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']= 'eb69c8bfa9ed26d632149db8322b3682'

posts = [
    {
        'author': 'Carlos Ortega',
        'title': 'Movie Post 1',
        'content': 'bad movie',
        'datePosted': 'December 1, 2018'
    },
    {
        'author': 'Carlos Ortega',
        'title': 'Movie Post 2',
        'content': "bad movie don't go",
        'datePosted': 'December 2, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title= 'About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return  render_template('register.html', title= 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return  render_template('login.html', title= 'Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)