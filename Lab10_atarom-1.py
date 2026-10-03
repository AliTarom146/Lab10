"""
Program: Word Analyzer
Author: Ali Tarom
Purpose: This program reads a text file and counts the frequency
of each word using object-oriented programming.
Starter Code: No starter code was used.
Date: October 2, 2026
"""

import pathlib
import string


class WordAnalyzer:
    """Analyze a text file and count the frequency of each word."""

    def __init__(self, filepath):
        """Initialize the WordAnalyzer with a file path."""
        self.__filepath = pathlib.Path(filepath)
        self.__frequencies = {}