from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHHiN]LWX/, PRT*'
@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {escape(session["username"])}'
    return 'You are not logged in'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type="text" name="username" placeholder="Enter username"></p>
            <p><input type="submit" value="Login"></p>
        </form>
    '''
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
