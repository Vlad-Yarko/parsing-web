from abc import ABC, abstractmethod


class Parse(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def parse(self):
        pass
