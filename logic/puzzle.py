from itertools import product
from logic.piece import Piece
from logic.image_maker import ImageMaker
import random


class Puzzle:
    def __init__(self, shape):
        self.shape = shape
        self.map = None

    def __repr__(self):
        rep = ''
        for i in self.map:
            rep += str(i) + '\n'
        rep.removesuffix('\n')
        return rep

    def __getitem__(self, item):
        return self.map[item]

    def generate(self):
        """
        Generate the shuffled puzzle.
        """
        # Initiallize 2D array
        pieces = [[None for _ in range(self.shape)] for _ in range(self.shape)]

        for r, c in product(range(self.shape), repeat=2):
            if (r != self.shape - 1) or (c != self.shape - 1):
                # noinspection PyTypeChecker
                pieces[r][c] = Piece((r, c))

        self.map = pieces
        self._shuffle()

    def _shuffle(self):
        """
        Shuffle the puzzle.
        """
        time = 30
        exclude = None

        for _ in range(time):
            for r, c in product(range(self.shape), repeat=2):
                if not self[r][c]:

                    # Get possible move.
                    option = []
                    if r != 0 and exclude != 'u':
                        option.append('u')
                    if r != self.shape - 1 and exclude != 'd':
                        option.append('d')
                    if c != 0 and exclude != 'l':
                        option.append('l')
                    if c != self.shape - 1 and exclude != 'r':
                        option.append('r')

                    # Exclude option to prevent moving back.
                    choice = random.choice(option)
                    match choice:
                        case 'u':
                            self[r - 1][c], self[r][c] = self[r][c], self[r - 1][c]
                            exclude = 'd'
                        case 'd':
                            self[r + 1][c], self[r][c] = self[r][c], self[r + 1][c]
                            exclude = 'u'
                        case 'l':
                            self[r][c - 1], self[r][c] = self[r][c], self[r][c - 1]
                            exclude = 'r'
                        case 'r':
                            self[r][c + 1], self[r][c] = self[r][c], self[r][c + 1]
                            exclude = 'l'
                        case _:
                            raise Exception

    def create_image(self, image_maker: ImageMaker):
        """
        Create image for each pieces in the puzzle.
        """
        for r, c in product(range(self.shape), repeat=2):
            image_maker.split(self[r][c])

    def click(self, pos: tuple[int, int]):
        """
        Return bool is used to shuffle.
        """
        r, c = pos[0], pos[1]
        if r != 0 and not self[r - 1][c]:
            self[r - 1][c], self[r][c] = self[r][c], self[r - 1][c]
        elif r != self.shape - 1 and not self[r + 1][c]:
            self[r + 1][c], self[r][c] = self[r][c], self[r + 1][c]
        elif c != 0 and not self[r][c - 1]:
            self[r][c - 1], self[r][c] = self[r][c], self[r][c - 1]
        elif c != self.shape - 1 and not self[r][c + 1]:
            self[r][c + 1], self[r][c] = self[r][c], self[r][c + 1]
        else:
            return False
        return True

    def complete(self):
        for r, c in product(range(self.shape), repeat=2):
            if self[r][c] and self[r][c].pos != (r, c):
                return False
        return True
