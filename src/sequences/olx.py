from src.sequences.sequence import Sequence


WINDOW = "div > div"
MAIN_ELEMENT = "div > div > div > div > div"
SIDE_ELEMENT = "div > div > div"


class OLXSequence(Sequence):
    def __init__(self):
        self.title = "div > div > div > div > div > div > div > div > div > h4"
        self.price = "div > div > div > div > div > div > div > div > h3"
        
