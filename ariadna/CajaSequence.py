"""Caja decorator for immutable sequences"""

from collections.abc import Sequence, Iterator
from .Caja import Caja

CajaBase = Caja
CajaAggregatedTrait = Sequence
CajaMeta = type('Meta', (type(CajaBase), type(CajaAggregatedTrait)), {})


class CajaSequence(CajaBase, CajaAggregatedTrait, metaclass=CajaMeta):
    """Caja decorator for immutable sequences"""

    @classmethod
    def _default_content(cls) -> Sequence:
        return tuple()

    @CajaBase.content.getter
    def content(self) -> Sequence:
        return type(self._content_)([
            item.content() if isinstance(item, Caja) else item
            for item in self._content_
        ])

    def _split_key(self, key) -> tuple:
        right = None
        if isinstance(key, (slice, int)):
            left = key
        else:
            left, right = self.path_splitter(key)
            try:
                left = int(left)
            except ValueError:
                left = self._parse_splice(left)
        return left, right

    def _parse_splice(self, splice_str: str) -> slice:
        parts = splice_str.split(':')
        start = int(parts[0]) if parts[0] else None
        stop = int(parts[1]) if parts[1] else None
        step = int(parts[2]) if len(parts) == 3 and parts[2] else None
        return slice(start, stop, step)

    # mixin methods

    def __reversed__(self) -> Iterator:
        return reversed(self._content_)
