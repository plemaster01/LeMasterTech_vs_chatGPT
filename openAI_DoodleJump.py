import pygame
import random

# Initialize pygame
pygame.init()

# Set up the pygame window
window_size = (400, 600)
pygame.display.set_caption('Doodle Jump')
screen = pygame.display.set_mode(window_size)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player ( manually fixed mapping to player image)
player_image = pygame.transform.scale(pygame.image.load('doodle.png'), (100, 50))
player_pos = [50, 50]
player_speed = 5

# Set up the platforms ( manually drew instead of getting an image)
platform_image = pygame.image.load('platform.png')
platform_width = 80
platform_height = 20
platforms = []
for i in range(5):
    platform_x = random.randint(0, window_size[0] - platform_width)
    platform_y = random.randint(0, window_size[1] - platform_height)
    platforms.append([platform_x, platform_y])

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_pos[1] -= player_speed

    # Update the player position
    player_pos[1] += player_speed

    # Check for collision with platforms
    for platform in platforms:
        if player_pos[0] + player_image.get_width() > platform[0] and player_pos[0] < platform[0] + platform_width:
            if player_pos[1] + player_image.get_height() > platform[1] and player_pos[1] < platform[1] + platform_height:
                player_pos[1] = platform[1] - player_image.get_height()

    # Draw the game objects (changed screen fill from black to white)
    screen.fill(WHITE)
    for platform in platforms:
        screen.blit(platform_image, platform)
    screen.blit(player_image, player_pos)
    pygame.display.update()

# Quit pygame
pygame.quit()