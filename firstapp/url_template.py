from flask import Flask,url_for,render_template

app=Flask(__name__)#create instance
#1st route
@app.route("/")
@app.route("/<name>")#defalut
def index(name = None):#we should give none if we use keyword to avoid error
    return render_template("index.html",name=name)#value
#to declare runtime value in html we usw {{value}}
@app.route("/vannako")
def vanako():
    return "vannakam"
@app.route("/contact")
def msg():
    return render_template("contact.html")
@app.route("/user/<name>")#to get value at run time <>
def user(name):
    return f"\n hello\t{name}"

with app.test_request_context(): #builtin func
    print(url_for("vanako"))