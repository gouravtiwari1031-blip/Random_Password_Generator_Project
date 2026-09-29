"""Input checks used by the password generator."""

class InputValidator:
    """Keep user input within the limits expected by the application."""

    MIN_LENGTH = 4
    MAX_LENGTH = 128

    @classmethod
    def validate_length(cls, length):
        """Check whether a requested password length is acceptable."""
        if not isinstance(length, int):
            return False, "Length must be an integer."

        if length < cls.MIN_LENGTH:
            return False, f"Length must be at least {cls.MIN_LENGTH}."

        if length > cls.MAX_LENGTH:
            return False, f"Length cannot exceed {cls.MAX_LENGTH}."

        return True, ""

    @staticmethod
    def parse_yes_no(value):
        """Turn a yes/no response into a Boolean value."""
        normalized = value.strip().lower()

        if normalized in {"y", "yes"}:
            return True

        if normalized in {"n", "no"}:
            return False

        raise ValueError("Please enter yes or no.")

    @staticmethod
    def validate_categories(categories):
        """Make sure the user selected at least one character group."""
        if not any(categories.values()):
            return False, "Select at least one character category."

        return True, ""
