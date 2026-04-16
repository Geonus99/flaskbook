from pathlib import Path
from flask_login import LoginManager
from apps.config import config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
csrf = CSRFProtect()

# Login_Manager를 인스턴스화한다.
login_manager = LoginManager()
# login_view 속성에 미로그인 시 리다이렉트하는 엔드포인트를 지정한다
login_manager.login_view = "auth.signup"
# login_message 속성에 로그인 후에 표시할 메세지를 지정한다
# 여기에서는 아무것도 표시하지 않도록 공백을 지정한다
login_manager.login_message=""


def create_app(config_key="local"):
    # 플라스크 인스턴스 생성
    app = Flask(__name__)

    app.config.from_object(config[config_key])
    # 앱의 config 설정을 한다. 138p 제거
    # app.config.from_mapping(
    #     SECRET_KEY="flaskbooktest",
    #     SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
    #     SQLALCHEMY_TRACK_MODIFICATIONS=False,

    # # SQL을 콘솔 로그에 출력하는 설정
    #     SQLALCHEMY_ECHO=True,
    #     WTF_CSRF_SECRET_KEY="AuwzyszU5sugKN7KZs6f"
    # )

    csrf.init_app(app)
    # SQLAlchmey와 앱을 연계한다
    db.init_app(app)
    # Migrate와 앱을 연계한다
    Migrate(app, db)
    # login_manager를 애플리케이션과 연계한다.
    login_manager.init_app(app)

    # 🚨 이 한 줄이 핵심입니다! 모델을 불러와야 Migrate가 인식해요.
    from apps.crud import models as crud_models

    from apps.crud import views as crud_views

    # register_blueprint를 사용해 views의 crud를 앱에 등록한다
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # 이제부터 작성하는 auth 패키지로부터 views를 import한다
    from apps.auth import views as auth_views

    # register_blueprint를 사용해 views의 auth를 앱에 등록한다
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    # 이제부터 작성하는 detector 패키지로부터 views를 import한다
    from apps.detector import views as dt_views

    # register_blueprint를 사용해 views의 dt를 앱에 등록한다
    app.register_blueprint(dt_views.dt)

    return app