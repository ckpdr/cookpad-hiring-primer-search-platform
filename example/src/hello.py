import os
import sys
from pathlib import Path


def hello(name: str):
    virtualenv = os.getenv("VIRTUAL_ENV", None)

    try:
        virtualenv = str(Path(virtualenv).relative_to(Path.cwd()))
    except ValueError:
        pass

    print(f"Hello {name}!")
    print(f"You are using Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    if virtualenv:
        print(f"You have an activated virtual environment at '{virtualenv}/'")
    else:
        print(f"You do not have an activated virtual environment")
