import pygame
from itertools import product
from logic.puzzle import Puzzle
from front.piece_surface import PieceSurface


class PuzzleSurface(Puzzle):
    def __init__(self, screen:pygame.Surface, shape):
        super().__init__(shape)
        self.screen = screen

    def convert_all_image(self, size:int|float):
        for r, c in product(range(self.shape), repeat=2):
            if self[r][c]:
                # noinspection PyUnresolvedReferences
                self[r][c].convert_pygame_image(size)

    def generate(self):
        """
        Generate the shuffled puzzle.
        """
        # Initiallize 2D array
        pieces = [[None for _ in range(self.shape)] for _ in range(self.shape)]

        for r, c in product(range(self.shape), repeat=2):
            if (r != self.shape - 1) or (c != self.shape - 1):
                # noinspection PyTypeChecker
                pieces[r][c] = PieceSurface((r,c))

        self.map = pieces
        self._shuffle()

    def display(self, margin:int, size:int|float):
        if self.map:
            for r, c in product(range(self.shape), repeat=2):
                if self[r][c]:
                    rect = (margin+c*size, margin+r*size)
                    self.screen.blit(self[r][c].img, rect)
