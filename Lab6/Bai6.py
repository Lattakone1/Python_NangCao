from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Đây là trang môn học Python!"
@app.route('/monhoc/')
def learn():
    return "Đây là trang môn học Python!"
@app.route('/monhoc/<tenmon>')
def subjects(tenmon):
    chuoi = "Đây là trang môn học Python"
    monhoc = str(tenmon).upper()
    if monhoc == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + monhoc
    return chuoi
@app.route('/sinhvien/<kho>')
def sinhvien(kho):
    return f"Trang của sinh viên khóa {kho}"
if __name__ == '__main__':
    app.run(host='localhost', port=5050)
