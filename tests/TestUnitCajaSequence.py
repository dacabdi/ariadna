import unittest
import traceback
from frozendict import frozendict
from Ariadna import Caja,       \
    CajaSequence\



class TestUnitCajaSequence(unittest.TestCase):

    def test_unit_caja_sequence(self):
        test_contents = [tuple(('a', 1, 5.4, TypeError))]
        for test_content in test_contents:
            try:
                sequence = CajaSequence(test_content)
            except TypeError as e:
                self.fail(msg=f'Failed with {e} {traceback.format_exc()}')
            msg = f'Testing sequence with test_content {test_content}'
            with self.subTest(msg=msg, sequence=sequence, test_content=test_content):
                self.assertEqual(len(sequence), len(test_content))  # same length
                self.assertEqual(sequence.content, test_content)  # compare sequences
                self.assertEqual(sequence[::-1], test_content[::-1])  # compared reverse/sliced
                for item in test_content:
                    msg = f'Item {item} exists both in test_content and Caja, with same count'
                    with self.subTest(msg=msg, item=item):
                        self.assertTrue(item in sequence)
                        self.assertEqual(sequence.count(item), test_content.count(item))
                        self.assertEqual(sequence.index(item), test_content.index(item))
                for idx in range(len(test_content)):
                    with self.subTest(idx=idx):
                        self.assertEqual(sequence[idx], test_content[idx])

    def test_unit_caja_sequence_nested(self):
        test_content = ((1, 2, 3), (6, 7, (8, 9, 10, (11, 12))))
        path_value = {
            '0': (1, 2, 3),
            '0.0': 1,
            '0.1': 2,
            '0.2': 3,
            '1': (6, 7, (8, 9, 10, (11, 12))),
            '1.0': 6,
            '1.1': 7,
            '1.2': (8, 9, 10, (11, 12)),
            '1.2.0': 8,
            '1.2.1': 9,
            '1.2.2': 10,
            '1.2.3': (11, 12),
            '1.2.3.0': 11,
            '1.2.3.1': 12
        }
        sequence = CajaSequence(test_content)
        # some slices
        self.assertEqual(sequence['1.::-1'].content, ((6, 7, (8, 9, 10, (11, 12))))[::-1])
        for wrong_path in ['9', '1.2.3.1.2', '1.a']:
            with self.assertRaises(LookupError):
                _ = sequence[wrong_path]
        for path, value in path_value.items():
            msg = f'Key {path} should return {value}'
            with self.subTest(msg=msg, path=path, value=value):
                self.assertEqual(sequence[path], value)
