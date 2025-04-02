# Formacao_Logica_Programacao

# Desafio 1 - Classificador de Nível de Herói

# Classificação dos níveis
def classificar_heroi(nome, xp):
    if xp < 1000:
        nivel = "Ferro"
    elif xp <= 2000:
        nivel = "Bronze"
    elif xp <= 5000:
        nivel = "Prata"
    elif xp <= 7000:
        nivel = "Ouro"
    elif xp <= 8000:
        nivel = "Platina"
    elif xp <= 9000:
        nivel = "Ascendente"
    elif xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    
    print(f"O Herói de nome {nome} está no nível de {nivel}")

# Lista de heróis e seus XP
herois = [
    ("Goku", 500),
    ("Chapolin", 1500),
    ("Hulk", 3000),
    ("Batman", 6000),
    ("Superman", 7500),
    ("Pegasus", 8500),
    ("Andromeda", 9500),
    ("Fenix", 11000)
]

# Exibir opções de heróis
print("Escolha um herói:")
for i, (nome, _) in enumerate(herois, 1):
    print(f"{i}. {nome}")

# Solicitar escolha do usuário
escolha = int(input("Digite o número do herói escolhido: ")) - 1

# Validar escolha e classificar
if 0 <= escolha < len(herois):
    nome_heroi, xp_heroi = herois[escolha]
    classificar_heroi(nome_heroi, xp_heroi)
else:
    print("Escolha inválida!")

------------------------------------------------------------------------------------------------
# Desafio 2
# Calculadora de Partidas Rankeadas

#Função vitoria - derrota
def calcular_saldo(vitorias, derrotas):
    return vitorias - derrotas

#Classificação de vitorias
def classificar_jogador(vitorias):
    if vitorias < 10:
        return "Ferro"
    elif vitorias <= 20:
        return "Bronze"
    elif vitorias <= 50:
        return "Prata"
    elif vitorias <= 80:
        return "Ouro"
    elif vitorias <= 90:
        return "Diamante"
    elif vitorias <= 100:
        return "Lendário"
    else:
        return "Imortal"

# Entrada do usuário
vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

# Cálculo do saldo de vitórias
saldo_vitorias = calcular_saldo(vitorias, derrotas)
nivel = classificar_jogador(vitorias)

# Exibir resultado
print(f"O Herói tem um saldo de {saldo_vitorias} e está no nível de {nivel}")

------------------------------------------------------------------------------------------------
# Desafio 3
# Escrevendo as classes de um jogo

# Metodo construtor
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
