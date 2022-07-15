from english_words import english_words_lower_alpha_set

LIB = ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 'z', 'x',
       'c', 'v', 't', 'y', 'u', 'i', 'o', 'p', 'g', 'h',
       'j', 'k', 'l', 'b', 'n', 'm']
SCREEN = None
SCREEN_INFO = None
SCREEN_WIDTH = None
SCREEN_HEIGHT = None

start_button = None

stack = [] # Keeps track of typing order
user_stack = [] # Keeps track of typing input
score = 0
lives = 5
time_out = 8 # Time to type
timer_running = False
start_time = 0

state_start = True
state_game = False
state_pause = False
state_end = False

title_text = None
score_text = None
lives_text = None
time_text = None
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