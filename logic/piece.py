class Piece:
    def __init__(self, pos:tuple[int,int]):
        self.pos = pos
        self.img = None

    def show(self):
        self.img.show()

    def __repr__(self):
        return f"P{self.pos}"

    __slots__ = ('pos','img')