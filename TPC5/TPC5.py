import json
from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)
@app.route('/') 
def hello_world():
    return '<p>Hello World!</p>'


db_file=open('conceitos_.json', "r", encoding="utf-8")
db=json.load(db_file)
db_file.close()
@app.route('/api/conceitos')
def conceitos():
    return (db)


@app.route('/api/conceitos/<designacao>')
def api_conceito(designacao):
    return {"designacao":f'{designacao}', "descricao":db[designacao]}


@app.route('/conceitos')
def adiciona_conceito():
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Designações")

@app.route('/conceitos/<designacao>')
def api_conceito_designacao(designacao):
    return render_template("conceito_descricao.html", designacao=designacao, descricao=db[designacao], title="Conceito e desginação")


app.run(host="localhost",port=4002,debug=True)