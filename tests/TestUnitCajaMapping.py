import unittest
import traceback
from frozendict import frozendict
from Ariadna import Caja,       \
    CajaMapping \



class TestUnitCajaMapping(unittest.TestCase):

    def test_unit_caja_mapping(self):
        test_contents = [frozendict({'key1': 'test', 1: '1', TypeError: 'SomeException'})]
        for test_content in test_contents:
            try:
                mapping = CajaMapping(test_content)
            except TypeError as e:
                self.fail(msg=f'Failed with {e} {traceback.format_exc()}')
            msg = f'Testing mapping with test_content {test_content}'
            with self.subTest(msg=msg, mapping=mapping, test_content=test_content):
                self.assertEqual(len(mapping), len(test_content))  # same length
                self.assertEqual(mapping.content, test_content)  # compare mappings
                for key in test_content:
                    msg = f'key {key} exists both in test_content and Caja, with same value'
                    with self.subTest(msg=msg, key=key):
                        self.assertTrue(key in mapping)
                        self.assertTrue(mapping[key], test_content[key])

    def test_unit_caja_mapping_nested(self):
        test_content = frozendict({'a': 'value_a', 'b': 'value_b', 'c':
                                   {'under_d': 'value_under_d', 'under_e': [1, 2, frozendict({'z': 'z_value'})]}})
        path_value = {
            'a': 'value_a',
            'b': 'value_b',
            'c': frozendict({'under_d': 'value_under_d', 'under_e': [1, 2, frozendict({'z': 'z_value'})]}),
            'c.under_d': 'value_under_d',
            'c.under_e': [1, 2, frozendict({'z': 'z_value'})],
            'c.under_e.2.z': 'z_value',
            'c.under_e.::-1.0.z': 'z_value'
        }
        mapping = CajaMapping(test_content)
        for wrong_path in ['a.d', 'c.n', '1.a', 'c.under_e.2.x']:
            with self.assertRaises(LookupError):
                _ = mapping[wrong_path]
        for path, value in path_value.items():
            msg = f'Key {path} should return {value}'
            with self.subTest(msg=msg, path=path, value=value):
                self.assertEqual(mapping[path], value)
                self.assertEqual(mapping.get(path), value)
