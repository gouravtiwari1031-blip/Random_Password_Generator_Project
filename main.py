"""Command-line interface for the Random Password Generator."""

from password_generator import PasswordGenerator
from password_strength import PasswordStrengthChecker
from validator import InputValidator
from history_manager import SessionHistory


def get_yes_no(prompt):
    """Ask a yes/no question until the user gives a valid answer."""
    while True:
        try:
            return InputValidator.parse_yes_no(input(prompt))
        except ValueError as error:
            print(f"Error: {error}")


def generate_password_workflow(generator, checker, history):
    """Collect settings, generate a password, check it, and save the result."""
    print("\n========== GENERATE PASSWORD ==========")

    while True:
        try:
            length = int(input("Enter password length (4-128): "))
            valid, message = InputValidator.validate_length(length)
            if valid:
                break
            print(f"Error: {message}")
        except ValueError:
            print("Error: enter a whole number.")

    categories = {
        "uppercase": get_yes_no("Include uppercase letters? (yes/no): "),
        "lowercase": get_yes_no("Include lowercase letters? (yes/no): "),
        "digits": get_yes_no("Include numbers? (yes/no): "),
        "symbols": get_yes_no("Include symbols? (yes/no): "),
    }

    valid, message = InputValidator.validate_categories(categories)
    if not valid:
        print(f"Error: {message}")
        return

    password = generator.generate(
        length,
        categories["uppercase"],
        categories["lowercase"],
        categories["digits"],
        categories["symbols"],
    )

    report = checker.check(password)
    history.add(password, report["strength"])

    print("\n---------- RESULT ----------")
    print(f"Generated password : {password}")
    print(f"Strength           : {report['strength']}")
    print(f"Security score     : {report['score']}/{report['max_score']}")

    if report["suggestions"]:
        print("\nSuggestions:")
        for item in report["suggestions"]:
            print(f"- {item}")
    else:
        print("\nAll strength checks passed.")


def check_password_workflow(checker):
    """Let the user enter a password and see how it performs against the rules."""
    print("\n========== PASSWORD STRENGTH CHECKER ==========")
    password = input("Enter a password to analyze: ")

    if not password:
        print("Error: password cannot be empty.")
        return

    report = checker.check(password)

    print("\n---------- ANALYSIS ----------")
    print(f"Strength       : {report['strength']}")
    print(f"Security score : {report['score']}/{report['max_score']}")

    print("\nChecks:")
    for name, passed in report["checks"]:
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}")

    if report["suggestions"]:
        print("\nSuggestions:")
        for item in report["suggestions"]:
            print(f"- {item}")


def show_menu():
    """Print the main menu."""
    print("\n==============================================")
    print("          RANDOM PASSWORD GENERATOR")
    print("==============================================")
    print("1. Generate random password")
    print("2. Check password strength")
    print("3. View session history")
    print("4. Exit")
    print("==============================================")


def main():
    """Start the application and keep it running until the user exits."""
    generator = PasswordGenerator()
    checker = PasswordStrengthChecker()
    history = SessionHistory()

    print("Welcome to the Random Password Generator!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            generate_password_workflow(generator, checker, history)
        elif choice == "2":
            check_password_workflow(checker)
        elif choice == "3":
            history.display()
        elif choice == "4":
            print("\nThank you for using the project.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
