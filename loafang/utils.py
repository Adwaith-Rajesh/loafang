from typing import List

from ._const import ERROR_CODES
from ._const import METHODS
from .methods import Methods
from .query import QueryBuilder


def err_msg(code: int) -> str:
    return ERROR_CODES.get(code, "")


def map_parser(methods: Methods, parser: QueryBuilder, apply_to: List[str] = []) -> Methods:
    if not apply_to:
        apply_to = [i.lower() for i in METHODS]

    else:
        apply_to = [i.lower() for i in apply_to if i.upper() in METHODS]
        others = [i.lower() for i in METHODS if i.lower() not in apply_to]

    for i in apply_to:
        setattr(methods, f"{i}_query_parser", parser)

    for o in others:
        setattr(methods, f"{o}_query_parser", None)

    return methods
