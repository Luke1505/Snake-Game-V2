import settings
import file
import colors

import pygame
import random
import time
import asyncio
from operator import itemgetter


# One player Mode
def oneplayer(change_to, direction, fruit_position, fruit_spawn, snake_speed, score, snake_position, snake_body,
              game_size, pycolor, multiplayer, change_to2, direction2, score2, snake_position2, snake_body2, pycolor2):
    # Saving the initial value of the snake speed
    snake_speed_start = snake_speed
    powerup = random.choice(["speed", "double", "invincible", "slow"])
    if not multiplayer:
        while True:
            # Set Window Title
            pygame.display.set_caption('Snake Game')
            # Recognize keystrokes and change direction
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if settings.Button == 1:
                        if event.key == pygame.K_UP:
                            change_to = 'UP'
                        if event.key == pygame.K_DOWN:
                            change_to = 'DOWN'
                        if event.key == pygame.K_LEFT:
                            change_to = 'LEFT'
                        if event.key == pygame.K_RIGHT:
                            change_to = 'RIGHT'
                    elif settings.Button == 0:
                        if event.key == pygame.K_w:
                            change_to = 'UP'
                        if event.key == pygame.K_s:
                            change_to = 'DOWN'
                        if event.key == pygame.K_a:
                            change_to = 'LEFT'
                        if event.key == pygame.K_d:
                            change_to = 'RIGHT'
                    if event.key == pygame.K_SPACE:
                        # Instant Game Over
                        game_over(score, score2, snake_speed,
                                  game_size, pycolor, pycolor2)
                    if event.key == pygame.K_ESCAPE:
                        # Back to Main Menu
                        pygame.quit()
                        settings.reset_menu()
                # Close Game
                if event.type == pygame.QUIT:
                    quit()
            # Direction control
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
            # Moving the snake
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10
            # Snake body growing mechanism
            snake_body.insert(0, list(snake_position))
            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                if snake_speed_start == 10:
                    score += 0.5
                elif snake_speed_start == 20:
                    score += 1
                elif snake_speed_start == 30:
                    score += 1.5
                snake_speed += 0.5
                fruit_spawn = False
            else:
                snake_body.pop()
            # Spawn fruit
            if not fruit_spawn:
                fruit_position = [random.randrange(1, (settings.window_x // 10)) * 10,
                                  random.randrange(1, (settings.window_y // 10)) * 10]
            fruit_spawn = True
            settings.game_window.fill(pygame.Color(colors.black))
            # Draw snake
            for pos in snake_body:
                pygame.draw.rect(settings.game_window, pycolor,
                                 pygame.Rect(pos[0], pos[1], game_size, game_size))
            # Draw fruit
            pygame.draw.rect(settings.game_window, pygame.Color(colors.red), pygame.Rect(
                fruit_position[0], fruit_position[1], game_size, game_size))
            pygame.display.flip()
            # Window end set to other side of screen
            if snake_position[0] >= settings.window_x:
                snake_position[0] = 0
            if snake_position[1] >= settings.window_y:
                snake_position[1] = 0
            if snake_position[0] < 0:
                snake_position[0] = 720
            if snake_position[1] < 0:
                snake_position[1] = 480
            # Touching the snake body
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over(score, score2, snake_speed_start,
                              game_size, pycolor, pycolor2)
            # Show score
            show_score(colors.white, 'Corbel', 20, score)
            # Refresh game screen
            pygame.display.update()
            # Frame Per Second /Refresh Rate
            settings.fps.tick(snake_speed)


# Two player Mode
def twoplayer(change_to, direction, fruit_position, fruit_spawn, snake_speed, score, snake_position, snake_body,
              game_size,
              pycolor, Multiplayer, change_to2, direction2, score2, snake_position2, snake_body2, pycolor2):
    # Saving the initial value of the snake speed
    snake_speed_start = snake_speed
    powerup = random.choice(["speed", "double", "invincible", "slow", "swap"])
    # Double Check if Multiplayer is True
    if Multiplayer:
        # Set Window Title
        pygame.display.set_caption('Snake Game - Multiplayer')
        while True:
            # Recognize keystrokes and change direction
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to2 = 'UP'
                    elif event.key == pygame.K_DOWN:
                        change_to2 = 'DOWN'
                    elif event.key == pygame.K_LEFT:
                        change_to2 = 'LEFT'
                    elif event.key == pygame.K_RIGHT:
                        change_to2 = 'RIGHT'
                    elif event.key == pygame.K_w:
                        change_to = 'UP'
                    elif event.key == pygame.K_s:
                        change_to = 'DOWN'
                    elif event.key == pygame.K_a:
                        change_to = 'LEFT'
                    elif event.key == pygame.K_d:
                        change_to = 'RIGHT'
                    if event.key == pygame.K_SPACE:
                        # Instant Game Over
                        game_over(score, score2, snake_speed,
                                  game_size, pycolor, pycolor2)
                    if event.key == pygame.K_ESCAPE:
                        # Back to Main Menu
                        pygame.quit()
                        settings.reset_menu()
                # Close Game
                if event.type == pygame.QUIT:
                    quit()
            # we don't want the snakes to move into two
            # directions simultaneously
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
            if change_to2 == 'UP' and direction2 != 'DOWN':
                direction2 = 'UP'
            if change_to2 == 'DOWN' and direction2 != 'UP':
                direction2 = 'DOWN'
            if change_to2 == 'LEFT' and direction2 != 'RIGHT':
                direction2 = 'LEFT'
            if change_to2 == 'RIGHT' and direction2 != 'LEFT':
                direction2 = 'RIGHT'
            # Moving the snakes
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10
            if direction2 == 'UP':
                snake_position2[1] -= 10
            if direction2 == 'DOWN':
                snake_position2[1] += 10
            if direction2 == 'LEFT':
                snake_position2[0] -= 10
            if direction2 == 'RIGHT':
                snake_position2[0] += 10
            # Snake body growing mechanisms
            snake_body.insert(0, list(snake_position))
            snake_body2.insert(0, list(snake_position2))
            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                if snake_speed_start == 10:
                    score += 0.5
                elif snake_speed_start == 20:
                    score += 1
                elif snake_speed_start == 30:
                    score += 1.5
                snake_speed += 0.5
                fruit_spawn = False
            else:
                snake_body.pop()
            if snake_position2[0] == fruit_position[0] and snake_position2[1] == fruit_position[1]:
                if snake_speed_start == 10:
                    score2 += 0.5
                elif snake_speed_start == 20:
                    score2 += 1
                elif snake_speed_start == 30:
                    score2 += 1.5
                snake_speed += 0.5
                fruit_spawn = False
            else:
                snake_body2.pop()
            # Spawn fruit
            if not fruit_spawn:
                fruit_position = [random.randrange(1, (settings.window_x // 10)) * 10,
                                  random.randrange(1, (settings.window_y // 10)) * 10]
            fruit_spawn = True
            settings.game_window.fill(pygame.Color(colors.black))
            # Draw snake 1
            for pos in snake_body:
                pygame.draw.rect(settings.game_window, pycolor,
                                 pygame.Rect(pos[0], pos[1], game_size, game_size))
            # Draw snake 2
            for pos in snake_body2:
                pygame.draw.rect(settings.game_window, pycolor2,
                                 pygame.Rect(pos[0], pos[1], game_size, game_size))
            # Draw fruit
            pygame.draw.rect(settings.game_window, pygame.Color(colors.red), pygame.Rect(
                fruit_position[0], fruit_position[1], game_size, game_size))
            pygame.display.flip()
            # Window end set snake to other side of screen (Player 1)
            if snake_position[0] >= settings.window_x:
                snake_position[0] = 0
            if snake_position[1] >= settings.window_y:
                snake_position[1] = 0
            if snake_position[0] < 0:
                snake_position[0] = 720
            if snake_position[1] < 0:
                snake_position[1] = 480
            # Window end set snake to other side of screen (Player 2)
            if snake_position2[0] >= settings.window_x:
                snake_position2[0] = 0
            if snake_position2[1] >= settings.window_y:
                snake_position2[1] = 0
            if snake_position2[0] < 0:
                snake_position2[0] = 720
            if snake_position2[1] < 0:
                snake_position2[1] = 480
            # Touching the snake body (Player 1)
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over(score, score2, snake_speed_start,
                              game_size, pycolor, pycolor2)
            # Touching the snake body (Player 2)
            for block in snake_body2[1:]:
                if snake_position2[0] == block[0] and snake_position2[1] == block[1]:
                    game_over(score, score2, snake_speed_start,
                              game_size, pycolor, pycolor2)
            # Refresh game screen
            pygame.display.update()
            # Frame Per Second /Refresh Rate
            settings.fps.tick(snake_speed)


# Showing the Score at top Left
def show_score(color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(
        'Score : ' + str(score), True, pygame.Color(color))
    score_rect = score_surface.get_rect()
    settings.game_window.blit(score_surface, score_rect)


# Showing the Game Over Screen
def game_over(score, score2, snake_speed, game_size, pycolor, pycolor2):
    my_font = pygame.font.SysFont('Corbel', 50)
    offset = 40
    # Game Over Screen for Two Player Mode
    if settings.Multiplayer:
        game_over_surface = my_font.render(
            'Player 1 Score : ' + str(score), True, colors.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (
            settings.window_x / 2, settings.window_y / 4 + offset)
        settings.game_window.blit(game_over_surface, game_over_rect)
        game_over_surface2 = my_font.render(
            'Player 2 Score : ' + str(score2), True, pygame.Color(colors.red))
        game_over_rect2 = game_over_surface2.get_rect()
        game_over_rect2.midtop = (
            settings.window_x / 2, settings.window_y / 4 + offset + 50)
        settings.game_window.blit(game_over_surface2, game_over_rect2)
        pygame.display.flip()
    # Game Over Screen for Single Player Mode
    elif not settings.Multiplayer:
        count = 0
        player_name = settings.player.get()
        my_font2 = pygame.font.SysFont('Corbel', 30)
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, pygame.Color(colors.red))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (settings.window_x / 2, settings.window_y / 4)
        settings.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        # Player name can be Empty so we need to check if it is empty and Fill it with 'Player'
        if player_name == '':
            player_name = 'Player'
        # appending the player name and score to the List
        settings.nicknames.append([player_name, score])
        for i in settings.nicknames:
            # showing the player name and score in the game over screen
            if not count >= 10:
                names = my_font2.render(
                    f'{i[0]}', True, pygame.Color(colors.red))
                scores = my_font2.render(
                    f'{i[1]}', True, pygame.Color(colors.red))
                names_rect = names.get_rect()
                scores_rect = scores.get_rect()
                names_rect.midtop = (
                    (settings.window_x / 2) - 125, (settings.window_y / 4) + offset)
                scores_rect.midtop = (
                    (settings.window_x / 2) + 50, (settings.window_y / 4) + offset)
                settings.game_window.blit(names, names_rect.midtop)
                settings.game_window.blit(scores, scores_rect.midtop)
                pygame.display.flip()
                offset += 30
                count += 1
        # Saving the List sorted to the File if The Score was not 0
        if score != 0:
            file.save(sorted(settings.nicknames,
                      key=itemgetter(1), reverse=True))
    time.sleep(2)
    # Restarting the Game
    settings.reset(snake_speed, game_size, pycolor, pycolor2)