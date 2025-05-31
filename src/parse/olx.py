from typing import Optional

from src.parse.web_product import WebProduct
from src.sequences.olx import OLXSequence


class OLXParse(WebProduct):
    def __init__(self, html: str, parse_engine: Optional[str] = 'lxml'):
        super().__init__(html, parse_engine)
        self.sequence = OLXSequence()
        
    def parse_price_by_inheritance(self):
        elements = self.parse_by_inheritance_group(self.price_sequence)
        self.price = elements[1].text
