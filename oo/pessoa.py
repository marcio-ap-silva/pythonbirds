class Pessoa:
    def __init__(self, *filhos, nome=None, idade=43):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    diogo = Pessoa(nome='Diogo')
    marcio = Pessoa(diogo, nome='Marcio')
    print(Pessoa.cumprimentar(marcio))
    print(id(marcio))
    print(marcio.cumprimentar())
    print(marcio.nome)
    print(marcio.idade)
    for filho in marcio.filhos:
        print(filho.nome)
