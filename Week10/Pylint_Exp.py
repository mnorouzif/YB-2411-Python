"""
Object-Oriented project to analyze text inputs.
Performs:
1. Calculates total length.
2. Determines number of uppercase characters.
"""

from typing import Union


class TextAnalyzer:
    """A class to analyze text data (string or list)."""

    def __init__(self, data: Union[str, list]) -> None:
        """
        Initialize the analyzer with a string or list.

        Args:
            data (Union[str, list]): Input text or list of characters/words.
        """
        if not isinstance(data, (str, list)):
            raise TypeError("Input must be a string or a list.")
        self.data = data

    def get_length(self) -> int:
        """
        Calculate the total length of the input.

        Returns:
            int: Length of the input data.
        """
        return len(self.data)

    def count_uppercase(self) -> int:
        """
        Count the number of uppercase characters in the input.

        Returns:
            int: Number of uppercase characters.
        """
        if isinstance(self.data, str):
            return sum(1 for char in self.data if char.isupper())
        return sum(1 for item in self.data if isinstance(item, str) and item.isupper())


if __name__ == "__main__":
    string_input = TextAnalyzer("We have a Guest Lecturer Today!")
    print("String input length:", string_input.get_length())
    print("Uppercase letters:", string_input.count_uppercase())

    list_input = TextAnalyzer(["Hello", "WORLD", "abc", "XYZ"])
    print("List input length:", list_input.get_length())
    print("Uppercase items:", list_input.count_uppercase())
