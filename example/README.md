# Example Python project

This directory contains an example "Hello, world" Python project. Use it to check that you can run Python code.

## Instructions

### 1. Ensure you are using Python 3.9

See [PREREQUISITES.md](../PREREQUISITES.md) for instructions.

### 2. Create and activate a virtual environment

Create a [virtual environment](https://docs.python.org/3/library/venv.html):

```shell
python -m venv .venv
```

> :information_source: This will create an isolated copy of a Python installation in the directory `.venv/`

Activate the virtual environment:

```shell
source .venv/bin/activate
```

> :information_source: This will modify the _current shell session_ to use the virtual environment. Whilst activated, packages you install will be installed here rather than on your system Python installation. Run `deactivate` at any time to deactivate the virtual environment.

### 3. Install dependencies

Install dependencies specified in [requirements.txt](./requirements.txt):

```shell
pip install -r requirements.txt
```

### 4. Run the program


You can execute the Python program as follows:

```shell
PYTHONPATH=src python -m main --name=$(whoami)
```

> :information_source: The `PYTHONPATH` environment variable allows Python to discover the modules found in [src/](./src).

You should see output as follows:

```
Hello <YOUR_NAME_HERE>!
You are using Python 3.9.7
You have an activated virtual environment at '.venv/'
```

> :warning: If you see an error, a different Python version, or no activated virtual environment, its likely you missed one of the steps above.
