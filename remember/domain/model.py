from dataclasses import dataclass
from datetime import date
from typing import Any


class FlashCard:
    ref: str
    front: str
    back: str
    counter: int
    cycle_date: date

    def __init__(self, ref: str, front: str, back: str, counter: int, cycle_date: date):
        self.ref = ref
        self.front = front
        self.back = back
        self.counter = counter
        self.cycle_date: date

    def __eq__(self, other: Any) -> bool:
        return self.ref == other.ref

    def __hash__(self) -> int:
        return hash(self.ref)

    def rollback(self) -> None:
        self.counter = 0
        self.cycle_date = tomorrow
