from flask import Flask, make_response, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400

@app.route('/cookie')
def set_cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('redirected'))

@app.route('/redirected')
def redirected():
    return '<h1>You have been redirected!</h1>'

if __name__ == '__main__':
    app.run(debug=True)









