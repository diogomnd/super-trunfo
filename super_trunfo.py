import art
import random
import os
from colorama import Fore, init
from time import sleep


def remover_cartas(pilha_central, deck_jogador):
    for carta in deck_jogador:
        if carta in pilha_central:
            pilha_central.remove(carta)


def modo_de_disputa(deck_jogador, pick_jogador):
    if pick_jogador in deck_jogador:
        deck_jogador.remove(pick_jogador)


def descartar_cartas(pick_jogador, pilha_de_descarte):
    pilha_de_descarte.append(pick_jogador)


init(autoreset=True)

print(Fore.RED + "⎯⎯" * 86)
art.tprint("Copa do Mundo FIFA Catar 2022")
print(Fore.RED + "⎯⎯" * 86)

sleep(5)
os.system('cls')
sleep(1)

print(Fore.BLUE + "No super trunfo cada jogador começa com 1000 pontos e "
      "pegará 4 cartas aleatórias da pilha central, e então escolherá entre os"
      " atributos: Ataque, Meio-Campo e Defesa, e en-\ntão a partida começará."
      " Quem tiver o melhor atributo ao fim da rodada, ganha a quantidade de"
      " pontos do atributo e seu adversário perderá a quantidade de pontos "
      "equivalente\nà diferença dos atributos escolhidos por cada jogador. Se "
      "houver empate, a rodada será anulada e as cartas escolhidas descartadas"
      ". Ao fim de 4 rodadas, o jogador que tiver\na maior quantidade de "
      "pontos vencerá o jogo. \n")

sleep(10)

continuar = input(Fore.RESET + "Aperte enter para continuar: \n")
os.system('cls')

sleep(0.5)
nome1 = input("Qual o nome do 1º jogador? ").strip().title()
sleep(0.5)
nome2 = input("Qual o nome do 2º jogador? ").strip().title()

os.system('cls')

# Pilha central
pilha_central = [
    ["Alemanha", 86, 84, 85], ["Argentina", 87, 88, 80],
    ["Bélgica", 84, 85, 86], ["Brasil", 91, 85, 79],
    ["Croácia", 81, 82, 92], ["Dinamarca", 80, 82, 93],
    ["EUA", 83, 79, 93], ["Espanha", 82, 87, 86],
    ["França", 88, 84, 83], ["Holanda", 84, 83, 88],
    ["Inglaterra", 85, 85, 85], ["Marrocos", 79, 82, 95],
    ["México", 79, 83, 93], ["Gales", 84, 82, 89],
    ["Polônia", 81, 79, 95], ["Portugal", 87, 84, 84],
    ["Senegal", 80, 81, 94], ["Sérvia", 80, 83, 92],
    ["Suíça", 80, 82, 93], ["Uruguai", 84, 84, 87]]

# Embaralhar
random.shuffle(pilha_central)

# Sorteio da mão do 1º jogador
deck_jogador1 = random.sample(pilha_central, 4)

# Remove as cartas sorteadas para o 1º jogador da pilha central
remover_cartas(pilha_central, deck_jogador1)

# Sorteio da mão do 2º jogador
deck_jogador2 = random.sample(pilha_central, 4)

# Remove as cartas sorteadas para o 2º jogador da pilha central
remover_cartas(pilha_central, deck_jogador2)

# Início da rodada
pontos_jogador1 = pontos_jogador2 = 1000
numero_rodadas = 1
pilha_de_descarte = []

