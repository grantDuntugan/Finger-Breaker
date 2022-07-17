from english_words import english_words_lower_alpha_set

'''System Constants'''
SCREEN = None
SCREEN_INFO = None
SCREEN_WIDTH = None
SCREEN_HEIGHT = None

'''Game State Variables'''
current_state = 0
START_STATE = 0
GAME_STATE = 1
PAUSE_STATE = 2
END_STATE = 3
TYPING_TEST_STATE = 4

'''Intermediate Game State Variables'''
enemy_state = 0
word_state = 0
ENEMY_DEAD = 0
ENEMY_ALIVE = 1
WORD_NOT_CREATED = 0
WORD_BEING_TYPED = 1

'''Start Screen Variables'''
secret_stack = []
start_button = None
title_text = None

'''Game Variables'''
current_enemy = None
health_bar = None
enemy_group = None

'''Typing Test Variables'''
score = 0
lives = 5
time_out = 8 # Time to type
timer_running = False
start_time = 0
score_text = None
lives_text = None
time_text = None

'''Shared Game and Typing Test Variables'''
stack = [] # Keeps track of typing order
user_stack = [] # Keeps track of typing input
letters_typed_text = None
word_to_type_text = None
def create_wordlib(num_words):
    my_set = []
    counter = 0
    for val in english_words_lower_alpha_set:
        my_set.append(val)
        counter += 1
        if (counter > num_words):
            break
    return my_set
word_lib = create_wordlib(3000)


