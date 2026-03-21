from flask import Flask

app=Flask(__name__)#create instance
#1st route
@app.route("/")#defalut
def index():
    return "This will be default"
@app.route("/vannako")
def vanako():
    return "vannakam"
@app.route("/contact")
def msg():
    return "8778149499"
@app.route("/user/<name>")#to get value at run time <>
def user(name):
    return f"\n hello\t{name}"
@app.route("/uid/<int:uid>")#to get declare data type type:
def uid(uid):
    return f"\n ur id\t{uid}"
#we can declare path as data type to redirect to site

