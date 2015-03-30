from datetime import datetime
from flask import Flask, render_template, session, g
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField("What is your name?",
                validators=[Required(), Length(1,32)])
    submit = SubmitField('Submit')

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
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('user.html', form=form, name=name, pv=session['pv'])

#
# mapping of routes are in this map
#      app.url_map
#
if __name__ == '__main__':
    app.run(debug=True)
