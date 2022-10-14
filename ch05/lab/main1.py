import pygame
pygame.init()
display = pygame.display.set_mode()
display.fill("blue")
pygame.draw.lines(display,"black",False,[(150,300),(250,300)],1)
pygame.display.flip()
