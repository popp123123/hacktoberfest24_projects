import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 720, 480
SPEED = 10
BLOCK_SIZE = 20

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the snake and food
snake = [(WIDTH // 2, HEIGHT // 2)]
food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
        random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
direction = 'Right'

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'Down':
                direction = 'Up'
            elif event.key == pygame.K_DOWN and direction != 'Up':
                direction = 'Down'
            elif event.key == pygame.K_LEFT and direction != 'Right':
                direction = 'Left'
            elif event.key == pygame.K_RIGHT and direction != 'Left':
                direction = 'Right'

    # Move the snake
    head = (snake[-1][0] + (BLOCK_SIZE if direction == 'Right' else -BLOCK_SIZE if direction == 'Left' else 0),
            snake[-1][1] + (BLOCK_SIZE if direction == 'Down' else -BLOCK_SIZE if direction == 'Up' else 0))
    snake.append(head)

    # Check for collisions with food
    if snake[-1] == food:
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop(0)

    # Check for collisions with walls or self
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
            snake[-1] in snake[:-1]):
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, WHITE, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    # Update the display
    pygame.display.flip()
    pygame.time.delay(1000 // SPEED)
