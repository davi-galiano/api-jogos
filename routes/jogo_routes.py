from flask import Blueprint, request, jsonify
from controllers.jogo_controllers import listar_jogos, buscar_jogo, cadastrar_jogo, atualizar_jogo

jogo_bp = Blueprint("jogo_bp", __name__)

@jogo_bp.route("/jogos", methods=["GET"])
def get_jogos():
    return jsonify(listar_jogos())

@jogo_bp.route("/jogos/<int:id>", methods=["GET"])
def get_jogo(id):
    jogo = buscar_jogo(id)
    if jogo:
        return jsonify(jogo)
    return jsonify({"erro": "Jogo não encontrado"}), 404

@jogo_bp.route("/jogos", methods=["POST"])
def post_jogo():
    dados = request.json
    novo_jogo = cadastrar_jogo(dados)
    return jsonify(novo_jogo), 201

@jogo_bp.route("/jogos/<int:id>", methods=["PUT"])
def put_jogo(id):
    dados = request.json
    jogo_atualizado = atualizar_jogo(id, dados)
    if jogo_atualizado:
        return jsonify(jogo_atualizado)
    return jsonify({"erro": "Jogo não encontrado"}), 404
