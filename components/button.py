import pygame
from systems import GameVars

class Button(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, width, height, text = ""):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.center = ((x, y))
        self.image.fill((255,255,255))

    def draw(self):
        self.surface.blit(self.image, (self.rect.center))
        if self.text != '':
            font_name = pygame.font.match_font('leelawadee')
            font = pygame.font.Font(font_name, 18)
            text_surface = font.render(self.text, True, (0,0,0))
            width = self.image.get_width()
            height = self.image.get_height()
            self.surface.blit(text_surface, (self.x + (width/2 - text_surface.get_width()/2), self.y + (height/2 - text_surface.get_height()/2)))

    def in_bounds(self, pos):
        if pos[0] >= self.x and pos[0] <= self.x + self.width:
            if pos[1] >= self.y and pos[1] <= self.y + self.height:
                return True

        return False

def create_start_button():
    return Button(GameVars.SCREEN,
                  GameVars.SCREEN_WIDTH // 2 - GameVars.SCREEN_WIDTH // 10,
                  (GameVars.SCREEN_HEIGHT // 3) * 2,
                  GameVars.SCREEN_WIDTH //5,
                  GameVars.SCREEN_HEIGHT //10,
                  "Start")