import json
from datetime import date
from typing import Any, Set

from core import domain


class Flashcard(domain.ValueObject):
    front: str
    back: str
    counter: int = 0
    cycle_date: date = date.today()
    tags: Set = set()

    def __init__(
        self,
        front: str,
        back: str,
        tags: Set = set(),
        counter: int = 0,
        cycle_date: date = date.today(),
    ):
        self.front = front
        self.back = back
        self.counter = counter
        self.cycle_date: date
        self.tags = tags

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, Flashcard)
            and self.front == other.front
            and self.back == other.back
        )

    def __hash__(self) -> int:
        return hash(self.ref)

    def __str__(self) -> str:
        payload = json.dumps(
            {
                "front": self.front,
                "back": self.back,
                "counter": self.counter,
                "cycle_date": str(self.cycle_date),
                "tags": list(self.tags),
            }
        )

        return payload

    def rollback(self) -> None:
        self.counter = 0
        self.cycle_date = tomorrow
