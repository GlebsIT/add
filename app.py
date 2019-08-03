from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def main():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = {'username': 'Miguel'}
    return render_template('forms.html', title='Home', user=user, form=form)

if __name__ == '__main__':
    app.run()
