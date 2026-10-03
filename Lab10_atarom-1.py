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