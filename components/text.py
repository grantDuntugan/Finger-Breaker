import pygame
import time
from systems import GameVars

class Text():
    def __init__(self, surface, text, size, color, x, y):
        font_name = pygame.font.match_font('leelawadee')
        self.surface = surface
        self.text = text
        self.size = size
        self.font = pygame.font.Font(font_name, self.size)
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surface.blit(text_surface, text_rect)

def drawText(surface, text, color, rect, size, aa=False, bkg=None):
    font_name = pygame.font.match_font('leelawadee')
    font = pygame.font.Font(font_name, size)
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

def create_title_text():
    return Text(GameVars.SCREEN,
                "Finger Breaker",
                100,
                (255, 255, 255),
                GameVars.SCREEN_WIDTH / 2,
                GameVars.SCREEN_HEIGHT / 3)

def create_time_text(start_time):
    return Text(GameVars.SCREEN,
                str(int(time.time() - start_time - GameVars.time_out) * -1),
                100,
                (255, 0, 0),
                GameVars.SCREEN_WIDTH //2 ,
                GameVars.SCREEN_HEIGHT // 8)

def create_word_to_type_text():
    return Text(GameVars.SCREEN,
                "".join(GameVars.stack),
                100,
                (255, 255, 255),
                GameVars.SCREEN_WIDTH // 2,
                GameVars.SCREEN_HEIGHT // 4)

def create_letters_typed_text():
    return Text(GameVars.SCREEN,
                "".join(GameVars.user_stack),
                100,
                (255, 0, 255),
                GameVars.SCREEN_WIDTH // 2,
                (GameVars.SCREEN_HEIGHT // 2) * 1.5)

def create_player_money_text():
    return Text(GameVars.SCREEN,
                "Money: $" + str(GameVars.player_money),
                80,
                (0, 250, 0),
                GameVars.SCREEN_WIDTH // 8,
                GameVars.SCREEN_HEIGHT // 8)

def create_dpw_text():
    return Text(GameVars.SCREEN,
                "Damage: " + str(GameVars.player_damage) + "dpw",
                80,
                (0, 250, 0),
                GameVars.SCREEN_WIDTH // 7,
                (GameVars.SCREEN_HEIGHT // 8) * 2)


def create_TT_letters_typed_text():
    return Text(GameVars.SCREEN,
                "".join(GameVars.user_stack),
                100,
                (255, 0, 255),
                GameVars.SCREEN_WIDTH // 2,
                (GameVars.SCREEN_HEIGHT // 3) * 2)

def create_TT_word_to_type_text():
    return Text(GameVars.SCREEN,
                "".join(GameVars.stack),
                100,
                (255, 255, 255),
                GameVars.SCREEN_WIDTH // 2,
                GameVars.SCREEN_HEIGHT // 2)

def create_score_text():
    return Text(GameVars.SCREEN,
                "Score: " + str(GameVars.score),
                100, (0, 250, 0),
                GameVars.SCREEN_WIDTH//8,
                GameVars.SCREEN_HEIGHT // 8)

def create_lives_text():
    return Text(GameVars.SCREEN,
                "Lives: " + str(GameVars.lives),
                100,
                (0, 250, 0),
                GameVars.SCREEN_WIDTH//8,
                (GameVars.SCREEN_HEIGHT//8) * 2)

def draw_wrapped_congrats_text():
    drawText(GameVars.SCREEN,
             "Congrats! Your score was " + str(GameVars.score) + ".",
             (0, 250, 0),
             (0, GameVars.SCREEN_HEIGHT // 3, GameVars.SCREEN_WIDTH, (GameVars.SCREEN_HEIGHT//3) * 2),
             150)