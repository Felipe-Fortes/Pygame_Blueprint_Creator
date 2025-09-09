import os
import tkinter as tk
from tkinter import messagebox 


# Blueprint Para o Jogo Da Cobrinha

def criar_snake():
    codigo_snake = '''
import pygame
import random


pygame.init()
opacidade = 0
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jogo da Cobrinha")
fundo = pygame.image.load("Bigboss.png").convert_alpha()
fundo.set_alpha(opacidade)

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

cobrinha = [(100,50)]
direcao = (10,0)
comida = (100, 100)

# Define a cor dos elementos
def desenhar():
    tela.fill(PRETO)
    tela.blit(fundo, (0, 0))
    for parte in cobrinha:
        pygame.draw.rect(tela, VERDE, (*parte, 10, 10))

    pygame.draw.rect(tela, VERMELHO, (*comida, 10, 10))
    pygame.display.update()

# Mostra o menu de fim de jogo
def mostrar_menu(pontos):
    fonte = pygame.font.SysFont(None, 28)
    texto = fonte.render(f'Pontos: {pontos}', True, VERDE)
    reiniciar = fonte.render('Pressione R para reiniciar', True, VERMELHO)
    sair = fonte.render('Pressione ESC para sair', True, VERMELHO)
    while True:
        tela.fill(PRETO)
        tela.blit(texto, (160, 180))
        tela.blit(reiniciar, (120, 220))
        tela.blit(sair, (140, 260))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False

def jogo():
    global cobrinha, direcao, comida, opacidade
    cobrinha = [(100,50)]
    direcao = (10,0)
    comida = (100, 100)
    rodando = True
    relogio = pygame.time.Clock()
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                # Impede reversão de direção, Mapeamento de teclas
                if (evento.key == pygame.K_UP or evento.key == pygame.K_w) and direcao != (0, 10):
                    direcao = (0, -10)
                elif (evento.key == pygame.K_DOWN or evento.key == pygame.K_s) and direcao != (0, -10):
                    direcao = (0, 10)
                elif (evento.key == pygame.K_LEFT or evento.key == pygame.K_a) and direcao != (10, 0):
                    direcao = (-10, 0)
                elif (evento.key == pygame.K_RIGHT or evento.key == pygame.K_d) and direcao != (-10, 0):
                    direcao = (10, 0)

        nova_cabeca = (cobrinha[0][0] + direcao[0], cobrinha[0][1] + direcao[1])
        cobrinha.insert(0, nova_cabeca)

        # Verifica se a cobrinha comeu a comida e atualiza a posição da comida
        if nova_cabeca == comida:
            comida = (random.randrange(0, 50) * 10, random.randrange(0, 50) * 10)
            opacidade = min(opacidade + 2.5, 255)
            fundo.set_alpha(opacidade)
        else:
            cobrinha.pop()

        if nova_cabeca in cobrinha[1:]:
            rodando = False

        if (nova_cabeca[0] < 0 or nova_cabeca[0] >= 500 or
            nova_cabeca[1] < 0 or nova_cabeca[1] >= 500):
            rodando = False

        # Velocidade do jogo, quanto maior o valor, mais rapido 
        desenhar()
        relogio.tick(10)

while True:
    jogo()
    pontos = len(cobrinha) - 1
    if not mostrar_menu(pontos):
        break
pygame.quit()
'''
    if os.path.exists("snake_template.py"):
        messagebox.showinfo("AVISO", "Jogo Snake Já Foi Gerado, se quiser gerar novamente, exclua o arquivo existente(snake_template.py).")
    else:
        with open("snake_template.py", "w", encoding="utf-8") as f:
            f.write(codigo_snake)
        messagebox.showinfo("Blueprint", "Jogo Snake Sendo Gerado...")


# Blueprint Para o Campo Minado
def criar_campo_minado():
    codigo_campo_minado = '''
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
'''
    if os.path.exists("campo_minado_template.py"):
            messagebox.showinfo("AVISO", "Jogo Campo Minado Já Foi Gerado, se quiser gerar novamente, exclua o arquivo existente(campo_minado_template.py).")
    else:
        with open("campo_minado_template.py", "w", encoding="utf-8") as f:
            f.write(codigo_campo_minado)
        messagebox.showinfo("Blueprint", "Campo Minado Sendo Gerado...")

def main():
    root = tk.Tk()
    root.title("Ferramenta de Templates")
    root.geometry("400x200")

    label = tk.Label(root, text="Escolha uma blueprint:", font=("Arial", 14))
    label.pack(pady=20)

    btn_snake = tk.Button(root, text="Jogo Da Cobrinha(Snake)", width=25, command=criar_snake)
    btn_snake.pack(pady=10)

    btn_campo_minado = tk.Button(root, text="Campo Minado", width=25, command=criar_campo_minado)
    btn_campo_minado.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
        main()
