from flask import Blueprint, render_template

# 블루프린트의 별칭, __name__, url_prefix
bp = Blueprint('main_0416', __name__, url_prefix='/')

@bp.route('/')
def root():
    # html불러오기
    return render_template('index.html')

@bp.route('/hj')
def model():
    # html불러오기
    return render_template('hj.html')