from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        return 'File uploaded successfully!'
    return render_template('upload.html')

@app.route('/timkiem', methods=['GET', 'POST'])
def tim_kiem():
    if request.method == 'POST':
        search_query = request.form['query']
        return f'Tìm kiếm với từ khóa: {search_query}'
    return render_template('search.html')
if __name__ == '__main__':
    app.run(debug=True,port=5018)

