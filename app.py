from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ubalubaduba"

@app.route("/hello")
def index():
    flash("Qual o seu nome?")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greet():
    flash('Olá ' + str(request.form['nome']) + ' prazer em vê-lo!')
    return render_template('index.html')

