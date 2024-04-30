#!/usr/bin/env python3
"""test_utils module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test_access_nested_map method
        Args:
            nested_map: dict
            path: tuple
            expected: any
        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    """If run as main module"""
    unittest.main()
