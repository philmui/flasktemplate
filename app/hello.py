from datetime import datetime
from flask import Flask, render_template, session, g
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
logger = logging.getLogger('hello')

class NameForm(Form):
    name = StringField("What is your name?",
                validators=[Required(), Length(1,32)])
    submit = SubmitField('Submit')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True, unique=True)

    def __repr__(self):
        return '<User {0}>'.format(self.name)

#
# request hooks to do auth for all requests
#

@app.before_request
def before_request():
    if not 'pv' in session:
        session['pv'] = 1
    else:
        session['pv'] += 1
    # setting global variable during life of a request cycle
    g.when = datetime.now().strftime('%H:%M:%S')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    newuser = False
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if User.query.filter_by(name=name).first() is None:
            db.session.add(User(name=name))
            db.session.commit()
            newuser = True
    return render_template('user.html', form=form, name=name,
                           newuser=newuser, pv=session['pv'])

#
# mapping of routes are in this map
#      app.url_map
#
if __name__ == '__main__':
    try:
        logger.info("Trying to create all DBs ...")
        db.create_all()
    except:
        logger.warn("DBs have already been created!")
        pass
    app.run(debug=True)
