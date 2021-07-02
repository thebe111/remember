import tempfile

import config
from adapters import repository
from core.ports import file_unit_of_work


class FileUnitOfWork(file_unit_of_work.FileUnitOfWork):
    def __enter__(self):
        self.manager = tempfile.NamedTemporaryFile(dir=f"{config.STORAGE_PATH}")
        self.file = repository.FileRepository(self.manager)

        return super().__enter__()
