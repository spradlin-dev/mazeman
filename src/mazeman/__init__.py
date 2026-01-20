import pygame

from mazeman.player import Player
from mazeman.maze_generator import MazeGenerator

cell_size = 40
cols, rows = 32, 18

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    generator = MazeGenerator(cols, rows)
    return screen, clock, generator

def main():
    """Main entry point for the maze game."""
    screen, clock, generator = init_game()

    player = Player(0, 0)
    maze_walls = generator.generate()  # Called once at start

    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        generator.draw(screen, cell_size)

        keys = pygame.key.get_pressed()

        player.update(dt, keys)
        player.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

