class Jogo:
    def __init__(self, id, titulo, genero, desenvolvedor, plataforma):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.desenvolvedor = desenvolvedor
        self.plataforma = plataforma

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "desenvolvedor": self.desenvolvedor,
            "plataforma": self.plataforma
        }
