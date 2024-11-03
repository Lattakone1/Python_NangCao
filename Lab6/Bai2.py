from flask import Flask
ungdung = Flask(__name__)
@ungdung.route('/')
def hello():
    return ('Xin chao!')
if __name__ == "__main__":     # (lưu ý là 2 dấu gạch dưới _ ở mỗi vị trí name và main)
   ungdung.run()