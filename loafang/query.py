import argparse
from typing import Callable
from typing import Generic
from typing import TypeVar


T = TypeVar('T')


def gen_arg_name(name: str) -> str:
    """
        adds double dashes as prefix

        name -> --name
        -name -> --name
    """

    return "--" + "-".join(i for i in name.split('-') if i)


class QueryBuilder(Generic[T]):

    def __init__(self, head: str) -> None:

        self._head = str(head)  # to be used during the final parsing

        self._inner_parser = argparse.ArgumentParser(add_help=False)
        self._inner_parser.add_argument(str(head), type=str)

    def add_argument(self, name: str, type: Callable[[str], T], default: T) -> None:
        self._inner_parser.add_argument(
            gen_arg_name(name), type=type, default=default)
