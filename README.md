# Example of using Annotated to fetch the actual type at runtime

## Installation

```sh
poetry install
```

## Python

```sh
poetry run python main.py
```

Result (correct):

```
<app.type_a.TypeA object at 0x1055125b0>
<app.type_a.TypeA object at 0x1054b4e50>
```

## MyPy

```sh
poetry run mypy main.py
```

Output (incorrect, or at least undesired):

```
app/type_b.py:9: error: Name 'app' is not defined
Found 1 error in 1 file (checked 1 source file)
```
