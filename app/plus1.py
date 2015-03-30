from flask import Flask, render_template, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'


@app.route('/plus1')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('plus1.html', count=session['count'])


if __name__ == '__main__':
    app.run(debug=True)
