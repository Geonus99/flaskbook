# p306 추가
# from flask import Flask, jsonify, request p307수정
from flask import Blueprint, jsonify, request

from flaskbook_api.api import calculation  # p307 추가

api = Blueprint("api", __name__)  # p307 추가

# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(config[config_name])

#     return app

# p317 추가
@api.get("/")
def index():
    return jsonify({"column": "value"}), 201


# http://localhost:5000에 요청하면 {"column": "value"}를 응답으로 콘솔 화면에 표시


@api.post("/detect")
def detection():
    return calculation.detection(request)