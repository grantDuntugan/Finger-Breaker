import pygame
from systems import GameVars

def handle_start_keys(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                GameVars.secret_stack.append("q")
            elif event.key == pygame.K_w:
                GameVars.secret_stack.append("w")
            elif event.key == pygame.K_e:
                GameVars.secret_stack.append("e")
            elif event.key == pygame.K_r:
                GameVars.secret_stack.append("r")
            elif event.key == pygame.K_a:
                GameVars.secret_stack.append("a")
            elif event.key == pygame.K_s:
                GameVars.secret_stack.append("s")
            elif event.key == pygame.K_d:
                GameVars.secret_stack.append("d")
            elif event.key == pygame.K_f:
                GameVars.secret_stack.append("f")
            elif event.key == pygame.K_z:
                GameVars.secret_stack.append("z")
            elif event.key == pygame.K_x:
                GameVars.secret_stack.append("x")
            elif event.key == pygame.K_c:
                GameVars.secret_stack.append("c")
            elif event.key == pygame.K_r:
                GameVars.secret_stack.append("r")
            elif event.key == pygame.K_f:
                GameVars.secret_stack.append("f")
            elif event.key == pygame.K_v:
                GameVars.secret_stack.append("v")
            elif event.key == pygame.K_t:
                GameVars.secret_stack.append("t")
            elif event.key == pygame.K_y:
                GameVars.secret_stack.append("y")
            elif event.key == pygame.K_u:
                GameVars.secret_stack.append("u")
            elif event.key == pygame.K_i:
                GameVars.secret_stack.append("i")
            elif event.key == pygame.K_o:
                GameVars.secret_stack.append("o")
            elif event.key == pygame.K_p:
                GameVars.secret_stack.append("p")
            elif event.key == pygame.K_g:
                GameVars.secret_stack.append("g")
            elif event.key == pygame.K_h:
                GameVars.secret_stack.append("h")
            elif event.key == pygame.K_j:
                GameVars.secret_stack.append("j")
            elif event.key == pygame.K_k:
                GameVars.secret_stack.append("k")
            elif event.key == pygame.K_l:
                GameVars.secret_stack.append("l")
            elif event.key == pygame.K_b:
                GameVars.secret_stack.append("b")
            elif event.key == pygame.K_n:
                GameVars.secret_stack.append("n")
            elif event.key == pygame.K_m:
                GameVars.secret_stack.append("m")
            elif event.key == pygame.K_BACKSPACE and len(GameVars.secret_stack) != 0:
                GameVars.secret_stack = []
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

def handle_game_keys(event):
    if event.type == pygame.KEYDOWN:
        pygame.mixer.music.play()
        if event.key == pygame.K_q:
            GameVars.user_stack.append("q")
        elif event.key == pygame.K_w:
            GameVars.user_stack.append("w")
        elif event.key == pygame.K_e:
            GameVars.user_stack.append("e")
        elif event.key == pygame.K_r:
            GameVars.user_stack.append("r")
        elif event.key == pygame.K_a:
            GameVars.user_stack.append("a")
        elif event.key == pygame.K_s:
            GameVars.user_stack.append("s")
        elif event.key == pygame.K_d:
            GameVars.user_stack.append("d")
        elif event.key == pygame.K_f:
            GameVars.user_stack.append("f")
        elif event.key == pygame.K_z:
            GameVars.user_stack.append("z")
        elif event.key == pygame.K_x:
            GameVars.user_stack.append("x")
        elif event.key == pygame.K_c:
            GameVars.user_stack.append("c")
        elif event.key == pygame.K_r:
            GameVars.user_stack.append("r")
        elif event.key == pygame.K_f:
            GameVars.user_stack.append("f")
        elif event.key == pygame.K_v:
            GameVars.user_stack.append("v")
        elif event.key == pygame.K_t:
            GameVars.user_stack.append("t")
        elif event.key == pygame.K_y:
            GameVars.user_stack.append("y")
        elif event.key == pygame.K_u:
            GameVars.user_stack.append("u")
        elif event.key == pygame.K_i:
            GameVars.user_stack.append("i")
        elif event.key == pygame.K_o:
            GameVars.user_stack.append("o")
        elif event.key == pygame.K_p:
            GameVars.user_stack.append("p")
        elif event.key == pygame.K_g:
            GameVars.user_stack.append("g")
        elif event.key == pygame.K_h:
            GameVars.user_stack.append("h")
        elif event.key == pygame.K_j:
            GameVars.user_stack.append("j")
        elif event.key == pygame.K_k:
            GameVars.user_stack.append("k")
        elif event.key == pygame.K_l:
            GameVars.user_stack.append("l")
        elif event.key == pygame.K_b:
            GameVars.user_stack.append("b")
        elif event.key == pygame.K_n:
            GameVars.user_stack.append("n")
        elif event.key == pygame.K_m:
            GameVars.user_stack.append("m")
        elif event.key == pygame.K_BACKSPACE and len(GameVars.user_stack) != 0:
            GameVars.user_stack.pop()
        elif event.key == pygame.K_UP:
            if GameVars.player_money >= 15:
                GameVars.player_damage += 10
                GameVars.player_money -= 15
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()