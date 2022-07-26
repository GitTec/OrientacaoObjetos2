class Papagaio:
    nome = ""
    cor = ""
    peso = 0
    comprimento = 0

    def falar(self, frase):
        print(f"OLÁ MEU NOME É {self.nome} E {frase}")

    def voar(self):
        print(f"ESTOU VOANDO")

    def andar(self):
        print(f"ESTOU ANDANDO")

    def alimentar(self, comida):
        if comida == "PAO":
            print(f"EU TENHO CARA DE COMER PÃO?")
        else:
            print(f"HUUMM, MEU PESO FICA {self.peso + 1} QUANDO ESTOU COMENDO {comida}")
