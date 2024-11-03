# application.py
from flask import Flask, render_template, redirect, url_for
from hello import NameForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return redirect(url_for('greet', username=name))
    return render_template('home.html', form=form)

@app.route('/greet/<username>')
def greet(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(debug=True,port=5011)
