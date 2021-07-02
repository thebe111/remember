import abc
from typing import Dict, List

from core import domain


class AbstractCommandHandler(abc.ABC):
    @abc.abstractmethod
    def store(self, aggregate: domain.Aggregate) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, id: str, payload: Dict[str, object]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def destroy(self, id: str) -> None:
        raise NotImplementedError


class AbstractQueryHandler(abc.ABC):
    @abc.abstractmethod
    def index(self) -> List[domain.Aggregate]:
        raise NotImplementedError

    @abc.abstractmethod
    def show(self, id: str) -> domain.Aggregate:
        raise NotImplementedError
