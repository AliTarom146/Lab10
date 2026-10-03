"""
Program: Word Analyzer
Author: Ali Tarom
Purpose: This program reads a text file and counts the frequency
of each word using object-oriented programming.
Starter Code: No starter code was used.
Date: October, 2026
"""

import pathlib
import string


class WordAnalyzer:
    """Analyze a text file and count the frequency of each word."""

    def __init__(self, filepath):
        """Initialize the WordAnalyzer with a file path."""
        self.__filepath = pathlib.Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        """Read the file and count the frequency of each word."""
        if not self.__filepath.exists():
            print(f"File not found: {self.__filepath}")
            return False

        try:
            translation_table = str.maketrans(
                "", "", string.punctuation
            )

            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.translate(translation_table)
                    line = line.lower()
                    words = line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print(f"File not found: {self.__filepath}")
            return False

    def print_report(self):
        """Print the word frequencies in alphabetical order."""
        sorted_words = sorted(self.__frequencies.keys())

        for word in sorted_words:
            print(f"{word:<10} :: {self.__frequencies[word]}")


def main():
    """Run the Word Analyzer menu."""
    files = {
        "1": ("Princess Mars", pathlib.Path("princess_mars.txt")),
        "2": ("Tarzan", pathlib.Path("Tarzan.txt")),
        "3": ("Treasure Island", pathlib.Path("treasure_island.txt")),
        "4": ("Monte Cristo", pathlib.Path("monte_cristo.txt")),
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for number, (name, filepath) in files.items():
            print(f"{number}. {name}")

        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nGoodbye!")
            break

        if choice not in files:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu...")
            continue

        name, filepath = files[choice]

        print(f"\nProcessing '{filepath}'...")

        analyzer = WordAnalyzer(filepath)

        if analyzer.process_file():
            analyzer.print_report()

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()