import pygame
from systems import GameVars

class HealthBar():
    def __init__(self, max_health):
        self.max_length = 750
        self.max_health = max_health
        self.current_health = self.max_health

    def set_current_health(self, current_health):
        self.current_health = current_health

    def draw(self):
        if (self.current_health == 0):
            length = 0
        else:
            length = (self.current_health / self.max_health) * self.max_length
        pygame.draw.rect(GameVars.SCREEN,
                         (255, 0, 0),
                         ((GameVars.SCREEN_WIDTH // 2) - (self.max_length // 2), GameVars.SCREEN_HEIGHT // 2.8, self.max_length, 50))
        pygame.draw.rect(GameVars.SCREEN,
                         (0, 255, 0),
                         ((GameVars.SCREEN_WIDTH // 2) - (self.max_length // 2), GameVars.SCREEN_HEIGHT // 2.8, length, 50))
