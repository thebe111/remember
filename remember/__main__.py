import sys, getopt

from domain import model, exceptions
from services.handlers import command
from core.domain import Status, HELP

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hs", ["help", "storage"])
    except getopt.GetoptError:
        print(HELP)
        sys.exit(Status.ERROR.value)

    for opt, arg in opts:
        if opt == "-h" or "--help":
            print(HELP)
            sys.exit(Status.SUCCESS.value)
        elif opt == "-s" or "--storage":
            front = input("Type the flashcard front text: ")
            back = input("Type the flashcard back text: ")

            try:
                command.store(uow, front, back)
            except Exception as e:
                ...

if __name__ == "__main__":
    main(sys.argv[1:])

