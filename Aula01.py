from Pessoa import Pessoa

pessoa1 = Pessoa()
pessoa1.nome="José"
pessoa1.idade=10

pessoa2 = Pessoa()
pessoa2.nome="Maria"
pessoa2.idade=15

print(f"OLÁ MEU NOME É {pessoa1.nome}")
print(f"OLÁ MEU NOME É {pessoa2.nome}")
pessoa2.nome="Carla"
print(f"OLÁ MEU NOME É {pessoa2.nome}")

pessoa2.andar()
pessoa1.baterPalma()
pessoa2.cumprimentar("francisco")
pessoa2.falar(frase="Estou aprendendo POO")
pessoa2.apresentacao()