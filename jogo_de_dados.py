"""
Jogo de dados(21)

Este jogo tem como intuito um jogo entre 2 ou mais jogadores,
no qual, os jogadores que retirarem a quantia de 21 primeiro,
este será o vencedor.
"""

from random import randint

qtd_jogadores = 2

jogadores = ["jogador " + str(i) for i in range(1, qtd_jogadores+1)]

vencedor = 0
contador = 1
jogadas = [[] for x in range(qtd_jogadores)]
dado_1, dado_2 = 0, 0


while(vencedor == 0):
    if len(jogadores) == 2:
        # Se a jogada for ímpar, será o jogador 1, se não será o jogador 2
        if contador%2 != 0:
            print("\033[31mVez do Jogador 1\033[0;0m")
            jogar = input("Clique em qualque tecla pra começar: ")
            if jogar != None:
                dado_1 =  randint(1, 6)
                dado_2 =  randint(1, 6)
                total_1 = 0

                jogadas[0].append((dado_1, dado_2))
                print("Jogadas: ", jogadas[0], "\033[0;0m")
                for valor in jogadas[0]:
                    total_1 += sum(valor)
                
                print("\033[31mtotal: ", total_1, "\033[0;0m")
                if total_1 >= 21:
                    vencedor = 1


        else:
            print("\033[34mVez do Jogador 2\033[0;0m")
            jogar = input("Clique em qualque tecla pra começar: ")
            if jogar != None:
                dado_1 =  randint(1, 6)
                dado_2 =  randint(1, 6)
                total_2 = 0

                jogadas[1].append((dado_1, dado_2))
                print("Jogadas: ", jogadas[1])
                for valor in jogadas[1]:
                    total_2 += sum(valor)
                
                print("\033[34mtotal: ", total_2, "\033[0;0m")
                
                if total_2 >= 21:
                    vencedor = 2

    contador += 1

if vencedor == 1:
    print(f"\033[31m\nVencedor foi o Jogador {vencedor}\033[0;0m")
else:
    print(f"\033[34m\nVencedor foi o Jogador {vencedor}\033[0;0m")