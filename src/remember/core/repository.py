import abc
from typing import Dict

from core import domain


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def store(self, aggregate: domain.Aggregate) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, id: str, payload: Dict[str, object]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def destroy(self, id: str) -> None:
        raise NotImplementedError
