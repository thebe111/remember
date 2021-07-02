import abc
from typing import Any


class AbstractUnitOfWork(abc.ABC):
    def __enter__(self) -> Any:
        return self

    def __exit__(self, *args: Any) -> None:
        self.rollback()

    @abc.abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError
