import pygame
def handle_keys(event, user_stack):
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
        elif event.key == pygame.K_z:
            user_stack.append("z")
        elif event.key == pygame.K_x:
            user_stack.append("x")
        elif event.key == pygame.K_c:
            user_stack.append("c")
        elif event.key == pygame.K_r:
            user_stack.append("r")
        elif event.key == pygame.K_f:
            user_stack.append("f")
        elif event.key == pygame.K_v:
            user_stack.append("v")
        elif event.key == pygame.K_t:
            user_stack.append("t")
        elif event.key == pygame.K_y:
            user_stack.append("y")
        elif event.key == pygame.K_u:
            user_stack.append("u")
        elif event.key == pygame.K_i:
            user_stack.append("i")
        elif event.key == pygame.K_o:
            user_stack.append("o")
        elif event.key == pygame.K_p:
            user_stack.append("p")
        elif event.key == pygame.K_g:
            user_stack.append("g")
        elif event.key == pygame.K_h:
            user_stack.append("h")
        elif event.key == pygame.K_j:
            user_stack.append("j")
        elif event.key == pygame.K_k:
            user_stack.append("k")
        elif event.key == pygame.K_l:
            user_stack.append("l")
        elif event.key == pygame.K_b:
            user_stack.append("b")
        elif event.key == pygame.K_n:
            user_stack.append("n")
        elif event.key == pygame.K_m:
            user_stack.append("m")
        elif event.key == pygame.K_BACKSPACE and len(user_stack) != 0:
            user_stack.pop()