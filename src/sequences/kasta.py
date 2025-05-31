from src.sequences.sequence import Sequence


WINDOW = "div > div > div > div > div > div > div > div > div > div > div > form"


class KastaSequence(Sequence):
    def __init__(self):
        self.title = WINDOW + ' > h1'
        self.price = WINDOW + " > div > div > div > div > span"
