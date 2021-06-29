import abc
import enum

HELP = """
    help message
"""

class Aggregate(abc.ABC):
    ...

class Entity(Aggregate):
    pass


class ValueObject(Aggregate):
    pass


class Status(enum.Enum):
    SUCCESS = 0
    ERROR = 1
