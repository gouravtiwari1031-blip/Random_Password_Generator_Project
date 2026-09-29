"""Keep a small password history for the current program session.

Nothing in this module is written to disk. The history disappears when
the application closes.
"""

from datetime import datetime


class SessionHistory:
    """Store generated passwords temporarily while the program is running."""

    def __init__(self):
        self._records = []

    def add(self, password, strength):
        """Add one generated password to the current session."""
        self._records.append({
            "password": password,
            "strength": strength,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    def get_records(self):
        """Return the session records without exposing the internal list."""
        return list(self._records)

    def display(self):
        """Print the passwords generated during this session."""
        if not self._records:
            print("\nNo password history in this session.")
            return

        print("\n========== SESSION HISTORY ==========")
        for number, record in enumerate(self._records, start=1):
            print(f"\nPassword {number}")
            print(f"Password : {record['password']}")
            print(f"Strength : {record['strength']}")
            print(f"Time     : {record['time']}")
        print("\nNote: history is memory-only and disappears when the program closes.")
        print("=====================================")
