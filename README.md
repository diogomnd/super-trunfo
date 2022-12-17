# Super Trunfo
Objetivo do Projeto: Consolidar a prática e experiência na implementação de software utilizando a
linguagem de programação Python, fazendo uso dos conhecimentos adquiridos na disciplina.

- O jogo consiste em um baralho de 20 cartas. Cada carta irá conter um personagem e três
características dele com valores numéricos diferentes de zero. Alguns exemplos:
o Baralho de Países: população, área e PIB
o Baralho de Animais: altura, peso e velocidade
o Baralho de Carros: velocidade, motor e preço
- O jogo terá dois participantes. Inicialmente, cada um começa com 1000 pontos, e 4 cartas sorteadas
aleatoriamente do baralho, que ficarão empilhadas (numa determinada sequência) e ocultas (conteúdo
não revelado). As demais cartas ficam ocultas em uma pilha central.
- A cada rodada, os participantes se alternam escolhendo uma das características para desafiar seu
oponente. As cartas de cima da pilha de cada um terão os valores dessa característica comparados, e
aquele que tiver maior valor ganha a rodada.
- O jogador vencedor terá sua pontuação aumentada do valor da característica vencedora. Já o jogador
perdedor da rodada terá sua pontuação diminuída pela diferença entre os valores comparados nas
cartas. (Ex: considerando a característica velocidade, caso a carta do Jogador 1 tenha valor 100 e a do
Jogador 2 tenha valor 20, o Jogador 1 ganhará 100 pontos e o Jogador 2 perderá 80 pontos)
- Além disso, as duas cartas que disputaram a rodada vão para baixo da pilha do jogador vencedor.
- Em caso de empate nos valores, a rodada é anulada e as cartas são descartadas. Então, cada jogador
recebe uma nova carta dentre as que ficaram na pilha central, iniciando a rodada novamente com a
escolha da característica a ser comparada (pode ser a mesma ou outra). É importante enfatizar que as
novas cartas recebidas ficam em cima das respectivas pilhas.
- Após 4 rodadas, vencerá o jogador que tiver o maior saldo de pontos. Caso ambos tenham o mesmo
saldo, será decretado um empate.
