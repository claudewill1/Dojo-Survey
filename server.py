from flask import Flask, render_template, session, request, redirect
from env import KEY
app = Flask(__name__)
app.secret_key = KEY

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/result",methods=['POST'])
def results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def getResults():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)