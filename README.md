# Random Password Generator

A small Python command-line project for generating random passwords and checking basic password strength.

I built the project around a few simple ideas: the user should be able to choose what goes into a password, invalid input should be handled without crashing the program, and the password generator should use Python's `secrets` module rather than the ordinary `random` module.

## What the program can do

- Generate a password from 4 to 128 characters.
- Let the user choose uppercase letters, lowercase letters, numbers, and symbols.
- Make sure each selected character group appears in the generated password.
- Check an existing password against a few straightforward strength rules.
- Show suggestions when a check is not met.
- Keep a history of passwords generated during the current run.
- Run a small `unittest` test suite.

The history is intentionally temporary. It is kept in memory and is gone when the program closes.

## Project layout

```text
Random_Password_Generator/
├── src/
│   ├── main.py
│   ├── password_generator.py
│   ├── password_strength.py
│   ├── validator.py
│   └── history_manager.py
├── tests/
│   └── test_project.py
├── docs/
│   ├── system_architecture.md
│   ├── workflow.md
│   ├── uml_diagrams.md
│   └── project_report.md
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Requirements

Python 3.9 or later is recommended. There are no third-party packages to install; the project uses the Python Standard Library.

## Run the program

From the project folder:

```bash
python src/main.py
```

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## How the code is divided

`main.py` handles the menu and talks to the other modules.

`password_generator.py` is responsible for creating the password. It uses `secrets.choice()` and `secrets.randbelow()` so that the random choices are suitable for security-related use.

`password_strength.py` checks length and character variety. The score is deliberately simple and transparent rather than pretending to be a full password-cracking estimator.

`validator.py` keeps input checking in one place.

`history_manager.py` stores generated passwords only for the current session.

## Security note

Generated passwords are displayed in the terminal and are kept in memory while the application is running. If the terminal output is being recorded, screenshotted, or shared, do not use those example passwords as real account credentials.

## GitHub

After adding your own repository URL, the usual commands are:

```bash
git init
git add .
git commit -m "Add random password generator project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Academic files

The `docs` folder contains the architecture, workflow, UML diagrams, and project report. The project statement and submission checklist are also included.
