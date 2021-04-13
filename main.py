import pygame
import random

# Iniciando pygame
pygame.init()

# Definindo cores (RGB)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
laranja = (255, 165, 0)
verde = (0, 255, 0)

# Definindo tamanho da tela do jogo (em pixels)
largura, altura = 600, 400
game_display = pygame.display.set_mode((largura, altura))

# Definindo nome do jogo
pygame.display.set_caption('Snake Game')

# Definindo um relógio que mantém o tempo, o tamanho da cobra e a velocidade (em pixels)
relogio = pygame.time.Clock()
snake_tamanho = 10
snake_velocidade = 15

# Definindo a fonte ('nome da fonte', tamanho): escolha uma fonte da sua preferência
fonte_mensagem = pygame.font.SysFont('roboto', 30)
fonte_score = pygame.font.SysFont('roboto', 25)


# Função para atualizar o score
def mostra_score(score):
    text = fonte_score.render('Score: ' + str(score), True, verde)
    game_display.blit(text, [0, 0])


# Função para definir a cobra (tamanho, movimento)
def desenha_snake(snake_tamanho, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, branco, [pixel[0], pixel[1], snake_tamanho, snake_tamanho])


# Função do funcionamento do jogo
def run_game():
    game_over = False
    game_close = False

    # Posição inicial
    x = largura / 2
    y = altura / 2

    # Velocidade inicial
    x_velocidade = 0
    y_velocidade = 0

    # Tamanho da cobra. A lista vazia serve pra definir o crescimento da cobra ao longo do jogo
    snake_pixels = []
    snake_comprimento = 1

    # Definindo a posição da comida
    comida_x = round(random.randrange(0, largura - snake_tamanho) / 10.0) * 10
    comida_y = round(random.randrange(0, altura - snake_tamanho) / 10.0) * 10

    # Loop do jogo
    while not game_over:

        while game_close:
            game_display.fill(preto)
            game_over_mensagem = fonte_mensagem.render('Game Over!', True, vermelho)
            quit_mensagem = fonte_mensagem.render('Press Q to quit', True, vermelho)
            restart_mensagem = fonte_mensagem.render('Press R to restart', True, vermelho)
            game_display.blit(game_over_mensagem, [largura / 3, altura / 3])
            game_display.blit(quit_mensagem, [largura / 3, (altura / 3) + 30])
            game_display.blit(restart_mensagem, [largura / 3, (altura / 3) + 60])
            mostra_score(snake_comprimento - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        # Estabelece as setas do teclado para movimentar a cobra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_velocidade = -snake_tamanho
                    y_velocidade = 0
                if event.key == pygame.K_RIGHT:
                    x_velocidade = snake_tamanho
                    y_velocidade = 0
                if event.key == pygame.K_UP:
                    x_velocidade = 0
                    y_velocidade = -snake_tamanho
                if event.key == pygame.K_DOWN:
                    x_velocidade = 0
                    y_velocidade = snake_tamanho

        # Condição para fim de jogo caso a cobra bata na parede
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_close = True

        # Faz a cobra se movimentar baseado na velocidade
        x += x_velocidade
        y += y_velocidade

        # Colocando a cor de fundo e posisionando os elementos na tela
        game_display.fill(preto)
        pygame.draw.rect(game_display, laranja, [comida_x, comida_y, snake_tamanho, snake_tamanho])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_comprimento:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        desenha_snake(snake_tamanho, snake_pixels)
        mostra_score(snake_comprimento - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - snake_tamanho) / 10.0) * 10
            comida_y = round(random.randrange(0, altura - snake_tamanho) / 10.0) * 10
            snake_comprimento += 1

        relogio.tick(snake_velocidade)

    pygame.quit()
    quit()


run_game()
