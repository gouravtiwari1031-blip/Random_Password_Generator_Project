"""Password generation helpers used by the command-line app."""

import secrets
import string


class PasswordGenerator:
    """Build random passwords from the character types the user selects."""

    def __init__(self):
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.digits = string.digits
        self.symbols = string.punctuation

    def generate(self, length, use_uppercase=True, use_lowercase=True,
                 use_digits=True, use_symbols=True):
        """Create a password using the requested character groups."""
        pools = []

        if use_uppercase:
            pools.append(self.uppercase)
        if use_lowercase:
            pools.append(self.lowercase)
        if use_digits:
            pools.append(self.digits)
        if use_symbols:
            pools.append(self.symbols)

        if not pools:
            raise ValueError("At least one character category must be selected.")

        if length < 4:
            raise ValueError("Password length must be at least 4.")

        # Start with one character from each selected group so that every
        # option chosen by the user is actually represented.
        password_chars = [secrets.choice(pool) for pool in pools]
        all_characters = "".join(pools)

        while len(password_chars) < length:
            password_chars.append(secrets.choice(all_characters))

        # Shuffle the characters so the required characters are not always
        # placed at the beginning of the password.
        shuffled = []
        remaining = password_chars[:]
        while remaining:
            index = secrets.randbelow(len(remaining))
            shuffled.append(remaining.pop(index))

        return "".join(shuffled)
