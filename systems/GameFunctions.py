from systems import GameVars
from components import text
import random

def get_word_from_lib():
    GameVars.stack = []
    GameVars.user_stack = []
    word = random.choice(GameVars.word_lib)
    for char in word:
        GameVars.stack.append(char)


def add_point_and_get_next_word():
    GameVars.timer_running = False
    GameVars.score += 1
    if (GameVars.time_out > 2):
        if GameVars.score % 3 == 0:
            GameVars.time_out -= 1

def subtract_life():
    GameVars.lives -= 1
    GameVars.timer_running = False

def end_game():
    GameVars.state_game = False
    GameVars.state_end = True

def set_and_draw_text():
    GameVars.score_text = text.create_score_text()
    GameVars.lives_text = text.create_lives_text()
    GameVars.time_text = text.create_time_text(GameVars.start_time)
    GameVars.letters_typed_text = text.create_letters_typed_text()

    GameVars.score_text.draw()
    GameVars.lives_text.draw()
    GameVars.time_text.draw()
    GameVars.word_to_type_text.draw()
    GameVars.letters_typed_text.draw()
