import pygame
from systems import GameVars

skeleton_img = pygame.image.load("images/skeleton.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

def get_skeleton_enemy():
    s = Enemy(skeleton_img,
              1,
              GameVars.SCREEN_WIDTH // 2,
              GameVars.SCREEN_HEIGHT // 2,
              200)
    s.image.set_colorkey((255,255,255))
    return s