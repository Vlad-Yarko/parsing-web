from typing import Optional

from src.parse.product import Product
from src.sequences.sequence import Sequence


class WebProduct(Product):
    def __init__(self, html: str, parse_engine: Optional[str] = 'lxml'):
        super().__init__(html, parse_engine)
        self.title = None
        self.price = None
        self.sequence = Sequence()
        self.price_sequence = self.sequence.price
        self.title_sequence = self.sequence.title

    def parse_title_by_inheritance(self):
        self.title = self.parse_by_inheritance_one(self.title_sequence)
    
    def parse_price_by_inheritance(self):
        self.price = self.parse_by_inheritance_one(self.price_sequence)
    
    def parse(self):
        self.price_sequence = self.sequence.price
        self.title_sequence = self.sequence.title
        self.parse_title_by_inheritance()
        self.parse_price_by_inheritance()
