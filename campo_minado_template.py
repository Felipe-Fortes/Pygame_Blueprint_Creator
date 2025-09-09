
import pygame
import random

# Configurações
LARGURA, ALTURA = 400, 400
LINHAS, COLUNAS = 10, 10
MINAS = 10
TAMANHO_CELULA = LARGURA // COLUNAS

# Cores
CINZA = (200, 200, 200)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Campo Minado")

# Função para criar o tabuleiro
def criar_tabuleiro():
    tabuleiro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
    minas = set()
    while len(minas) < MINAS:
        x = random.randint(0, LINHAS - 1)
        y = random.randint(0, COLUNAS - 1)
        minas.add((x, y))
    for (mx, my) in minas:
        tabuleiro[mx][my] = -1
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = mx + i, my + j
                if 0 <= nx < LINHAS and 0 <= ny < COLUNAS and tabuleiro[nx][ny] != -1:
                    tabuleiro[nx][ny] += 1
    return tabuleiro, minas

tabuleiro, minas = criar_tabuleiro()
reveladas = [[False for _ in range(COLUNAS)] for _ in range(LINHAS)]

def desenhar():
    tela.fill(BRANCO)
    fonte = pygame.font.SysFont(None, 24)
    for x in range(LINHAS):
        for y in range(COLUNAS):
            rect = pygame.Rect(y * TAMANHO_CELULA, x * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
            pygame.draw.rect(tela, CINZA, rect, 0 if reveladas[x][y] else 1)
            if reveladas[x][y]:
                if tabuleiro[x][y] == -1:
                    pygame.draw.circle(tela, VERMELHO, rect.center, TAMANHO_CELULA // 4)
                elif tabuleiro[x][y] > 0:
                    texto = fonte.render(str(tabuleiro[x][y]), True, PRETO)
                    tela.blit(texto, (rect.x + TAMANHO_CELULA // 3, rect.y + TAMANHO_CELULA // 4))
    pygame.display.update()

def revelar(x, y):
    if reveladas[x][y]:
        return
    reveladas[x][y] = True
    if tabuleiro[x][y] == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if 0 <= nx < LINHAS and 0 <= ny < COLUNAS:
                    if not reveladas[nx][ny]:
                        revelar(nx, ny)

def perdeu():
    for (mx, my) in minas:
        reveladas[mx][my] = True

rodando = True
while rodando:
    desenhar()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mx, my = pygame.mouse.get_pos()
            x, y = my // TAMANHO_CELULA, mx // TAMANHO_CELULA
            if tabuleiro[x][y] == -1:
                perdeu()
            else:
                revelar(x, y)
pygame.quit()
