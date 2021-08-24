from flask import Flask,render_template,flash, request, redirect, url_for
import subprocess as sp
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    cmd=request.form.get('dropdown_cmds')
    res=sp.getstatusoutput(cmd)
    res=res[1].split('\n')
    return render_template("index.html",results=res)

@app.route("/")
def up():
    return render_template("index.html")

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.debug = True
    app.run()