"""Caja decorator for sequential structures (lists et al)"""

from collections.abc import MutableSequence
from .CajaSequence import CajaSequence

CajaBase = CajaSequence
CajaAggregatedTrait = MutableSequence
CajaMeta = type('Meta', (type(CajaBase), type(CajaAggregatedTrait)), {})


class CajaMutableSequence(CajaBase, CajaAggregatedTrait, metaclass=CajaMeta):
    """Caja decorator for sequential structures (lists et al)"""

    @classmethod
    def _default_content(cls):
        return list()

    # abc interface

    def __setitem__(self, key, value) -> None:
        self._assign_item(key, value)

    def __delitem__(self, key) -> None:
        self._del_item(key)

    def insert(self, index, value) -> None:
        self._content_.insert(index, value)
