import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Colors
WHITE = (255, 255, 255)  # score and score counting
BLACK = (0, 0, 0)  # background
RED = (255, 0, 0)  # boll
BLUE = (0, 0, 255)  # ground

# Game settings
clock = pygame.time.Clock()
FPS = 60
score =0
font = pygame.font.Font(None, 36)

# Player settings
player_width, player_height = 100, 20
player_x, player_y = WIDTH // 2 - player_width // 2, HEIGHT - 30
player_speed = 12

# Ball settings
ball_radius = 15
ball_x = random.randint(0, WIDTH - ball_radius)
ball_y = -ball_radius
ball_speed = 5

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Ball movement
    ball_y += ball_speed

    # Check if the ball hits the paddle
    if (player_y < ball_y + ball_radius < player_y + player_height and
            player_x < ball_x < player_x + player_width):
        score += 1
        ball_y = -ball_radius
        ball_x = random.randint(0, WIDTH - ball_radius)

    # Check if the ball hits the ground
    if ball_y > HEIGHT:
        running = False

    # Draw player and ball
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
