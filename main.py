import pygame
import os 
import random
import time
from english_words import english_words_lower_alpha_set
from components import text, button
from systems import keyhandle

os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pygame.init()

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
screen_width,screen_height = info.current_w,info.current_h

STATE_START = True
STATE_GAME = False
STATE_PAUSE = False
STATE_END = False

LIB = ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 'z', 'x', 'c', 'v', 't', 'y', 'u', 'i', 'o', 'p', 'g', 'h', 'j', 'k', 'l', 'b', 'n', 'm']
stack = [] # Keeps track of typing order
user_stack = [] # Keeps track of typing input
difficulty = 6 # Num letters during encounter
timeout = 8 # Time to type

timegoing = False

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

start_button = button.Button(screen_width // 2 - screen_width // 10, (screen_height // 3) * 2, screen_width //5, screen_height //10, "Start")



my_set = []
counter = 0
for val in english_words_lower_alpha_set:
    my_set.append(val)
    counter += 1
    if (counter > 30000):
        break




score = 0
lives = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if STATE_START:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if start_button.in_bounds(pos):
                    STATE_START = False
                    STATE_GAME = True

        elif STATE_GAME:
            keyhandle.handle_keys(event, user_stack)


    if STATE_START:
        title_text = text.Text(screen, "Finger Breaker", 100, (255,255,255), screen_width/2, screen_height / 3)
        title_text.draw()
        start_button.draw(screen)
        
    elif STATE_GAME:
        if (timegoing == False):
            stack = []
            user_stack = []
            # CHARACTER BASED
            # for i in range(difficulty):
            #     letter = random.choice(my_set)
            #     stack.append(letter)
            word = random.choice(my_set)
            for char in word:
                stack.append(char)

            start = time.time()
            print(stack)
            timegoing = True
            text_to_type = text.Text(screen, "".join(stack), 100, (255, 255, 255), screen_width // 3, screen_height // 3)
        
        if time.time() - start >= timeout:
            lives -= 1
            timegoing = False
            if lives == 0:
                STATE_GAME = False
                STATE_END = True
            
        if user_stack == stack:
            timegoing = False
            score += 1
            if (timeout > 2):
                if score % 3 == 0:
                    timeout -= 1


        text_time = text.Text(screen, str(int(time.time() - start - timeout) * -1), 100, (255, 0, 0), screen_width //2 , screen_height // 8)
        text_typed = text.Text(screen, "".join(user_stack), 100, (255, 0, 255), screen_width // 2, (screen_height // 3) * 2)
        
        screen.fill((0,0,0))
        text_score = text.Text(screen, "Score: " + str(score), 100, (0, 250, 0), screen_width//8, screen_height // 8)
        text_score.draw()

        text_lives = text.Text(screen, "Lives: " + str(lives), 100, (0, 250, 0), screen_width//8, (screen_height//8) * 2)
        text_lives.draw()

        text_time.draw()
        text_to_type.draw()
        text_typed.draw()
    elif STATE_PAUSE:
        pass

    elif STATE_END:
        screen.fill((0,0,0))
        text_finish = text.Text(screen, "Congrats! Your score was " + str(score) + ".", 150, (0, 250, 0), screen_width // 2, screen_height // 2)
        text.drawText(screen, "Congrats! Your score was " + str(score) + ".", (0, 250, 0), (0, screen_height // 3, screen_width, (screen_height//3) * 2), 150)
    pygame.display.update()