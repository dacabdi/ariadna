"""Library of maps and collections that support full paths as keys"""

from .PathSplitter import PathSplitter
from .PathSplitter import RegexSplitter

from .Caja import Caja
from .CajaMapping import CajaMapping
from .CajaMutableMapping import CajaMutableMapping
from .CajaMutableSequence import CajaMutableSequence
from .CajaMutableSet import CajaMutableSet
from .CajaSequence import CajaSequence
from .CajaSet import CajaSet

DefaultPathSplitter = RegexSplitter
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

__all__ = __cajas__ + ['PathSplitter', 'RegexSplitter']
