import getopt
import os
import sys
from collections import namedtuple

import config
from core.domain import HELP, Exit
from core.exceptions import exceptions_resolver as eresolver
from domain import exceptions, model
from services import unit_of_work
from services.handlers import command, query


def _store(*args):
    uow, handler = args

    stop = False

    while stop is False:
        front = input("Type the flashcard front text: ").lower()
        back = input("Type the flashcard back text: ").lower()
        tags = set()

        while True:
            _input = input(
                "Type tags for you card or press enter to continue: "
            ).lower()

            if _input == "":
                break

            tags.add(_input)

        card = model.Flashcard(front, back, tags)

        try:
            handler.command.store(uow, card)
        except exceptions.StoreError as e:
            eresolver(e.__class__.__name__)
        except Exception as e:
            eresolver(e.__class__.__name__)

        response = input("Add another card? [Y/n]: ").lower()

        if response == "n":
            stop = True


def main(argv):
    uow = unit_of_work.FileUnitOfWork()

    Handlers = namedtuple("Handlers", ["command", "query"])
    handler = Handlers(
        command.FlashcardCommandHandler(), query.FlashcardQueryHandler()
    )

    try:
        opts, args = getopt.getopt(argv, "hst", ["help", "store", "tag"])
    except getopt.GetoptError:
        print(HELP)
        sys.exit(Exit.ERROR.value)

    for opt, arg in opts:
        if opt == "-h" or opt == "--help":
            print(HELP)
            sys.exit(Exit.SUCCESS.value)
        elif opt == "-s" or opt == "--store":
            _store(uow, handler)
        elif opt == "-t" or opt == "--tag":
            ...
        else:
            ...


if __name__ == "__main__":
    if not os.path.exists(config.STORAGE_PATH):
        os.mkdir(config.STORAGE_PATH)

    main(sys.argv[1:])
