from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ubalubaduba"

@app.route("/")
def index():
    flash("Qual o seu nome?")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greet():
    flash('Olá ' + str(request.form['nome']) + ' prazer em vê-lo!')
    return render_template('index.html')
    
@app.route("/ranking")
def ranking():
    #pegar dados do banco
    return render_template("ranking.html")
     
@app.route("/esqueleto")
def esqueleto():
    return render_template("esqueleto.html")
    
@app.route("/mobile")
def mobile():
    return render_template("mobile.html")