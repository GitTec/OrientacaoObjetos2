
class Carro:
    marca=""
    placa=""
    cor=""
    qtdPortas=""
    anoFab=int

    def ligar(self):
        print(f"Estou ligando o meu {self.marca}")


    def dirigir(self):
        print(f"Estou dirigindo um {self.marca} {self.cor}")


    def acelerar(self):
        print(f"Acelerei a todo o vapor meu {self.marca}")