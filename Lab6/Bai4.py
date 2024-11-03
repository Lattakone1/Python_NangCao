from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    tentruong = '<a href="https://www.vanlanguni.edu.vn">Dai hoc Van Lang!</a><br>'
    nam = datetime.date.today().year
    chuoi = f"{tentruong} <b>Xin <i>chao</i> Tan sinh vien nam {nam}!</b>"
    return chuoi

if __name__ == "__main__":
    app.run()

