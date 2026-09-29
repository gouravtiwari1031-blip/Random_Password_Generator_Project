"""Simple password-strength checks for the project."""

import string


class PasswordStrengthChecker:
    """Check a password against a small set of easy-to-understand rules."""

    def check(self, password):
        """Return the checks, score, and suggestions for a password."""
        score = 0
        checks = []
        suggestions = []

        length_ok = len(password) >= 8
        if length_ok:
            score += 1
        else:
            suggestions.append("Use at least 8 characters.")
        checks.append(("Length >= 8", length_ok))

        uppercase_ok = any(c.isupper() for c in password)
        if uppercase_ok:
            score += 1
        else:
            suggestions.append("Add uppercase letters.")
        checks.append(("Uppercase letter", uppercase_ok))

        lowercase_ok = any(c.islower() for c in password)
        if lowercase_ok:
            score += 1
        else:
            suggestions.append("Add lowercase letters.")
        checks.append(("Lowercase letter", lowercase_ok))

        digit_ok = any(c.isdigit() for c in password)
        if digit_ok:
            score += 1
        else:
            suggestions.append("Add numbers.")
        checks.append(("Number", digit_ok))

        symbol_ok = any(c in string.punctuation for c in password)
        if symbol_ok:
            score += 1
        else:
            suggestions.append("Add special symbols.")
        checks.append(("Special symbol", symbol_ok))

        long_ok = len(password) >= 12
        if long_ok:
            score += 1
        else:
            suggestions.append("Use 12 or more characters for better protection.")
        checks.append(("Length >= 12", long_ok))

        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

        return {
            "strength": strength,
            "score": score,
            "max_score": 6,
            "checks": checks,
            "suggestions": suggestions,
        }
