"""Caja decorator for mutable sets"""

from collections.abc import MutableSet
from .CajaSet import CajaSet

CajaBase = CajaSet
CajaAggregatedTrait = MutableSet
CajaMeta = type('Meta', (type(CajaBase), type(CajaAggregatedTrait)), {})


class CajaMutableSet(CajaBase, CajaAggregatedTrait, metaclass=CajaMeta):
    """Caja decorator for mutable sets"""

    @classmethod
    def _default_content(cls):
        return set()

    # abc interface

    def add(self, value):
        raise self._content_.add(value)

    def discard(self, value):
        raise self._content_.add(value)
