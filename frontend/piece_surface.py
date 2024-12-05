import pygame
from logic.piece import Piece


class PieceSurface(Piece):
    def __init__(self, pos: tuple[int, int]):
        super().__init__(pos)

    def convert_pygame_image(self, size: int | float):
        image_byte = self.img.tobytes()
        image_size = self.img.size
        image = pygame.image.fromstring(image_byte, image_size, self.img.mode)
        image = pygame.transform.scale(image, (size, size))
        self.img = image
