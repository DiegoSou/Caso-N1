from .constructors import (
    introduction,
)

routes: dict[str, callable] = {
    "i": introduction,
}
