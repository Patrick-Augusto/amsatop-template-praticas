# MyHtop

A Python implementation of your own version of htop.

**Alumno:** Patrick Augusto Pinheiro da Silva

## 📦 Installing dependencies

Remember that, for the tests, we use a obscure feature of linux called [fuse (FileSystem on Userspace)](https://github.com/libfuse/libfuse). You don't have to understand what it does **but you have to
install it or the tests will not work**:

```bash
sudo apt update && sudo apt install libfuse2t64
```

## 🚀 Setting Up the Virtual Environment

Create and sync a virtual environment in the .venv folder:

```bash
uv sync
```

Activate the environment (if you have nushell or other type of shell, it will be different):
```bash
source .venv/bin/activate 
```


## ▶️ Running the Program
To run the myhtop program and see **all** the processes of your system, you may need sudo for system-level access:

```bash
uv run myhtop
```

## 🧪 Running Tests

### Run All Tests

```bash
uv run pytest
```

### Run Tests for a Specific Assignment
Replace x with the appropriate assignment number (1, 2, or 3):

```bash
uv run pytest test/prac_2_x
```

Examples:
```bash
uv run pytest test/prac_2_1
uv run pytest test/prac_2_2
uv run pytest test/prac_2_3
```

## 🧹 Linting the Code

To check your code for linting issues using ruff, run:
```bash
uv run ruff check
```
If any issues are found and you want to automatically fix them, run:
```bash
uv run ruff format
```
