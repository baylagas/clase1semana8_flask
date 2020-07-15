from flask import Flask, render_template, request, redirect, session
from MethodUtil import MethodUtil


app = Flask(__name__)
app.secret_key = "python es bien chivo"


@app.route("/")
def hello():
    if "username" in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in"


#                    methods=["GET", "POST"]
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        print(MethodUtil.list_ALL())
        session["username"] = "balbino"
    return "Now you are log in"


@app.route("/logout", methods=MethodUtil.list_ALL())
def logout():
    session.pop("username", None)
    return "Now you are logged out"


@app.route("/loginform", methods=MethodUtil.list_ALL())
def loginform():
    if request.method == "GET":
        return render_template("loginform.html")
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        print(password)
        return render_template("dashboard.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True)
