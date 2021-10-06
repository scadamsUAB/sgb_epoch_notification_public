from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    f=open("log.txt","r")
    last_log=f.read()

    return "<H2>Welcome to the basic Web interface to check Epoch Status <p>"+str(last_log)+"</p>"

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')