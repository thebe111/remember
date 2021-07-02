import abc
import enum

HELP = """
Usage: remember [options]

Options:
    -s, --store             Store a new flashcard item
    -t, --tag <text>        Learn only flashcards with the given tag

    -h, --help              Show this message and exit
    -v, --version           Show the version and exit
"""


class Aggregate(abc.ABC):
    pass


class Entity(Aggregate):
    pass


class ValueObject(Aggregate):
    pass


class Exit(enum.Enum):
    SUCCESS = 0
    ERROR = 1
