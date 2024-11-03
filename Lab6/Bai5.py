from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Day la trang mon hoc!'

@app.route('/monhoc')
def learn():
    return "Day la trang mon hoc!"

if __name__ == "__main__":
    app.run(port=5050)


