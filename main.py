import pygame
import random
import time
import text
pygame.init()

lib = ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']
stack = [] # Keeps track of typing order
user_stack = [] # Keeps track of typing input
difficulty = 6 # Num letters during encounter
timeout = 3 # Time to type

timegoing = False

screen = pygame.display.set_mode((500, 500))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                user_stack.append("q")
            elif event.key == pygame.K_w:
                user_stack.append("w")
            elif event.key == pygame.K_e:
                user_stack.append("e")
            elif event.key == pygame.K_r:
                user_stack.append("r")
            elif event.key == pygame.K_a:
                user_stack.append("a")
            elif event.key == pygame.K_s:
                user_stack.append("s")
            elif event.key == pygame.K_d:
                user_stack.append("d")
            elif event.key == pygame.K_f:
                user_stack.append("f")
            elif event.key == pygame.K_BACKSPACE and len(user_stack) != 0:
                user_stack.pop()
            print(user_stack)
    
    if (timegoing == False):
        stack = []
        user_stack = []
        for i in range(difficulty):
            letter = random.choice(lib)
            stack.append(letter)
        start = time.time()
        print(stack)
        timegoing = True
        text_to_type = text.Text(screen, " ".join(stack), 100, (255, 255, 255), 250, 0)
    
    if time.time() - start >= timeout:
        print("Time out!")
        timegoing = False
        break
    if user_stack == stack:
        timegoing = False
        print("GJ!")

    text_typed = text.Text(screen, " ".join(user_stack), 100, (255, 0, 255), 250, 350)
    
    screen.fill((0,0,0))
    text_to_type.draw()
    text_typed.draw()
    pygame.display.update()