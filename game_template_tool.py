import tkinter as tk
from tkinter import messagebox 


#Blueprint Para o Jogo Da Cobrinha
def criar_snake():
    codigo_snake = '''
import pygame
import random


pygame.init()
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jogo da Cobrinha")

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
    for parte in cobrinha:
        pygame.draw.rect(tela, VERDE, (*parte, 10, 10))

    pygame.draw.rect(tela, VERMELHO, (*comida, 10, 10))
    pygame.display.update()


def mostrar_menu(pontos):
    fonte = pygame.font.SysFont(None, 28)
    texto = fonte.render(f'Pontuação: {pontos}', True, VERDE)
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
    global cobrinha, direcao, comida
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
        else:
            cobrinha.pop()

        if nova_cabeca in cobrinha[1:]:
            rodando = False

        if (nova_cabeca[0] < 0 or nova_cabeca[0] >= 500 or
            nova_cabeca[1] < 0 or nova_cabeca[1] >= 500):
            rodando = False

        desenhar()
        relogio.tick(15)

while True:
    jogo()
    pontos = len(cobrinha) - 1
    if not mostrar_menu(pontos):
        break
pygame.quit()
'''
    with open("snake_template.py", "w", encoding="utf-8") as f:
        f.write(codigo_snake)
    messagebox.showinfo("Blueprint", "Jogo Snake Sendo Gerado...")


#Blueprint Para o Campo Minado
def criar_campo_minado():
    messagebox.showinfo("Blueprint", "Jogo Campo Minado Sendo Gerado...")

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
