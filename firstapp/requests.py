from flask import Flask,url_for,render_template,request

app=Flask(__name__)#create instance
#1st route
@app.route("/")
@app.route("/<name>")#defalut
def index(name = None):#we should give none if we use keyword to avoid error
    return render_template("index.html",name=name)#value
#to create login page
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':#if its ture it returnn email is ----giveb
        email=request.form.get("email")#to show in backend {that name should be same as in name inn html file
        passs=request.form.get("passs")
        return f"email is {email}"
    return render_template("login.html")