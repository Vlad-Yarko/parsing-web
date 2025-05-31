from src.sequences.sequence import Sequence


WINDOW = "div > div > div > div"
INFO = "div > div > div"


class ShafaSequence(Sequence):
    def __init__(self):
        self.title = "div > div > div > div > div > div > div > h1"
        self.price = "div > div > div > div > div > div > div > div > div > span"
