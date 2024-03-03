""" can't make an instance using this class or call its methods without implementation """
from abc import ABC

class View_Interface(ABC):
    """ Represents a contract of view 

        Views are the most simple layer, it just shows a screen and pass 
        user input informations to controllers
    """

    def screen(self) -> str|None:
        pass
    
    def refresh(self) -> View_Interface:
        pass
