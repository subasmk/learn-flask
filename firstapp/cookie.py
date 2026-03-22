from flask import Flask,url_for,render_template,request
from flask import make_response

app=Flask(__name__)#create instance
#1st route
@app.route("/")
def index():
    response=make_response(render_template("cookie.html"))
    response.set_cookie("username","subash")#inbuilt func
    response.set_cookie("password","m76arftz9h")
    print(username,password)
#we can see the cookie in inspect->application->cookie storage
    return response
