from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Đây là trang con môn học 2021!"

@app.route('/monhoc/')
def learn():
    return "Đây là trang môn học 2021!"

@app.route('/monhoc/<tenmon>')
def subjects(tenmon):
    chuoi = "Đây là trang môn học"
    monhoc = str(tenmon).upper()
    if monhoc == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + monhoc
    return chuoi

@app.route('/sinhvien/<int:kho>/<string:namsinh>')
def sinhvien(kho, namsinh):
    return f"Trang của sinh viên khóa {kho}, năm sinh {namsinh}."

@app.route('/sinhvien/<int:kho>')
def sinhvien_kho(kho):
    return f"Trang của sinh viên khóa {kho}."

@app.route('/sinhvien/<int:kho>/<float:namsinh>')
def sinhvien_year(kho, namsinh):
    return f"Trang của sinh viên khóa {kho}, năm học {namsinh:.2f}."

if __name__ == '__main__':
    # Chạy ứng dụng trên cổng 5050
    app.run(host='localhost', port=5050)
