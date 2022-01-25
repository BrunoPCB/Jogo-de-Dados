"""
Jogo de dados(21)

Este jogo tem como intuito um jogo entre 2 ou mais jogadores,
no qual, os jogadores que retirarem a quantia de 21 primeiro,
este será o vencedor.
"""

from random import randint

qtd_jogadores = input("Informe a quantidade de jogadores: ")


# Tratando possibilidade de erros do usuário(Ex: Informar valor alfa numérico).
while(isinstance(qtd_jogadores, str)):
    
    try:
        qtd_jogadores = int(qtd_jogadores)

        # Erro caso o valor seja menor que 2, pois só pode jogar 2 ou mais jogadores.
        if qtd_jogadores < 2:
            raise ValueError("O valor informado deve ser maior ou igual a 2.")
        else:
            break

    except Exception as e:
        print("Erro: ", e)
        qtd_jogadores = input("Informe a quantidade de jogadores: ")


jogadores = ["jogador " + str(i) for i in range(1, qtd_jogadores+1)]

vencedor = 0
contador = 1
jogadas = [[] for x in range(qtd_jogadores)]
dado_1, dado_2 = 0, 0


while(vencedor == 0):
    if len(jogadores) == 2:
        # Se a jogada for ímpar, será o jogador 1, se não será o jogador 2
        if contador%2 != 0:
            print("Vez do Jogador 1")
            dado_1 =  randint(1, 6)
            dado_2 =  randint(1, 6)
            total_1 = 0

            jogadas[0].append((dado_1, dado_2))
            print("Jogadas: ", jogadas[0])
            for valor in jogadas[0]:
                total_1 += sum(valor)
                print("total_1: ", total_1)
            if total_1 >= 21:
                vencedor = 1


        else:
            print("Vez do Jogador 2")
            dado_1 =  randint(1, 6)
            dado_2 =  randint(1, 6)
            total_2 = 0

            jogadas[1].append((dado_1, dado_2))
            print("Jogadas: ", jogadas[1])
            for valor in jogadas[1]:
                total_2 += sum(valor)
                print("total_2: ", total_2)
            if total_2 >= 21:
                vencedor = 2

    contador += 1

print(f"Vencedor foi o Jogador {vencedor}")