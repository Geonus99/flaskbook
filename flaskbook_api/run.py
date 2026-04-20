# p306 추가 config 읽어들이고 플라스크 앱 만들기
import os

from flask import Flask  # p307 추가

# from flaskbook_api.api import create_app p307 수정
from flaskbook_api.api import api
from flaskbook_api.api.config import config

# create_app은 __init__.py에 작성함
# config = os.environ.get("CONFIG", "local") p307 수정
config_name = os.environ.get("CONFIG", "local")

# app = create_app(config) p307 수정
app = Flask(__name__)
app.config.from_object(config[config_name])

# blueprint를 애플리케이션에 등록 p307 추가
app.register_blueprint(api)