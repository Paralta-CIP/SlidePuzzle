import pygame
from itertools import product
from logic.puzzle import Puzzle
from frontend.piece_surface import PieceSurface


class PuzzleSurface(Puzzle):
    """
    Pygame-frontend puzzle.
    """

    def __init__(self, screen: pygame.Surface, shape):
        super().__init__(shape)
        self.screen = screen

    def convert_all_image(self, size: int | float):
        """
        Convert all the pieces in the puzzle into pugame Surface.
        """
        for r, c in product(range(self.shape), repeat=2):
            if self[r][c]:
                # noinspection PyUnresolvedReferences
                self[r][c].convert_pygame_image(size)

    @staticmethod
    def _create_piece(pos: tuple[int, int]):
        """
        Override the creating method.
        """
        return PieceSurface(pos)

    def display(self, margin: int, size: int | float):
        """
        Display the full puzzle status.
        """
        if self.map:
            for r, c in product(range(self.shape), repeat=2):
                if self[r][c]:
                    rect = (margin + c * size, margin + r * size)
                    self.screen.blit(self[r][c].img, rect)
