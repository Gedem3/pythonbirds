class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    glauco = Pessoa(nome='Glauco')
    salete = Pessoa(glauco, nome='Salete')
    print(Pessoa.cumprimentar(salete))
    print(id(salete))
    print(salete.cumprimentar())
    print(salete.nome)
    print(salete.idade)
    for filho in salete.filhos:
        print(filho.nome)
    salete.sobrenome = 'Duarte'
    del salete.filhos
    salete.olhos = 3
    del salete.olhos
    print(salete.__dict__)
    print(glauco.__dict__)
    Pessoa.olhos = 4
    print(Pessoa.olhos)
    print(salete.olhos)
    print(glauco.olhos)
    print(id(Pessoa.olhos), id(glauco.olhos), id(salete.olhos))


