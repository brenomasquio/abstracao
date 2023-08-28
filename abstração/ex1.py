class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa('Ana Luiza',17)
pessoa2 = Pessoa('Breno',17)
print("O nome da primeira pessoa é:", pessoa1.nome)