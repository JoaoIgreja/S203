from filme import Filme


class CatalogoFilmes:
    def __init__(self):
        self._filmes = []

    def adicionar_filme(self, filme):
        self._filmes.append(filme)

    def listar_filmes(self):
        return self._filmes

    def buscar_por_ano(self, ano):
        return [filme for filme in self._filmes if filme.get_ano_lancamento() == ano]

    def buscar_por_genero(self, genero):
        return [filme for filme in self._filmes if filme.get_genero() == genero]

    def buscar_por_diretor(self, diretor):
        return [filme for filme in self._filmes if filme.get_diretor() == diretor]
