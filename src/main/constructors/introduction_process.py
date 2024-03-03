from src.views import (
    index_view, 
    not_found_view, 
    exit_view
)

def introduction():
    index_input = index_view.screen()
    
    if index_input == 'exit':
        exit_view.screen()
    
    else:
        not_found_view.screen()
