import sys
import pygame
from pygame.locals import *
from frontend.puzzle_surface import PuzzleSurface
from logic.image_maker import ImageMaker
from frontend.widgets import Widgets
from frontend.operators import Operators


FPS = 10
SHAPE = 4
WIDTH, HEIGHT = 900, 600
MARGIN = 20
SIZE = (HEIGHT - 2 * MARGIN) / SHAPE
TITLE_CENTER = (750, 150)
TITLE_SIZE = 50
SELECTION_CENTER = (750, 320)
SELECTION_SIZE = 30
START_CENTER = (750, 420)
START_SIZE = 60
COMPLETE_CENTER = (750, 530)
COMPLETE_SIZE = 30

# Pygame initialization.
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Slide Puzzle')
zone = pygame.Surface((HEIGHT, HEIGHT))
clock = pygame.time.Clock()

# Game initialization.
maker = ImageMaker(shape=SHAPE)
maker.set_image(r'images\2.png')
puzzle = PuzzleSurface(zone, shape=SHAPE)
operators = Operators(puzzle, maker, zone)
widgets = Widgets(screen, r'font\ShuHei.otf')

# Draw basic widgets.
screen.fill('white')
zone.fill('white')
puzzle.display(MARGIN, SIZE)
operators.display_full(MARGIN, HEIGHT - 2 * MARGIN)
widgets.draw_title(TITLE_CENTER, TITLE_SIZE)
widgets.draw_line(HEIGHT, HEIGHT)
selection_rect = widgets.draw_selection(SELECTION_CENTER, SELECTION_SIZE)
start_rect = widgets.draw_start(START_CENTER, START_SIZE)

game_start = False
game_win = False
win_effect = False
alpha = 0

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN and event.button == 1:

            # If clicked selection
            if selection_rect.collidepoint(event.pos):
                operators.select_image()
                zone.fill('white')
                operators.display_full(MARGIN, HEIGHT - 2 * MARGIN)

            # If clicked start
            elif start_rect.collidepoint(event.pos):
                operators.start(SIZE)
                game_start = True
                game_win = False
                alpha = 0

            # If clicked puzzle
            elif game_start and MARGIN <= event.pos[0] <= HEIGHT - MARGIN and MARGIN <= event.pos[1] <= HEIGHT - MARGIN:
                r = int((event.pos[1] - MARGIN) // SIZE)
                c = int((event.pos[0] - MARGIN) // SIZE)
                puzzle.click((r, c))
                if puzzle.complete():
                    game_win = win_effect = True

    if game_start:
        zone.fill('white')
        puzzle.display(MARGIN, SIZE)

    if game_win:
        widgets.draw_complete(COMPLETE_CENTER, COMPLETE_SIZE)
        screen.blit(zone, (0, 0))

        # Draw alpha changing effect
        if win_effect:
            image = operators.get_last_img(SIZE)

            fps = 30
            rect = (MARGIN + SIZE * (puzzle.shape - 1), MARGIN + SIZE * (puzzle.shape - 1))
            while alpha <= 255:
                image.set_alpha(alpha)
                screen.blit(image, rect)
                pygame.display.flip()
                clock.tick(fps)
                alpha += 255 // (1.5 * fps)

            win_effect = game_start = False

        operators.display_full(MARGIN, HEIGHT - 2 * MARGIN)

    screen.blit(zone, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
