class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

aluno = aluno("Ana Luiza", 8.5, 8.0)
media = aluno.calcular_media()
print(f"A média da aluna {aluno.nome} é: {media}")