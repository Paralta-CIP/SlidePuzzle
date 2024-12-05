from PIL import Image
from logic.piece import Piece


class ImageMaker:
    def __init__(self, shape: int):
        self.img = None
        self.size = None
        self.shape = shape
        self.last_img = None

    def set_image(self, path: str):
        self.img = Image.open(path)
        self._cut_square()
        self._get_last_image()

    def _cut_square(self):
        """
        Cut the image into square.
        """
        width, height = self.img.size
        if width == height:
            pass
        elif width < height:
            y = (height - width) / 2
            box = (0, y, width, height - y)
            self.img = self.img.crop(box)
        elif width > height:
            x = (width - height) / 2
            box = (x, 0, width - x, height)
            self.img = self.img.crop(box)
        self.size, _ = self.img.size

    def _get_last_image(self):
        box = (self.size * (1 - 1 / self.shape), self.size * (1 - 1 / self.shape), self.size, self.size)
        self.last_img = self.img.crop(box)

    def show(self):
        self.img.show()

    def split(self, piece: Piece | None):
        """
        Split the image into slices and match them to each piece.
        """
        if piece:
            r, c = piece.pos[0], piece.pos[1]
            delta = self.size / self.shape
            box = (c * delta, r * delta, (c + 1) * delta, (r + 1) * delta)
            piece.img = self.img.crop(box)


if __name__ == '__main__':
    ...
