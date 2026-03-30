from flask import Flask,url_for,render_template,url_for,abort
from flask import session,request
app=Flask(__name__)#create instance
app.secret_key=b"m76arftz9h"
@app.route("/")
def index(name = None):
    if 'username' in session:
        return f'loggined in as {sessiom["username"]}'
    return f"not logged"
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return ''''''
