# application.py
from flask import Flask, render_template, request, redirect, url_for
from config import Config
from database import init_db
from services import create_user

app = Flask(__name__)
app.config.from_object(Config)
init_db(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_user', methods=['GET', 'POST'])
def create_user_route():
    if request.method == 'POST':
        username = request.form['username']
        try:
            create_user(username)
            return redirect(url_for('index'))
        except ValueError as e:
            return str(e)  # Có thể cải thiện bằng cách hiển thị lỗi trên trang
    return render_template('create_user.html')
if __name__ == '__main__':
    app.run(debug=True,port=5013)


