from flask.globals import request
from flask import Flask, render_template
from tempo import Tempo


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    """Função que exibi a pagina inicial"""

    return render_template("index.html")


@app.route("/buscar", methods=["GET", "POST"])
def mostrar_informacoes():
    """Função que irá exibir as informações do clima do Estado
    que for informado"""

    # Cria um objeto da classe tempo
    tempo = Tempo(request.form["nome"])

    # retorna as informações em uma nova pagina
    return render_template("info_estado.html",
    nome = tempo.nome, geral = tempo.exibir_informacoes_tempo())


@app.errorhandler(AttributeError)
def exibir_pagina_erro(e):
    """Função que irá redirecionar para pagina de erro, 
    caso o usuário digite um estado inválido"""

    return render_template("erro.html")


if __name__ == "__main__":
    app.run(debug=True)