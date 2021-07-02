from typing import Callable, Dict

from core import domain, repository


class AbstractFileRepository(repository.AbstractRepository):
    def __init__(self, manager: Callable):
        self.manager = manager

    def store(self, aggregate: domain.Aggregate) -> None:
        raise NotImplementedError

    def update(self, id: str, payload: Dict[str, object]) -> None:
        raise NotImplementedError

    def destroy(self, id: str) -> None:
        raise NotImplementedError
