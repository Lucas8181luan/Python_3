# APRENDA A TOCAR UM MP3

# 1° PASSO, IMPORTE UM AUDIO PARA A MESMA PASTA

# 2° PASSO, INSTALE A BIBLIOTECA PYGAME

# Importe pygame
import pygame

# Para iniciar a biblioteca pygame
pygame.init()

# Importando o audio
pygame.mixer.music.load( nome do arquivo do audio usando aspas )

# tocar a musica
pygame.mixer.music.play()
pygame.event.wait()

# AGORA E SÓ OUVIR
