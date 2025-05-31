from abc import abstractmethod
from typing import Optional

from src.parse.html import HTMLParse


class Product( HTMLParse):
    def __init__(self, html: str, parse_engine: Optional[str] = 'lxml'):
        super().__init__(html, parse_engine)
        
    @abstractmethod
    def parse(self):
        pass
