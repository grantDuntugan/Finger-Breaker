import pygame
import os
import time
from components import text, button
from systems import GameVars, GameFunctions, keyhandle
os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pygame.init()

GameVars.SCREEN_INFO = pygame.display.Info() # You have to call this before pygame.display.set_mode()
GameVars.SCREEN_WIDTH = GameVars.SCREEN_INFO.current_w
GameVars.SCREEN_HEIGHT = GameVars.SCREEN_INFO.current_h
GameVars.SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

start_button = button.create_start_button()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if GameVars.state_start:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if start_button.in_bounds(pos):
                    GameVars.state_start = False
                    GameVars.state_game = True

        elif GameVars.state_game:
            keyhandle.handle_keys(event)

    if GameVars.state_start:
        title_text = text.create_title_text()
        title_text.draw()
        start_button.draw()

    elif GameVars.state_game:
        GameVars.SCREEN.fill((0,0,0))

        if (GameVars.timer_running == False):
            GameFunctions.get_word_from_lib()
            GameVars.start_time = time.time()
            GameVars.timer_running = True
            GameVars.word_to_type_text = text.create_word_to_type_text()

        if time.time() - GameVars.start_time >= GameVars.time_out:
            GameFunctions.subtract_life()
            if GameVars.lives == 0:
                GameFunctions.end_game()

        if GameVars.user_stack == GameVars.stack:
            GameFunctions.add_point_and_get_next_word()

        GameFunctions.set_and_draw_text()

    elif GameVars.state_pause:
        pass

    elif GameVars.state_end:
        GameVars.SCREEN.fill((0,0,0))
        text.draw_wrapped_congrats_text()
    pygame.display.update()