from flask import Flask, render_template

app = Flask(__name__, static_folder='D:\\Lập trình Python nâng cao\\Lab6\\flask_covid\\templates\\static')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
