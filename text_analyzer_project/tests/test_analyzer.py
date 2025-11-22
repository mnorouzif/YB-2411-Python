"""
Simple unit tests for TextAnalyzer.
Run with: python -m unittest tests/test_analyzer.py
"""

import unittest
from analyzer import TextAnalyzer


class TestTextAnalyzer(unittest.TestCase):
    """Unit tests for TextAnalyzer class."""

    def test_total_length_string(self):
        analyzer = TextAnalyzer("Hello")
        self.assertEqual(analyzer.total_length(), 5)

    def test_uppercase_count_list(self):
        analyzer = TextAnalyzer(["Hi", "World"])
        self.assertEqual(analyzer.uppercase_count(), 2)


if __name__ == "__main__":
    unittest.main()
