# Começando o projeto
#bibliotecas
import pygame

#variaveis gerais
points = 0

#variaveis passaros
bird_x = 62
bird_y = 200
bird_width = 30
bird_height = 25
bird_y_speed = 0


#variaveis da janela
playing_area_width = 300
playing_area_height = 388

#variaveis do tubo1
pipe_width = 35
pipe_space_height = 100
pipe_space_y = 150
pipe_x = playing_area_width-pipe_width

#variaveis do tubo2
pipe_space_height_2 = 100
pipe_space_y_2 = 150
pipe_x_2 = playing_area_width-pipe_width+200


#funcao desenho
def draw():
    screen.fill((0,0,0))
    #fundo da tela
    screen.draw.filled_rect(
        Rect(
            (0,0),
            (playing_area_width, playing_area_height)
        ),
        color=(72, 61, 139)
=======
#funcao desenho
def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (playing_area_width, playing_area_height)
        ),
        color=(135,206,250)
>>>>>>> aa009f53b348a22d26c20f638b748b84c1c01521
    )
    screen.draw.filled_rect(
        Rect(
            (bird_x, bird_y),
            (bird_width, bird_height)
        ),
        color=(255,255,224)
    )

    #tubo1
    desenhar_tubo(pipe_x,pipe_width,pipe_space_y,pipe_space_height)

    #tubo2
    desenhar_tubo(pipe_x_2,pipe_width,pipe_space_y_2,pipe_space_height_2)

    #pontos na tela
    screen.draw.text(str(points), (15,15))

def on_key_down():
    global bird_y_speed
    if bird_y > 0:
        bird_y_speed -= 165
def update(dt):
    global bird_y
    global bird_y_speed
    global points
    global pipe_x
    global pipe_x_2
    bird_y_speed += 516 * dt
    bird_y += bird_y_speed * dt
    #testa se o tubo1 esta na tela
    if( pipe_x > -35):
        pipe_x -= 60 * dt
    else:
        points += 1
        pipe_x = playing_area_width-pipe_width+54

    #testa se o tubo2 esta na tela
    if( pipe_x_2 > -35):
        pipe_x_2 -= 60 * dt
    else:
        points += 1
        pipe_x_2 = playing_area_width-pipe_width+54

def desenhar_tubo(pipe_x,pipe_width,pipe_space_y,pipe_space_height):
    #tubo1
    screen.draw.filled_rect(
        Rect(
            (pipe_x, 0),
            (pipe_width, pipe_space_y)
    ),
        color=(219,112,147)
    )

#tubo2
    screen.draw.filled_rect(
        Rect(
            (pipe_x, pipe_space_y + pipe_space_height),
            (pipe_width, pipe_space_y)
         ),
        color=(219,112,147)
    )

#config do pygame
WIDTH = playing_area_width
HEIGHT = playing_area_height

