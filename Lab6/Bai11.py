from flask import Flask, redirect, url_for, abort

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)

@app.route('/error/401')
def error_401():
    return "Unauthorized access - You don't have permission to access this resource.", 401

if __name__ == '__main__':
    app.run(debug=True)



