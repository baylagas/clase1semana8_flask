from flask import Flask, render_template, request, redirect, session
from MethodUtil import MethodUtil
from userlogic import UserLogic
from userobj import UserObj
from werkzeug.security import generate_password_hash, check_password_hash


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
        return render_template("loginform.html", message="")
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        print(password)
        print(generate_password_hash(password))
        print(
            check_password_hash(
                "pbkdf2:sha256:150000$Q5PULnGV$bdc51198ad18432f00fea6a5cb59bec4d7977cb28d3e7ef575bab3b93bfa9628",
                "12345",
            )
        )
        logic = UserLogic()
        userdata = logic.getUserData(user)
        # session["user"] = userdata
        if userdata is not None:
            if userdata.password == password:
                if userdata.role == "admin":
                    return render_template(
                        "dashboard_admin.html", userdata=userdata.user
                    )
                else:
                    return render_template(
                        "dashboard_user.html", userdata=userdata.user
                    )
            else:
                return render_template("loginform.html", message="hubo error")
        else:
            return render_template("loginform.html", message="hubo error")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True)
