from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        message = f"Welcome back, {username}!"
    else:
        message = "Hello, new user!"
    return render_template('index.html', message=message)

@app.route('/setcookie')
def set_cookie():
    resp = make_response(render_template('index.html', message="Cookie has been set!"))
    resp.set_cookie('username', 'the_username')
    return resp
if __name__ == '__main__':
    app.run(debug=True,port=5024)
