from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHHiN]LWX/, PRT*'

class DienTen(FlaskForm):
    ten = StringField('Tên bạn là gì?', validators=[DataRequired()])
    nut_gui = SubmitField('Gửi')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DienTen()
    if form.validate_on_submit():
        ten = form.ten.data
        return f'Tên bạn là: {ten}'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True,port=5091)

