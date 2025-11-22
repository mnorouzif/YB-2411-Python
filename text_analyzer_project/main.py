"""
main.py
Demonstrates usage of the TextAnalyzer class.
"""

from analyzer import TextAnalyzer


class TextAnalyzerRunner:
    """Handles execution and display of TextAnalyzer results."""

    @staticmethod
    def run():
        """Main runner method to demonstrate TextAnalyzer."""
        # Example data
        example_data = ["Hello World", "Python IS Fun"]

        # Create analyzer instance
        analyzer = TextAnalyzer(example_data)
        results = analyzer.summar
        # Display results
        print("=== Text Analyzer Results ===")
        print(f"Total Length: {results['total_length']}")
        print(f"Uppercase Letters: {results['uppercase_count']}")


if __name__ == "__main__":
    TextAnalyzerRunner.run()
