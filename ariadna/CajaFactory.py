"""Factory pattern for Caja objects using CajaFactory metaclass."""

import inspect
import importlib
import collections.abc
from operator import itemgetter


class CajaFactory(type):
    """CajaFactory creates specific types of Cajas depending on decorated collection type."""

    traits_cache = {}
    exceptions = frozenset([str, range])

    def __call__(cls, content=None, *args, **kwds):  # pylint: disable=keyword-arg-before-vararg
        """Return Caja instance type according to content object type."""
        from .Caja import Caja  # pylint: disable=import-outside-toplevel
        if cls is Caja:
            return CajaFactory.wrapper_type(content)(content, *args, **kwds)
        return type.__call__(cls, content, *args, **kwds)

    @staticmethod
    def import_cajas() -> frozenset:
        """Import all Caja types from 'Ariadna' module.
        This will allow dynamically matching traits of the
        decorated type to find the fitting Caja type"""
        mod = importlib.import_module('Ariadna')
        return frozenset([getattr(mod, name) for name in mod.__cajas__])

    @staticmethod
    def import_default_caja() -> frozenset:
        """Import default Caja type for 'None' type content from 'Ariadna' module"""
        mod = importlib.import_module('Ariadna')
        return mod.DefaultNoneCaja

    @staticmethod
    def trait_filters(klass) -> frozenset:
        """Produce a list of ABC collection types from which the class is a subclass"""
        k = CajaFactory
        if klass not in k.traits_cache.keys():
            def tfilter(member):
                return inspect.isclass(member) \
                    and issubclass(member, collections.abc.Collection) \
                    and issubclass(klass, member)
            k.traits_cache[klass] = \
                frozenset(map(itemgetter(1), inspect.getmembers(
                    collections.abc, tfilter)))
        return k.traits_cache[klass]

    @staticmethod
    def trait_match(traits1, traits2) -> bool:
        """Return true if both lists (traits1 and traits2) of ABC collection types match"""
        return traits1 == traits2

    @staticmethod
    def wrapper_type(content):
        """Return the Caja type that implements the same traits as the wrapped collection object"""
        k = CajaFactory
        if type(content) not in k.exceptions:  # pylint: disable=unidiomatic-typecheck
            if content is None:
                return k.import_default_caja()
            caja_classes = k.import_cajas()
            content_traits = k.trait_filters(type(content))
            for caja_class in caja_classes:
                if k.trait_match(k.trait_filters(caja_class), content_traits):
                    return caja_class
        raise TypeError(
            f'CajaFactory does not know how to decorate content type {type(content)}')
