"""Library of maps and collections that support full paths as keys"""

from .PathSplitter import PathSplitter
from .PathSplitter import RegexPathSplitter
from .PathSplitter import DefaultPathSplitter

from .Caja import Caja
from .CajaSet import CajaSet
from .CajaSequence import CajaSequence
from .CajaMutableSet import CajaMutableSet
from .CajaMutableSequence import CajaMutableSequence
from .CajaMutableMapping import CajaMutableMapping
from .CajaMapping import CajaMapping

DefaultNoneCaja = CajaMutableMapping

__cajas__ = [
    'Caja',
    'CajaMapping',
    'CajaMutableMapping',
    'CajaMutableSequence',
    'CajaMutableSet',
    'CajaSequence',
    'CajaSet'
]

__all__ = __cajas__ + ['PathSplitter', 'RegexPathSplitter']
