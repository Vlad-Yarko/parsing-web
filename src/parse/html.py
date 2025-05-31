from typing import Optional
from abc import abstractmethod

from bs4 import BeautifulSoup

from src.parse.parse import Parse


class HTMLParse(Parse):
    def __init__(
        self,
        html: str,
        parse_engine: Optional[str] = 'lxml'
        ):
        self.html = html
        self.parse_engine = parse_engine
        self.soup = BeautifulSoup(self.html, self.parse_engine)
    
    @abstractmethod
    def parse(self):    
        pass
    
    def parse_by_inheritance_one(self, inheritance: str):
        element = self.soup.select_one(inheritance)
        # return element
        return element.text
    
    def parse_by_inheritance_group(self, inheritance: str):
        elements = self.soup.select(inheritance)
        return elements
