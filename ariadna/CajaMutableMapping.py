"""Caja decorator for mutable mapping structures"""

from collections.abc import MutableMapping, Hashable
from .CajaMapping import CajaMapping

CajaBase = CajaMapping
CajaAggregatedTrait = MutableMapping
CajaMeta = type('Meta', (type(CajaBase), type(CajaAggregatedTrait)), {})


class CajaMutableMapping(CajaBase, CajaAggregatedTrait, metaclass=CajaMeta):
    """Caja decorator for mutable mapping structures"""

    @classmethod
    def _default_content(cls) -> MutableMapping:
        return dict()

    # abc interface

    def __setitem__(self, key: Hashable, value) -> None:
        self._assign_item(key, value)

    def __delitem__(self, key: Hashable) -> None:
        self._del_item(key)
