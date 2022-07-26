
class Caneta:
    marca=""
    cor=""
    qtdTinta=0
    tipoBico=""

    def tampar(self):
        print(f"A CANETA {self.cor} ESTÁ TAMPADA")

    def rabiscar(self):
        print(f"A CANETA DE BICO {self.tipoBico} ESTÁ RABISCANDO")

    def escrever(self, mensagem):
        print(f"{self.marca} --> A MARCA {mensagem}")


