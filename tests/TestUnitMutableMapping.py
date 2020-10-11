import unittest
import traceback
from frozendict import frozendict
from Ariadna import Caja,               \
    CajaMutableMapping  \



class TestUnitCajaMutableMapping(unittest.TestCase):

    def test_unit_caja_mutable_mapping_non_mutating(self):
        test_contents = [{'key1': 'test', 1: '1', TypeError: 'SomeException'}]
        for test_content in test_contents:
            try:
                mapping = CajaMutableMapping(test_content)
            except TypeError as e:
                self.fail(msg=f'Failed with {e} {traceback.format_exc()}')
            msg = f'Testing mutable mapping with test_content {test_content}'
            with self.subTest(msg=msg, mapping=mapping, test_content=test_content):
                self.assertEqual(len(mapping), len(test_content))  # same length
                self.assertEqual(mapping.content, test_content)  # compare mappings
                self.assertEqual(mapping.keys(), test_content.keys())
                self.assertEqual(str(mapping.values()), str(test_content.values()))
                self.assertEqual(mapping.items(), test_content.items())

    def test_unit_caja_mutable_mapping_mutating(self):
        test_content = {
            'strkey': 'strvalue',
            'somecollection': {},
            1: '1',
            TypeError: 'TypeError',
            frozendict({'content': 'content_value'}): 'complexkey',
            ('a', 'b'): 'ab->c'
        }

        mapping = CajaMutableMapping(test_content)

        self.assertEqual(mapping['strkey'], test_content['strkey'])
        try:
            mapping['strkey'] = 'anothervalue'
        except Exception as e:
            self.fail(msg=f'Failed with {e} {traceback.format_exc()}')
        self.assertEqual(mapping['strkey'], 'anothervalue')

        # set key that does not exist
        try:
            mapping['newkey.undernewkey.undernewnew_key'] = 'supernestedvalue'
        except Exception as e:
            self.fail(msg=f'Failed with {e} {traceback.format_exc()}')
        self.assertEqual(mapping['newkey.undernewkey.undernewnew_key'], 'supernestedvalue')

        # attempt to nest new key under existing path up to collection
        try:
            mapping['somecollection.undernewkey.undernewnew_key'] = 'supernestedvalue'
        except Exception as e:
            self.fail(msg=f'Failed with {e} {traceback.format_exc()}')
        self.assertEqual(mapping['somecollection.undernewkey.undernewnew_key'], 'supernestedvalue')

        # attempt to nest new key under existing path with non subscriptable leaf
        with self.assertRaises(Exception):
            mapping['strkey.undernewkey'] = 'supernestedvalue'

        # delete a value
        try:
            del mapping[1]
        except Exception as e:
            self.fail(msg=f'Failed with {e} {traceback.format_exc()}')
        with self.assertRaises(LookupError):
            _ = mapping[1]

    def test_unit_caja_mutable_mapping_nested_non_mutating(self):
        test_content = {'a': 'value_a', 'b': 'value_b', 'c':
                        {'under_d': 'value_under_d', 'under_e': [1, 2, frozendict({'z': 'z_value'})]}}
        path_value = {
            'a': 'value_a',
            'b': 'value_b',
            'c': frozendict({'under_d': 'value_under_d', 'under_e': [1, 2, frozendict({'z': 'z_value'})]}),
            'c.under_d': 'value_under_d',
            'c.under_e': [1, 2, frozendict({'z': 'z_value'})],
            'c.under_e.2.z': 'z_value',
            'c.under_e.::-1.0.z': 'z_value'
        }
        mapping = CajaMutableMapping(test_content)
        for wrong_path in ['a.d', 'c.n', '1.a', 'c.under_e.2.x']:
            with self.assertRaises(LookupError):
                _ = mapping[wrong_path]
        for path, value in path_value.items():
            msg = f'Key {path} should return {value}'
            with self.subTest(msg=msg, path=path, value=value):
                self.assertEqual(mapping[path], value)
                self.assertEqual(mapping.get(path), value)
