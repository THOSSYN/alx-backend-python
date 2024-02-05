#!/usr/bin/env python3
"""Unit testing execise"""

import unittest
from utils import *
import requests
from parameterized import parameterized
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """A test class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test if a result returns as it ought to"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test if KeyError is raised"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class for get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, expected, mocked_request):
        expected_response = expected
        mocked_response = MagicMock()
        mocked_response.json.return_value = expected_response
        mocked_request.return_value = mocked_response

        result = get_json(url)

        self.assertEqual(result, expected_response)
        mocked_request.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Test memoize function behavior"""
    def test_memoize(self):
        """A method that test memoize function behavior"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', spec=True) as mock_method:
            mock_method.return_value = 42

            instance = TestClass()
            result1 = instance.a_property
            result2 = instance.a_property

            mock_method.assert_called_once()

            self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()
