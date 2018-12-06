from flask import Flask, render_template, url_for, flash, redirect
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
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)











