import sys

from fire import Fire

from hello import hello


def main(name: str = "world"):
    hello(name)


if __name__ == "__main__":
    Fire(main)
