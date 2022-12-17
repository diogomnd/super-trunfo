def remover_cartas(pilha_central, deck_jogador):
    for carta in deck_jogador:
        if carta in pilha_central:
            pilha_central.remove(carta)


def modo_de_disputa(deck_jogador, pick_jogador):
    if pick_jogador in deck_jogador:
        deck_jogador.remove(pick_jogador)


def descartar_cartas(pick_jogador, pilha_de_descarte):
    pilha_de_descarte.append(pick_jogador)
