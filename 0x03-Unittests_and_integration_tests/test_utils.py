#!/usr/bin/env python3
""" Parameterize a unit test"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
import utils
from utils import (access_nested_map, get_json, memoize)


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


class TestGetJson(unittest.TestCase):
    """test that utils.get_json returns the expected result"""

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """tests that utils.get_json returns expected results"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests Memoize method"""

    @parameterized.expand([
        (42,),

    ])
    def test_memoize(self, return_value):
        """tests that memoize is called once"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=return_value) as mock_a_method:
            test = TestClass()

            result1 = test.a_property
            result2 = test.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(result1, return_value)
            self.assertEqual(result2, return_value)
