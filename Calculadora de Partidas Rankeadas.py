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
