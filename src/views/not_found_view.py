import os
from .interface import View_Interface

class Not_Found_View(View_Interface):
    
    def screen(self) -> str|None:
        os.system('cls||clear')
        print('Caminho não foi encontrado\n')
        
        return 'exit'
    
    def refresh(self) -> View_Interface:
        return Not_Found_View()
