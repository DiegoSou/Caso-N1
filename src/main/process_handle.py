from .router import routes

def start(is_running: bool = True, next_path: str = 'i') -> None:
    
    while is_running:
        if next_path not in routes:
            exit()
        
        next_path = routes[next_path]()
