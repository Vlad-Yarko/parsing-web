from typing import Optional

from src.parse.web_product import WebProduct
from src.sequences.kasta import KastaSequence


class KastaParse(WebProduct):
    def __init__(self, html: str, parse_engine: Optional[str] = 'lxml'):
        super().__init__(html, parse_engine)
        self.sequence = KastaSequence()
