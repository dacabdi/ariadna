"""Caja decorator for map structures (immutable)"""

from collections.abc import Mapping, Hashable
from frozendict import frozendict
from .Caja import Caja

CajaBase = Caja
CajaAggregatedTrait = Mapping
CajaMeta = type('Meta', (type(CajaBase), type(CajaAggregatedTrait)), {})


class CajaMapping(CajaBase, CajaAggregatedTrait, metaclass=CajaMeta):
    """Caja decorator for map structures (immutable)"""

    @classmethod
    def _default_content(cls) -> Mapping:
        return frozendict()

    @CajaBase.content.getter
    def content(self) -> Mapping:
        return type(self._content_)({
            key.content
                if isinstance(key, Caja)
                else key: value.content
                    if isinstance(value, Caja)
                    else value
            for key, value in self._content_.items()
        })

    def _split_key(self, key: Hashable) -> tuple:
        if isinstance(key, str):
            return self.path_splitter(key)
        return key, None

    def values(self):
        return self._content_.values()
