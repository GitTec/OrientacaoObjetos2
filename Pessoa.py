class Pessoa:
    nome = ""
    idade = 0
    cpf = ""
    rg = ""


    def andar(self):
        print(f"{self.nome} ESTOU ANDANDO")


    def baterPalma(self):
        print(f"{self.nome} ESTA BATENDO PALMA")


    def cumprimentar(self, nome):
        print(f"OLÁ {nome}")

    def falar(self, frase):
        print(frase)

    def apresentacao(self):
        print(f"OLÁ MEU NOME É {self.nome} E TENHO {self.idade} ANOS")


#métodos comprimentar que vai receber o nome da pessoa que comprimenta
#método apresentear que diz olá meu nome é ...
#método andar e bater palma, estou andando
#fazer aniversario, aumenta a idade em 1