while numero_rodadas <= 4:
    sleep(3)
    print(Fore.YELLOW + "⎯" * 30 + f"{numero_rodadas}ª rodada" + "⎯" * 30)

    if numero_rodadas % 2 != 0:
        print(f"Vez do(a) jogador(a): {nome1}")
        print(f"\n{nome1}, escolha uma característica:\n")

    else:
        print(f"Vez do(a) jogador(a): {nome2}")
        print(f"\n{nome2}, escolha uma característica:\n")

    # Definindo as escolhas dos jogadores (cartas do início da pilha)
    pick_jogador1 = deck_jogador1[0]
    pick_jogador2 = deck_jogador2[0]

    # As cartas que serão disputadas saem das mãos de cada jogador e
    # ficarão em modo de disputa
    modo_de_disputa(deck_jogador1, pick_jogador1)
    modo_de_disputa(deck_jogador2, pick_jogador2)

    caracteristica = int(input(Fore.RED + "[1] para Ataque\n"
                               + Fore.GREEN + "[2] para Meio-campo\n"
                               + Fore.BLUE + "[3] para Defesa\n"
                               + Fore.RESET + "\nDigite aqui: "))

    sleep(3)

    if caracteristica not in [1, 2, 3]:
        print("\nDigite um numero válido!")

    else:
        # Resumo da rodada
        print(Fore.YELLOW + "⎯" * 24 + f"Resumo da {numero_rodadas}ª rodada"
              + "⎯" * 26)

        # Exibe as cartas escolhidas pelos jogadores em questão
        print(f"\nCarta de {nome1}:", end=" ")
        print(Fore.CYAN + f"{pick_jogador1[0]}" + Fore.RESET +
              f" Ataque: {pick_jogador1[1]}; Meio: {pick_jogador1[2]};"
              f" Defesa: {pick_jogador1[3]}")

        print(f"Carta de {nome2}:", end=" ")
        print(Fore.CYAN + f"{pick_jogador2[0]}" + Fore.RESET +
              f" Ataque: {pick_jogador2[1]}; Meio: {pick_jogador2[2]};"
              f" Defesa: {pick_jogador2[3]}")

        if pick_jogador1[caracteristica] == pick_jogador2[caracteristica]:
            # Insere as cartas disputadas na pilha de descarte
            descartar_cartas(pick_jogador1, pilha_de_descarte)
            descartar_cartas(pick_jogador2, pilha_de_descarte)

            # Insere em cima da pilha do 1º jogador uma carta vinda da pilha
            # central
            deck_jogador1.insert(0, pilha_central[0])

            # Em seguida remove-a da pilha central pra evitar duplicatas
            remover_cartas(pilha_central, deck_jogador1)

            # Insere em cima da pilha do 2º jogador uma carta vinda da pilha
            # central
            deck_jogador2.insert(0, pilha_central[0])

            # Em seguida remove-a da pilha central pra evitar duplicatas
            remover_cartas(pilha_central, deck_jogador2)

            print(Fore.YELLOW + "\nHouve um empate. Rodada anulada.")

            numero_rodadas -= 1        # Anula a rodada

        elif pick_jogador1[caracteristica] > pick_jogador2[caracteristica]:
            # As cartas que disputaram rodada vão para baixo da pilha do
            # vencedor
            deck_jogador1.append(pick_jogador1)
            deck_jogador1.append(pick_jogador2)

            pontos_jogador1 += pick_jogador1[caracteristica]  # Adiciona os pts
            pontos_jogador2 -= pick_jogador1[caracteristica] - \
                pick_jogador2[caracteristica]                 # Debita os pts

            pontos_ganhos = pick_jogador1[caracteristica]

            pontos_perdidos = pick_jogador1[caracteristica] - \
                pick_jogador2[caracteristica]

            print(Fore.YELLOW + f"\n{nome1} venceu a rodada!")
            print(Fore.GREEN + f"{nome1} ganhou {pontos_ganhos} pontos!", "🤑")
            print(Fore.RED + f"{nome2} perdeu {pontos_perdidos} pontos!", "💀")

        else:
            # As cartas que disputaram rodada vão para baixo da pilha do
            # vencedor
            deck_jogador2.append(pick_jogador1)
            deck_jogador2.append(pick_jogador2)

            pontos_jogador2 += pick_jogador2[caracteristica]  # Adiciona os pts
            pontos_jogador1 -= pick_jogador2[caracteristica] - \
                pick_jogador1[caracteristica]                 # Debita os pts

            pontos_ganhos = pick_jogador2[caracteristica]

            pontos_perdidos = pick_jogador2[caracteristica] - \
                pick_jogador1[caracteristica]

            print(Fore.YELLOW + f"\n{nome2} venceu a rodada!")
            print(Fore.GREEN + f"{nome2} ganhou {pontos_ganhos} pontos!", "🤑")
            print(Fore.RED + f"{nome1} perdeu {pontos_perdidos} pontos!", "💀")

        # Final da rodada
        print(f"\nPontos de {nome1}: " + Fore.GREEN + f"{pontos_jogador1}")
        print(f"Pontos de {nome2}: " + Fore.GREEN + f"{pontos_jogador2}")

        numero_rodadas += 1        # Incrementa as rodadas

        # Em caso de sucessivos empates, e a pilha central ficar vazia, então
        # a pilha central receberá a pilha de descarte com todos os descartes
        # anteriores das rodadas em que houve empate
        if pilha_central == []:
            random.shuffle(pilha_de_descarte)
            pilha_central = pilha_de_descarte.copy()
            pilha_de_descarte.clear()

sleep(3)

print(Fore.YELLOW + "⎯" * 29 + "FIM DE JOGO" + "⎯" * 29)

if pontos_jogador1 > pontos_jogador2:
    print(Fore.MAGENTA +
          f"\n{nome1} venceu o jogo com {pontos_jogador1} pontos!", "👏")

elif pontos_jogador2 > pontos_jogador1:
    print(Fore.MAGENTA +
          f"\n{nome2} venceu o jogo com {pontos_jogador2} pontos!", "👏")

else:
    pontos_jogadores = pontos_jogador1 = pontos_jogador2
    print(Fore.MAGENTA +
          f"\nHouve um empate! Ambos terminaram com"
          f"{pontos_jogadores} pontos.", "😵")
