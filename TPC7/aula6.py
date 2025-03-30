import json
from flask import Flask, request, redirect, url_for, render_template
import re

app = Flask(__name__)
@app.route('/') 
def hello_world():
    return render_template("home.html")


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

@app.post("/conceitos")
def adicionar_conceito():
    descricao = request.form.get("descricao")
    designacao = request.form.get("designacao")

    db[designacao] = descricao
    f_out = open("conceitos_.json", "w")
    json.dump(db,f_out,indent=4,ensure_ascii=False)
    f_out.close()

    designacoes = sorted (list(db.keys()))
    return render_template("conceitos.html",  designacao=designacao, descricao=db[designacao], title="Lista de Conceitos")

@app.route("/pesquisar")
def pesquisar():
    termo = request.args.get("termo", "").strip().lower()
    encontrados = []

    if termo:
        for designacao, descricao in db.items():
            descricao_lower = descricao.lower()

            if termo == designacao.lower():
                encontrados.append((designacao, descricao))
                continue
            
            if termo in descricao_lower.split():
                # Destaca o termo na descrição
                palavras = descricao.split()
                descricao_destacada = " ".join(
                    [f"<mark class='highlight'>{palavra}</mark>" if palavra.lower() == termo else palavra for palavra in palavras]
                )
                encontrados.append((designacao, descricao_destacada))
    
    return render_template("pesquisar.html", termo=termo, resultados=encontrados)
    
@app.delete("/conceitos/<designacao>")
def delete_conceito(designacao):
    if designacao in db:
        del db[designacao]
        f_out=open("conceitos_.json", "w")
        json.dump(db, f_out, indent=4, ensure_ascii=False)
        f_out.close()
        return {"success":True,"message": "Conceito apagado com Sucesso!", "redirect_url": "/conceitos"}
    else:
        return{"success":False, "message":"Not Found", "data":designacao }


@app.route("/tabela")
def conceitos_tabela():
    return render_template("tabela.html", db=db, title="Tabela de Conceitos")

app.run(host="0.0.0.0", port=4002, debug=True)
