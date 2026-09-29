"""Tests for the main parts of the password generator project."""

import sys
from pathlib import Path
import unittest

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from password_generator import PasswordGenerator
from password_strength import PasswordStrengthChecker
from validator import InputValidator
from history_manager import SessionHistory


class TestValidator(unittest.TestCase):

    def test_valid_length(self):
        self.assertEqual(InputValidator.validate_length(12), (True, ""))

    def test_invalid_small_length(self):
        valid, _ = InputValidator.validate_length(3)
        self.assertFalse(valid)

    def test_invalid_large_length(self):
        valid, _ = InputValidator.validate_length(129)
        self.assertFalse(valid)

    def test_categories(self):
        valid, _ = InputValidator.validate_categories(
            {"uppercase": False, "lowercase": False,
             "digits": True, "symbols": False}
        )
        self.assertTrue(valid)


class TestPasswordGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = PasswordGenerator()

    def test_length(self):
        password = self.generator.generate(20)
        self.assertEqual(len(password), 20)

    def test_selected_digits_only(self):
        password = self.generator.generate(
            12, False, False, True, False
        )
        self.assertTrue(password.isdigit())

    def test_selected_lowercase_only(self):
        password = self.generator.generate(
            12, False, True, False, False
        )
        self.assertTrue(password.islower())


class TestStrengthChecker(unittest.TestCase):

    def setUp(self):
        self.checker = PasswordStrengthChecker()

    def test_strong_password(self):
        report = self.checker.check("Abcdef12!XYZ")
        self.assertEqual(report["strength"], "Strong")

    def test_weak_password(self):
        report = self.checker.check("abc")
        self.assertEqual(report["strength"], "Weak")


class TestHistory(unittest.TestCase):

    def test_session_history(self):
        history = SessionHistory()
        history.add("Example123!", "Strong")
        self.assertEqual(len(history.get_records()), 1)
        self.assertEqual(history.get_records()[0]["strength"], "Strong")


if __name__ == "__main__":
    unittest.main()
