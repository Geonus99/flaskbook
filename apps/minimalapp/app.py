# flask 클래스를 import한다.
from flask import Flask, render_template, url_for, current_app, g, request

# flask 클래스 인스턴스화한다
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flaskbook!"

@app.route("/hello/<name>", methods=["GET","POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/AK?page=1
    print(url_for("show_name", name="AK", page="1"))

ctx = app.app_context()
ctx.push()

print("current_app.name : "+current_app.name)

g.connection = "connection"
print(g.connection)

with app.test_request_context("/users?updated=true"):
    print(request.args.get("updated"))