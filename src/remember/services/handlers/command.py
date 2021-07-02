from core import handlers
from domain import exceptions, model


class FlashcardCommandHandler(handlers.AbstractCommandHandler):
    def store(self, uow, card: model.Flashcard):
        with uow:
            try:
                uow.file.store(card)
            except Exception:
                raise exceptions.StoreError()

            uow.commit()

    def update(self, uow, payload):
        ...

    def destroy(self, id):
        ...
