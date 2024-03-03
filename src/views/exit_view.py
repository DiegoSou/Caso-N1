from .interface import View_Interface

class Exit_View(View_Interface):
    
    def screen(self) -> str|None:
        print('Encerrando o programa.\n\n')
        
        return None
    
    def refresh(self) -> View_Interface:
        return Exit_View()
