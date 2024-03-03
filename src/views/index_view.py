import os
from .interface import View_Interface

class Index_View(View_Interface):
    
    def screen(self) -> str|None:
        os.system('cls||clear')
        print('Hello world\n')

        return 'exit'
    
    def refresh(self) -> View_Interface:
        return Index_View()
