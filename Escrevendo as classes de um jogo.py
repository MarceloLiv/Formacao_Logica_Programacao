#Metodo construtor
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()

    def atacar(self):
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }
        ataque = ataques.get(self.tipo, "um ataque desconhecido")
        print(f"O {self.tipo} atacou usando {ataque}")

# Exemplo de uso
heroi1 = Heroi("Marcelo", 40, "Guerreiro")
heroi2 = Heroi("Felipão", 50, "Mago")
heroi3 = Heroi("Leonardo", 70, "Monge")
heroi4 = Heroi("Vitor", 30, "Ninja")

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
