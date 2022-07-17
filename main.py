import pygame
import os
import time
from components import text, button, HealthBar
from systems import GameVars, GameFunctions, keyhandle
from entities import Enemy
os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()
pygame.init()
GameVars.SCREEN_INFO = pygame.display.Info() # You have to call this before pygame.display.set_mode()
GameVars.SCREEN_WIDTH = GameVars.SCREEN_INFO.current_w
GameVars.SCREEN_HEIGHT = GameVars.SCREEN_INFO.current_h
GameVars.SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
GameVars.start_button = button.create_start_button()
GameVars.health_bar = None
GameVars.enemy_group = pygame.sprite.Group()
pygame.mixer.music.load("sounds/typewriter-click (mp3cut.net).mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if GameVars.current_state == GameVars.START_STATE:
            GameFunctions.listen_for_start()
            keyhandle.handle_start_keys(event)

        elif GameVars.current_state == GameVars.GAME_STATE or GameVars.TYPING_TEST_STATE:
            keyhandle.handle_game_keys(event)

    if GameVars.current_state == GameVars.START_STATE:
        GameFunctions.run_start_state()

    elif GameVars.current_state == GameVars.GAME_STATE:
        GameFunctions.run_game_state()

    elif GameVars.current_state == GameVars.PAUSE_STATE:
        pass

    elif GameVars.current_state == GameVars.END_STATE:
        GameFunctions.run_end_state()

    elif GameVars.current_state == GameVars.TYPING_TEST_STATE:
        GameFunctions.run_typing_test_state()

    pygame.display.update()