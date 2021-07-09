
from flask import Flask, redirect, url_for, render_template # for html templates

#redirect and url_4 allow for returning of redirect 


app = Flask(__name__)
# app decorator
@app.route("/")
def home():
    return render_template("home.html")


'''
# decorator placed user
@app.route("/<name>")
def user(name):
    return f"hello, {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="ashwin"))
'''


if __name__ == "__main__":
    app.run()