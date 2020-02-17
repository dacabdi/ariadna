import unittest
import traceback
from frozendict import frozendict
from ariadna import Caja,                   \
                    CajaMapping,            \
                    CajaMutableMapping,     \
                    CajaMutableSequence,    \
                    CajaMutableSet,         \
                    CajaSequence,           \
                    CajaSet                 \

class TestUnitCajaTyping(unittest.TestCase):

    def setUp(self):
        self.types = {
            CajaMapping : [frozendict(), frozendict({'key':'string_val','nested':{'list':[1,2,3]}})],
            CajaMutableMapping : [None, dict(), dict({'key':'str','nested':{'list':[1.2, 1.5]}})],
            CajaMutableSequence : [list(), [1,2,3]],
            CajaMutableSet : [set(), set([1,2,3])],
            CajaSequence : [tuple(('a', 1, 5.4, TypeError))],
            CajaSet : [frozenset(), frozenset([1,2,3])]
        }
        self.non_container = (
            1,
            range(1),
            str(),
            'some string',
            lambda: None,
            TypeError()
        )

    def test_unit_caja_factory_types_positive(self):
        for caja_type, wrapped_instances in self.types.items():
            for wrapped_instance in wrapped_instances:
                msg = f'CajaFactory wrapping {type(wrapped_instance)} should produce {caja_type}'
                with self.subTest(msg=msg, wrapped_instance=wrapped_instance, caja_type=caja_type):
                    try:
                        caja_instance = Caja(wrapped_instance)
                    except TypeError as e:
                        self.fail(msg=f'Failed with {e} {traceback.format_exc()}')
                    self.assertIsInstance(caja_instance, Caja)
                    self.assertIsInstance(caja_instance, caja_type)
                    if wrapped_instance is not None:
                        self.assertIsInstance(caja_instance._content_, type(wrapped_instance))
                        self.assertEqual(caja_instance._content_, wrapped_instance)

    def test_unit_caja_factory_types_negative(self):
        for instance in self.non_container:
            with self.subTest(instance=instance):
                with self.assertRaises(TypeError):
                    _ = Caja(instance)

    def test_unit_caja_types_positive(self):
        for caja_type, wrapped_instances in self.types.items():
            for wrapped_instance in wrapped_instances + [None]:
                msg = f'{caja_type} accepts {type(wrapped_instance)}'
                with self.subTest(msg=msg, wrapped_instance=wrapped_instance, caja_type=caja_type):
                    try:
                        caja_instance = caja_type(wrapped_instance)
                    except TypeError as e:
                        self.fail(msg=f'Failed with {e} {traceback.format_exc()}')
                    # extra verifications
                    self.assertIsInstance(caja_instance, caja_type)
                    self.assertIsInstance(caja_instance, Caja)
                    if wrapped_instance is not None:
                        self.assertIsInstance(caja_instance._content_, type(wrapped_instance))
                        self.assertEqual(caja_instance._content_, wrapped_instance)

    def test_unit_caja_types_negative_collections(self):
        caja_types = self.types.keys()
        for caja_type in caja_types:
            for wrapped_instance_list in [self.types[ct] for ct in (self.types.keys() - [caja_type])]:
                for wrapped_instance in wrapped_instance_list:
                    msg = f'{caja_type} should not wrap type {type(wrapped_instance)}'
                    with self.subTest(msg=msg, caja_type=caja_type, wrapped_instance=wrapped_instance):
                        if wrapped_instance is not None:
                             with self.assertRaises(TypeError):
                                _ = caja_type(wrapped_instance)
    
    def test_unit_caja_types_negative_non_container(self):
        for caja_type in self.types.keys():
            for wrapped_instance in self.non_container:
                msg = f'{caja_type} should not wrap non container type {type(wrapped_instance)}'
                with self.subTest(msg=msg, caja_type=caja_type, wrapped_instance=wrapped_instance):
                    with self.assertRaises(TypeError):
                        _ = caja_type(wrapped_instance)