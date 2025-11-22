"""
analyzer.py
A simple Object-Oriented Text Analyzer module.
Use Pylint to check code quality and enforce best practices.
"""

class TextAnalyzer:
    """A class to analyze text data such as strings or lists of strings."""

    def __init__(self, data):
        """
        Initialize the TextAnalyzer with data.
        :param data: string or list of strings to analyze
        """
        if not isinstance(data, (str, list)):
            raise TypeError("Input must be a string or a list of strings.")
        self.data = data

    def total_length(self):
        """Return total length of the text or list of strings."""
        if isinstance(self.data, str):
            return len(self.data)
        return sum(len(item) for item in self.data)

    def uppercase_count(self):
        """Return the number of uppercase letters in the text."""
        text = self.data if isinstance(self.data, str) else ''.join(self.data)
        return sum(1 for char in text if char.isupper())

    def summary(self):
        """Return a summary dictionary with key stats."""
        return {
            "total_length": self.total_length(),
            "uppercase_count": self.uppercase_count()
        }
