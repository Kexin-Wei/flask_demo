from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
@app.route("/test/<name>")
def test(name=None):
    return render_template("test.html", name=name)


def valid_login(username, password):
    if username == "test" and password == "test":
        return True
    else:
        return False


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            return redirect(url_for("test", name=request.form["username"]))
        else:
            error = "Invalid username/password"
    return render_template("login.html", error=error)
