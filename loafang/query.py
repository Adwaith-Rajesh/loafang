import argparse
from typing import Any
from typing import Callable
from typing import NoReturn


def gen_arg_name(name: str) -> str:
    """
        adds double dashes as prefix

        name -> --name
        -name -> --name
    """

    return "--" + "-".join(i for i in name.split('-') if i)


class QueryBuilderError(Exception):

    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return self.msg


class CArgumentParser(argparse.ArgumentParser):

    def error(self, message: str) -> NoReturn:
        raise QueryBuilderError(message)


class QueryBuilder:

    # the reason why this class is not inheriting from the argparse.ArgumentParser,
    # is so that the methods given to the user can be limited.

    def __init__(self, head: str) -> None:

        self._head = str(head)  # to be used during the final parsing

        self._inner_parser = CArgumentParser(add_help=False)
        self._inner_parser.add_argument(str(head), type=str)

    def add_argument(self, name: str, type: Callable[[str], Any], default: Any = None) -> None:
        self._inner_parser.add_argument(
            gen_arg_name(name), type=type, default=default)
