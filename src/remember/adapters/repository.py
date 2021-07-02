import os

from core.ports import file_repository
from domain import model


class FileRepository(file_repository.AbstractFileRepository):
    def __init__(self, manager):
        super().__init__(manager)

    def store(self, card: model.Flashcard):
        self.manager.write(str(card).encode("utf-8"))

    def update(self, id, payload):
        self.manager(id, "w")
        self.manager.write(payload)

    def destroy(self, id):
        os.remove(id)
