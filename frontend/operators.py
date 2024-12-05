from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pygame
from frontend.puzzle_surface import PuzzleSurface
from logic.image_maker import ImageMaker


class Operators:
    """
    Frontend operations. Manage click and display.
    """

    def __init__(self, puzzle: PuzzleSurface, maker: ImageMaker, screen: pygame.Surface):
        self.puzzle = puzzle
        self.maker = maker
        self.screen = screen

    def select_image(self):
        """
        Image selection.
        """
        root = Tk()
        root.withdraw()
        path = askopenfilename()
        if path:
            self.maker.set_image(path)
        root.destroy()

    def start(self, size: int | float):
        """
        Generate the puzzle.
        """
        self.puzzle.generate()
        self.puzzle.create_image(self.maker)
        self.puzzle.convert_all_image(size)

    def display_full(self, margin: int, full_size: int):
        """
        Display full image before starting and after completion.
        :param full_size: The size of the full image.
        """
        image_byte = self.maker.img.tobytes()
        image_size = self.maker.img.size
        image = pygame.image.fromstring(image_byte, image_size, self.maker.img.mode)
        image = pygame.transform.scale(image, (full_size, full_size))
        rect = (margin, margin)
        self.screen.blit(image, rect)

    def get_last_img(self, size: int | float):
        """
        Get the last image of the puzzle to display completion effect.
        """
        image_byte = self.maker.last_img.tobytes()
        image_size = self.maker.last_img.size
        image = pygame.image.fromstring(image_byte, image_size, self.maker.img.mode)
        image = pygame.transform.scale(image, (size, size))
        return image
