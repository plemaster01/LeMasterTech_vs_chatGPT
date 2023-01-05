import pygame
from pygame import mixer
# Initialize pygame
pygame.init()

# Set up the pygame window
window_size = (400, 400)
pygame.display.set_caption('Drum Kit')
screen = pygame.display.set_mode(window_size)

# Load the drum sounds (manually remapped the sounds from openAI)
kick_sound = mixer.Sound('sounds\kick.WAV')
snare_sound = mixer.Sound('sounds\snare.WAV')
hi_hat_sound = mixer.Sound('sounds\hi hat.WAV')

# Set up the drum mapping
drum_mapping = {
    pygame.K_q: kick_sound,
    pygame.K_w: snare_sound,
    pygame.K_e: hi_hat_sound
}

# Run the game loop
running = True
while running:
    # Check for keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Play the drum sound if the corresponding key is pressed
            if event.key in drum_mapping:
                drum_mapping[event.key].play()

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()