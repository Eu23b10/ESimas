import pygame, random
# Carregando as imagens.
imagemNave = pygame.image.load('nave.png')
imagemAsteroide = pygame.image.load('asteroide.png')
imagemRaio = pygame.image.load('raio.png')
imagemFundo = pygame.image.load('magellanic-clouds.png')
LARGURAJANELA = 600  # largura da janela
ALTURAJANELA = 600  # altura da janela
CORTEXTO = (255, 255, 255)     # cor do texto (branca)
QPS = 40      # quadros por segundo
TAMMINIMO = 10  # tamanho mínimo do asteroide
TAMMAXIMO = 40  # tamanho máximo do asteroide
VELMINIMA = 1   # velocidade mínima do asteroide
VELMAXIMA = 8   # velocidade máxima do asteroide
ITERACOES = 6   # número de iterações antes de criar um novo asteroide
VELJOGADOR = 5  # velocidade da nave
VELRAIO = (0,-15)                # velocidade do raio
LARGURANAVE = imagemNave.get_width()
ALTURANAVE = imagemNave.get_height()
LARGURARAIO = imagemRaio.get_width()
ALTURARAIO = imagemRaio.get_height()
def moverJogador(jogador, teclas, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['objRect'].right < borda_direita:
        jogador['objRect'].x += jogador['vel']
    if teclas['cima'] and jogador['objRect'].top > borda_superior:
        jogador['objRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador['objRect'].bottom < borda_inferior:
        jogador['objRect'].y += jogador['vel']
