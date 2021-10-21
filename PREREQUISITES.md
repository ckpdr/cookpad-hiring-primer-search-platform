# Technical exercise prerequisites

Follow this guide to make sure that you have all the prerequisites needed for the exercise.

# Python

In the exercise you will encounter applications written in Python, and its important you are able to install dependencies and run the code.

> :information_source: Don't worry if you're unfamiliar with Python. You should be able to complete the task without an intimate understanding of Python source code - these instructions should cover everything you need to know.

## Install the correct Python version

Firstly, you will need to have Python 3.9 available on your machine - you can check this as follows:

```shell
$ python --version 
Python 3.9.x
```

If you see another version, we recommend that you use [pyenv](https://github.com/pyenv/pyenv) to install the correct version:

1. [Install pyenv](https://github.com/pyenv/pyenv#installation)
1. Run `pyenv install 3.9.7` (this can take a little while)

Once the desired version of Python is installed, you can activate it in a number of ways:

- Setting the `PYENV_VERSION` environment variable, e.g. `export PYENV_VERSION=3.9.7`
- Running `pyenv local 3.9.7` will add a `.python-version` file to the current directory, and any python invocations from that directory or its children will use the specified version.
- Running `pyenv global 3.9.7` will make the specified version the default for your entire machine.

## Prepare and run an example program

An example Python program can be found in [example/](./example). Follow the instructions in the [README](./example/README.md) for some practice creating virtual environments, installing dependencies, and running the code.
