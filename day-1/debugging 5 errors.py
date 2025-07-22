from io import StringIO
import sys
from unittest import TestCase
class Evaluate(TestCase):
    def test_debuggimg(self):
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout to capture print statements
        import main #Imports and run student solution
        sys.stdout = sys.__stdout__  # Reset redirect.
        output = captured_output.getvalue()  # Get the printed output
        self.assertIn("Notes from Day 1\nThe print statement is used to output strings\nStrings are strings of characters\nString Concatenation is done with the + sign\nNew lines can be created with a \\ and the letter n\n", output, "Make sure you are printing out all 5 lines.")
