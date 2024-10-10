from src.shared.repository_interface import IRepository
from src.shared.unit_of_work_interface import IUnitOfWork


class InMemoryUow(IUnitOfWork):
    def __init__(self, repository: IRepository):
        self.repository = repository
        self._committed = False

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def commit(self):
        self._committed = True

    def rollback(self):
        pass
