import random
import pygame
import time
from systems import GameVars
from components import text, HealthBar
from entities import Enemy

def listen_for_start():
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        if GameVars.start_button.in_bounds(pos):
            GameVars.current_state = GameVars.GAME_STATE

def get_next_word():
    GameVars.stack = []
    GameVars.user_stack = []
    word = random.choice(GameVars.word_lib)
    for char in word:
        GameVars.stack.append(char)
    GameVars.word_state = GameVars.WORD_BEING_TYPED

def get_and_set_next_word():
    GameVars.stack = []
    GameVars.user_stack = []
    word = random.choice(GameVars.word_lib)
    for char in word:
        GameVars.stack.append(char)
    GameVars.start_time = time.time()
    GameVars.timer_running = True
    GameVars.word_to_type_text = text.create_TT_word_to_type_text()

def end_game():
    GameVars.current_state = GameVars.END_STATE

def set_next_enemy():
    GameVars.current_enemy = Enemy.get_random_enemy()
    GameVars.enemy_group.add(GameVars.current_enemy)
    GameVars.health_bar = HealthBar.HealthBar(GameVars.current_enemy.health)
    GameVars.word_state = GameVars.WORD_NOT_CREATED
    GameVars.enemy_state = GameVars.ENEMY_ALIVE

def set_and_draw_screen():
    GameVars.word_to_type_text = text.create_word_to_type_text()
    GameVars.letters_typed_text = text.create_letters_typed_text()
    GameVars.player_money_text = text.create_player_money_text()
    GameVars.player_damage_text = text.create_dpw_text()
    GameVars.player_money_text.draw()
    GameVars.enemy_group.draw(GameVars.SCREEN)
    GameVars.health_bar.draw()
    GameVars.word_to_type_text.draw()
    GameVars.letters_typed_text.draw()
    GameVars.player_damage_text.draw()

def deal_damage_on_typing_word():
    if GameVars.user_stack == GameVars.stack:
        GameVars.current_enemy.health -= GameVars.player_damage
        GameVars.health_bar.current_health -= GameVars.player_damage
        GameVars.word_state = GameVars.WORD_NOT_CREATED
        GameVars.player_money += 3

def run_start_state():
    GameVars.title_text = text.create_title_text()
    GameVars.title_text.draw()
    GameVars.start_button.draw()

    if "".join(GameVars.secret_stack) == "test":
        GameVars.current_state = GameVars.TYPING_TEST_STATE

def run_game_state():
    GameVars.SCREEN.fill((0, 0, 0))

    if GameVars.enemy_state == GameVars.ENEMY_DEAD:
        set_next_enemy()

    if GameVars.enemy_state == GameVars.ENEMY_ALIVE:
        if GameVars.word_state == GameVars.WORD_NOT_CREATED:
            get_next_word()

        deal_damage_on_typing_word()

        if (GameVars.current_enemy.health <= 0):
            GameVars.enemy_state = GameVars.ENEMY_DEAD
            GameVars.enemy_group.empty()
            GameVars.player_money += 50
            GameVars.enemies_killed += 1

        set_and_draw_screen()

    pygame.display.update()

'''Typing Test Functions'''
def run_typing_test_state():
    GameVars.SCREEN.fill((0, 0, 0))

    if (GameVars.timer_running == False):
        get_and_set_next_word()

    if time.time() - GameVars.start_time >= GameVars.time_out:
        subtract_life()
        if GameVars.lives == 0:
            end_game()

    if GameVars.user_stack == GameVars.stack:
        add_point()

    set_and_draw_text()

def run_end_state():
    GameVars.SCREEN.fill((0, 0, 0))
    text.draw_wrapped_congrats_text()

def add_point():
    GameVars.timer_running = False
    GameVars.score += 1
    if (GameVars.time_out > 2):
        if GameVars.score % 3 == 0:
            GameVars.time_out -= 1

def subtract_life():
    GameVars.lives -= 1
    GameVars.timer_running = False

def set_and_draw_text():
    GameVars.score_text = text.create_score_text()
    GameVars.lives_text = text.create_lives_text()
    GameVars.time_text = text.create_time_text(GameVars.start_time)
    GameVars.letters_typed_text = text.create_TT_letters_typed_text()

    GameVars.score_text.draw()
    GameVars.lives_text.draw()
    GameVars.time_text.draw()
    GameVars.word_to_type_text.draw()
    GameVars.letters_typed_text.draw()