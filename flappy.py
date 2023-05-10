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

<<<<<<< HEAD

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
