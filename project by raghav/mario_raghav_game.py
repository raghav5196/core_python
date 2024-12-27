import sys
import pygame
import io

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("mario by raghav")

white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)

Clock = pygame.time.Clock()
FPS = 60

player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 100
player_velocity = 5
jumping = False
falling = False
jumping_height = 10
velocity_y = 0

ground_rect = pygame.Rect(0, screen_height - 100, screen_width, 100)
player = pygame.Rect(player_x, player_y, player_width, player_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        player.x -= player_velocity
    if key[pygame.K_RIGHT]:
        player.x += player_velocity

    if not jumping and key[pygame.K_SPACE]:
        jumping = True
        velocity_y = -jumping_height

    if jumping:
        player.y += velocity_y
        velocity_y += 1  # Gravity effect
        if player.y >= screen_height - player_height - 100:
            player.y = screen_height - player_height - 100
            jumping = False
            velocity_y = 0

    if player.x < 0:
        player.x = 0
    if player.x > screen_width - player_width:
        player.x = screen_width - player_width

        # Drawing everything
    screen.fill(white)  # Fill screen with white

    # Draw ground
    pygame.draw.rect(screen, green, ground_rect)

    # Draw player
    pygame.draw.rect(screen, blue, player)

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    Clock.tick(FPS)
