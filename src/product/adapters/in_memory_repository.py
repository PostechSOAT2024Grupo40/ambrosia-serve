from typing import List, Dict

from src.shared.dtos.repository_params_dto import RepositoryParamsDTO
from src.shared.repository_interface import IRepository


class InMemoryRepository(IRepository):
    def __init__(self):
        self.data = {}

    def get_all(self, table_name: str):
        return self.data.get(table_name, [])

    def filter_by(self, table_name: str, params: List[RepositoryParamsDTO]):
        records = self.get_all(table_name)
        for param in params:
            records = [r for r in records if self._matches(r, param)]
        return records

    def insert_update(self, table_name: str, params: List[RepositoryParamsDTO]):
        if table_name not in self.data:
            self.data[table_name] = []
        else:
            records = self.filter_by(table_name, params)
            if records:
                records = records[0]
                for param in params:
                    records[param.key] = param.value
                return records

        record = {param.key: param.value for param in params}
        self.data[table_name].append(record)
        return record

    def delete(self, table_name: str, params: List[RepositoryParamsDTO]):
        self.data[table_name] = [
            r for r in self.get_all(table_name) if not all(self._matches(r, param) for param in params)
        ]

    @staticmethod
    def _matches(record: Dict, param: RepositoryParamsDTO):
        return record.get(param.key) == param.value
