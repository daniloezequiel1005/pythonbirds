class Pessoa:
    def __init__(self, *filhos, nome = None, idade=22):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Danilo = Pessoa(nome='Danilo')
    Simone = Pessoa(Danilo, nome='Simone')
    print(Pessoa.cumprimentar(Simone))
    print(id(Simone))
    print(Simone.cumprimentar())
    print(Simone.nome)
    print(Simone.idade)
    for filho in Simone.filhos:
        print(filho.nome)