from pathlib import Path

PROJECT_DIR       = Path(__file__).parents[3].resolve()

INPUT             = PROJECT_DIR / 'input'
OUTPUT            = PROJECT_DIR / 'output'
QUERIES_DIR       = PROJECT_DIR / 'queries'
REPORTS_DIR       = PROJECT_DIR / 'reports'
WORKING_DIR       = PROJECT_DIR / 'working'

COMPETITION_INPUT = INPUT / '{{ cookiecutter.repo_name }}'
