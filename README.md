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
