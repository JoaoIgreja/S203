class Filme:
    def __init__(self, titulo, ano_lancamento, diretor, genero, duracao):
        self._titulo = titulo
        self._ano_lancamento = ano_lancamento
        self._diretor = diretor
        self._genero = genero
        self._duracao = duracao

    def __str__(self):
        return f"{self._titulo} ({self._ano_lancamento}) - {self._diretor}"

    def get_titulo(self):
        return self._titulo

    def get_ano_lancamento(self):
        return self._ano_lancamento

    def get_diretor(self):
        return self._diretor

    def get_genero(self):
        return self._genero

    def get_duracao(self):
        return self._duracao
