import sys
from functools import wraps
from typing import Callable

_EXCEPTIONS = {
    "StoreError": lambda t: f"{t}: Error to store flashcard",
    "UnknownError": lambda _: "RememberDefaultException: Unknown Error",
}


def exceptions_handler(func) -> Callable:
    @wraps(func)
    def wrapper(_type, *args):
        msg = func(_type, *args)

        return sys.exit(msg)

    return wrapper


@exceptions_handler
def exceptions_resolver(_type, *args) -> str:
    if str(_type) in _EXCEPTIONS:
        action = _EXCEPTIONS[str(_type)]
    else:
        action = _EXCEPTIONS["UnknownError"]

    return action(_type, *args)
