from src.views.interface import View_Interface
from .constructors import (
    introduction,
)

routes: dict[str, callable] = {
    "i": introduction,
}
