from models.jogo import Jogo

jogos = []
contador_id = 1

def listar_jogos():
    return [jogo.to_dict() for jogo in jogos]

def buscar_jogo(id):
    for jogo in jogos:
        if jogo.id == id:
            return jogo.to_dict()
    return None

def cadastrar_jogo(dados):
    global contador_id
    novo_jogo = Jogo(contador_id, dados["titulo"], dados["genero"], dados["desenvolvedor"], dados["plataforma"])
    jogos.append(novo_jogo)
    contador_id += 1
    return novo_jogo.to_dict()

def atualizar_jogo(id, dados):
    for jogo in jogos:
        if jogo.id == id:
            jogo.titulo = dados.get("titulo", jogo.titulo)
            jogo.genero = dados.get("genero", jogo.genero)
            jogo.desenvolvedor = dados.get("desenvolvedor", jogo.desenvolvedor)
            jogo.plataforma = dados.get("plataforma", jogo.plataforma)
            return jogo.to_dict()
    return None
