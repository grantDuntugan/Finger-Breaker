import pygame
import random
from systems import GameVars

skeleton_img = pygame.image.load("images/skeleton.png")
bat_img = pygame.image.load("images/bat.png")
spider_img = pygame.image.load("images/spider.png")
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
    skeleton = Enemy(skeleton_img,
              2.5,
              GameVars.SCREEN_WIDTH // 2,
              GameVars.SCREEN_HEIGHT // 2,
              50)
    skeleton.image.set_colorkey((255,255,255))
    return skeleton

def get_bat_enemy():
    bat = Enemy(bat_img,
    1.5,
    GameVars.SCREEN_WIDTH // 2,
    GameVars.SCREEN_HEIGHT // 1.7,
    90)
    bat.image.set_colorkey((255,255,255))
    return bat

def get_spider_enemy():
    spider = Enemy(spider_img,
                   6,
                   GameVars.SCREEN_WIDTH // 2,
                   GameVars.SCREEN_HEIGHT // 1.7,
                   90)
    return spider

def get_random_enemy(selector = None):
    rng = random.randint(1, 3)
    if (selector == "skeleton" or rng == 1):
        return get_skeleton_enemy()
    elif (selector == "bat" or rng == 2):
        return get_bat_enemy()
    elif (selector == "spider" or rng == 3):
        return get_spider_enemy()