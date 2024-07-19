import unittest
from io import StringIO
import sys

class TestPaintingCalculator(unittest.TestCase):
    def run_program_with_input(self, user_input):
        """Runs the assignment.py program with the given input and returns the output."""
        # Backup the original stdin and stdout
        original_stdin = sys.stdin
        original_stdout = sys.stdout

        # Redirect stdin and stdout
        sys.stdin = StringIO(user_input)
        sys.stdout = StringIO()

        # Run the script
        try:
            from assignment import main  # Import the main function
            main()  # Call the main function
            output = sys.stdout.getvalue()  # Capture the output
        finally:
            # Restore the original stdin and stdout
            sys.stdin = original_stdin
            sys.stdout = original_stdout

        return output.strip()
    
    def test_small_room(self):
        output = self.run_program_with_input("10\n8\n8\n")
        self.assertIn("Total area to be painted: 368.00 square feet", output)
        self.assertIn("Amount of primer needed: 1.84 gallons", output)
        self.assertIn("Amount of paint needed: 1.05 gallons", output)

    def test_large_room(self):
        output = self.run_program_with_input("20\n15\n12\n")
        self.assertIn("Total area to be painted: 1140.00 square feet", output)
        self.assertIn("Amount of primer needed: 5.70 gallons", output)
        self.assertIn("Amount of paint needed: 3.26 gallons", output)

    def test_square_room_with_high_ceiling(self):
        output = self.run_program_with_input("12\n12\n15\n")
        self.assertIn("Total area to be painted: 864.00 square feet", output)
        self.assertIn("Amount of primer needed: 4.32 gallons", output)
        self.assertIn("Amount of paint needed: 2.47 gallons", output)

if __name__ == "__main__":
    unittest.main()