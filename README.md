# Simple CLI Calculator

This is a simple command-line interface (CLI) calculator built in Python.

## Features

It supports the following basic operations:
- Addition (`add`)
- Subtraction (`subtract`)
- Multiplication (`multiply`)
- Division (`divide`)

## Project Structure

The project has a beautified file structure as shown below:

```
.
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── calculator.py
│   └── main.py
└── tests
    ├── __init__.py
    └── test_calculator.py
```

## How to Run

You can run the calculator using the CLI:

```bash
python -m src.main <operation> <a> <b>
```

### Examples

**Addition:**
```bash
python -m src.main add 5 3
# Output: Result: 8.0
```

**Subtraction:**
```bash
python -m src.main subtract 10 4
# Output: Result: 6.0
```

**Multiplication:**
```bash
python -m src.main multiply 3 4
# Output: Result: 12.0
```

**Division:**
```bash
python -m src.main divide 10 2
# Output: Result: 5.0
```

## Running Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover tests
```
