### => 기능 : main 범주의 url 라우팅 처리
### => URL : /main, /main/info, /main/about, .....

from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/main/') # '별칭'

@bp.route('about')
def about():
    return 'ABOUT MAIN'

@bp.route('info')
def info():
    return 'info'

@bp.route('')
def main():
    return 'main'
