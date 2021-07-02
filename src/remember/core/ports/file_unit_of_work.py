import shutil
import tempfile
import uuid
from typing import Any

import config
from core import unit_of_work


class FileUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.manager = tempfile.TemporaryFile()

    def __exit__(self, *args: Any) -> None:
        super().__exit__(*args)
        self.manager.close()

    def commit(self) -> None:
        self.manager.seek(0)
        shutil.copy(
            self.manager.name, f"{config.STORAGE_PATH}/{str(uuid.uuid4())}"
        )

    def rollback(self) -> None:
        pass
