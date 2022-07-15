import pygame
import os
import random
import time
from components import text, button
from systems import keyhandle, initialise, constants
os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pygame.init()

constants.SCREEN_INFO = pygame.display.Info() # You have to call this before pygame.display.set_mode()
constants.SCREEN_WIDTH = constants.SCREEN_INFO.current_w
constants.SCREEN_HEIGHT = constants.SCREEN_INFO.current_h

state_start = True
state_game = False
state_pause = False
state_end = False

stack = [] # Keeps track of typing order
user_stack = [] # Keeps track of typing input



constants.SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = constants.SCREEN
start_button = button.create_start_button()
my_set = initialise.create_wordlib(3000)




score = 0
timer_running = False
lives = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if state_start:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if start_button.in_bounds(pos):
                    state_start = False
                    state_game = True

        elif state_game:
            keyhandle.handle_keys(event, user_stack)


    if state_start:
        title_text = text.create_title_text()
        title_text.draw()
        start_button.draw()

    elif state_game:
        if (timer_running == False):
            stack = []
            user_stack = []
            word = random.choice(my_set)
            for char in word:
                stack.append(char)

            start = time.time()
            timer_running = True
            text_to_type = text.Text(screen, "".join(stack), 100, (255, 255, 255), constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)

        if time.time() - start >= constants.TIME_OUT:
            lives -= 1
            timer_running = False
            if lives == 0:
                state_game = False
                state_end = True

        if user_stack == stack:
            timer_running = False
            score += 1
            if (constants.TIME_OUT > 2):
                if score % 3 == 0:
                    constants.TIME_OUT -= 1


        text_time = text.Text(screen, str(int(time.time() - start - constants.TIME_OUT) * -1), 100, (255, 0, 0), constants.SCREEN_WIDTH //2 , constants.SCREEN_HEIGHT // 8)
        text_typed = text.Text(screen, "".join(user_stack), 100, (255, 0, 255), constants.SCREEN_WIDTH // 2, (constants.SCREEN_HEIGHT // 3) * 2)

        screen.fill((0,0,0))
        text_score = text.Text(screen, "Score: " + str(score), 100, (0, 250, 0), constants.SCREEN_WIDTH//8, constants.SCREEN_HEIGHT // 8)
        text_score.draw()

        text_lives = text.Text(screen, "Lives: " + str(lives), 100, (0, 250, 0), constants.SCREEN_WIDTH//8, (constants.SCREEN_HEIGHT//8) * 2)
        text_lives.draw()

        text_time.draw()
        text_to_type.draw()
        text_typed.draw()
    elif state_pause:
        pass

    elif state_end:
        screen.fill((0,0,0))
        text_finish = text.Text(screen, "Congrats! Your score was " + str(score) + ".", 150, (0, 250, 0), constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
        text.drawText(screen, "Congrats! Your score was " + str(score) + ".", (0, 250, 0), (0, constants.SCREEN_HEIGHT // 3, constants.SCREEN_WIDTH, (constants.SCREEN_HEIGHT//3) * 2), 150)
    pygame.display.update()