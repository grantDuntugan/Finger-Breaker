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
GameVars.start_button = button.create_start_button()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if GameVars.state_start:
            GameFunctions.listen_for_start()

        elif GameVars.state_game:
            keyhandle.handle_game_keys(event)

    if GameVars.state_start:
        GameFunctions.run_start_state()

    elif GameVars.state_game:
        GameFunctions.run_game_state()

    elif GameVars.state_pause:
        pass

    elif GameVars.state_end:
        GameFunctions.run_end_state()

    pygame.display.update()