from flask import Flask, render_template, Blueprint


### 애플리케이션 팩토리 함수
def create_app():
      app = Flask(__name__)

      # bp등록
      from .views import view
      app.register_blueprint(view.dataBP)


      @app.route('/')
      def index():
            return render_template('index.html')

      return app

