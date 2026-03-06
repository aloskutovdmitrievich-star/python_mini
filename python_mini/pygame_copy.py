import pygame
class newproject():
    pygame.init()
    def __init__(self):
        pass
    def create_window(size, fill=pygame.Color("black"), name_window="pygame window"):
        window = pygame.display.set_mode(size)
        pygame.display.set_caption(name_window)
        window.fill(fill)