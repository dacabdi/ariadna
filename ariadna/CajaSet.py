"""Caja decorator for immutable sets"""

from collections.abc import Set
from .Caja import Caja

CajaBase = Caja
CajaAggregatedTrait = Set
CajaMeta = type('Meta', (type(CajaBase), type(CajaAggregatedTrait)), {})


class CajaSet(CajaBase, CajaAggregatedTrait, metaclass=CajaMeta):
    """Caja decorator for immutable sets"""

    @classmethod
    def _default_content(cls):
        return frozenset()
