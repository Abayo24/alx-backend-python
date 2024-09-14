#!/usr/bin/env python3
""" Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """unit test for utils.access_nested_map"""
    
    @parameterized.expand([
        ({"a": 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: dict,
                               path: tuple,
                               expected_result: any,
                               ) -> None:
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b",), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: dict,
                                         path: tuple,
                                         exception: Exception,
                                         ) -> None:
        """test access_nested_map function with exception"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
