import tkinter as tk
from tkinter import messagebox 


#Blueprint Para o Jogo Da Cobrinha
def criar_snake():
    codigo_snake = '''
import pygame
import sys
import random

pygame.init()
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Snake
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_direcao = 'DIREITA'
comida_pos = [random.randrange(1, largura//10)*10, random.randrange(1, altura//10)*10]

def game_over():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direcao != 'BAIXO':
                snake_direcao = 'CIMA'
            elif event.key == pygame.K_DOWN and snake_direcao != 'CIMA':
                snake_direcao = 'BAIXO'
            elif event.key == pygame.K_LEFT and snake_direcao != 'DIREITA':
                snake_direcao = 'ESQUERDA'
            elif event.key == pygame.K_RIGHT and snake_direcao != 'ESQUERDA':
                snake_direcao = 'DIREITA'

    if snake_direcao == 'CIMA':
        nova_cabeca = [snake_pos[0][0], snake_pos[0][1] - 10]
    elif snake_direcao == 'BAIXO':
        nova_cabeca = [snake_pos[0][0], snake_pos[0][1] + 10]
    elif snake_direcao == 'ESQUERDA':
        nova_cabeca = [snake_pos[0][0] - 10, snake_pos[0][1]]
    elif snake_direcao == 'DIREITA':
        nova_cabeca = [snake_pos[0][0] + 10, snake_pos[0][1]]

    snake_pos.insert(0, nova_cabeca)
    if snake_pos[0] == comida_pos:
        comida_pos = [random.randrange(1, largura//10)*10, random.randrange(1, altura//10)*10]
    else:
        snake_pos.pop()

    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= largura or
        snake_pos[0][1] < 0 or snake_pos[0][1] >= altura or
        snake_pos[0] in snake_pos[1:]):
        game_over()

    tela.fill(PRETO)
    for pos in snake_pos:
        pygame.draw.rect(tela, VERDE, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(tela, VERMELHO, pygame.Rect(comida_pos[0], comida_pos[1], 10, 10))
    pygame.display.flip()
    clock.tick(15)
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
