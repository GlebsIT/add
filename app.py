from flask import Flask, render_template
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# from models import Logic
# from sqlalchemy.orm import mapper


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class Logic(db.Model):
    __tablename__ = 'logic_skill'
    id_logic = db.Column(db.Integer, primary_key=True)
    id_parents = db.Column(db.String(64))
    response = db.Column(db.String(120))
    template = db.Column(db.String(128))

    def __repr__(self):
        return '<Response {}>'.format(self.response)


# from models import Logic

@app.route('/')
def main():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = {'username': 'Miguel'}
    return render_template('forms.html', title='Home', user=user, form=form)


@app.route('/add', methods=['GET', 'POST'])
def add():
    skill = Logic(id_parents='01', response='best skills', template='%%')
    db.session.add(skill)
    db.session.commit()
    return render_template('bd.html', title='bd', skill=skill)

@app.route('/info', methods=['GET', 'POST'])
def info():
    logic = Logic.query.all()
    return render_template('info.html', title='Home', logic=logic)


if __name__ == '__main__':
    app.run()
