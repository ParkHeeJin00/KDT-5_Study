from flask import Flask, render_template, Blueprint


### 애플리케이션 팩토리 함수
def create_app():
      app = Flask(__name__)

      # bp등록
      from .views import main_0416
      app.register_blueprint(main_0416.bp)
      
      return app

