class Piece:
    """
    Each piece of the puzzle.
    """

    def __init__(self, pos: tuple[int, int]):
        self.pos = pos
        self.img = None

    def show(self):
        """
        Debugging tool.
        """
        self.img.show()

    def __repr__(self):
        return f"P{self.pos}"

    __slots__ = ('pos', 'img')
