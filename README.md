# QA Automation Engineer – Test Assignment #1 (V. Kazarin)

## Project Structure

```
 ├── checkers
 │   └── popularity_checker.py      # Functions to perform various checks
 ├── helpers
 │   ├── base_helper.py             # Utility functions for data processing
 │   └── table_helper.py            # Helpers for working with the website's table
 ├── models
 │   └── row_data_model.py          # Data model representing a table row
 ├── test_popularity.py             # Test file for popularity checks
 ├── conftest.py                    # Test fixtures
 └── README.md
```

## Running the Tests

1. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Install the dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the tests**

```bash
pytest --alluredir=allure-results
```

## Allure Report

1. **Install Allure**

```bash
brew install allure
```

1. **Run allure server**

```bash
allure serve allure-results
```