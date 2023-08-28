class contabancaria:
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    def depositar(self, deposito):
        self.saldo += deposito
        def sacar(self, saque):
            if saque <= self.saldo:
                self.saldo -= saque
    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self.titular}:"
              f" R${self.saldo}")

conta1 = contabancaria("Ana", "12345")
a= int(input('Digite o valor que você deseja sacar:'))
conta1.depositar(1000)
conta1.sacar(a)
conta1.exibir_saldo()