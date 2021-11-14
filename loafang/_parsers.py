from typing import Tuple
from typing import Union

from ._const import METHODS
from ._const import PROPERTY_KEYS
from ._dataclasses import Header


class HeaderParser:
    """
    This is whats called as the header of an 'execution block`
    GET:get-user:pe

    Here,
    GET      -> methods that the user likes to perform
    get-user -> An unique ID / name that represents the block
    pe       -> An optional key that determines the property of an execution block.

    """

    def __init__(self, header: str) -> None:
        self.header = header

    def parse(self) -> Union[Tuple[Header, None, None], Tuple[None, int, str]]:
        parts = [part for part in self.header.split(":") if part]
        rv = Header("", "", "")

        if len(parts) == 0:
            return (None, 600, "The header cannot be empty.")

        if len(parts) == 1:
            return (None, 603, "Missing ID.")

        if len(parts) > 3:
            return (None, 600, "The header cannot be more than 3 parts.")

        if len(parts) >= 2:
            if parts[0] in METHODS:
                rv.method = parts[0]
                rv.id = parts[1]
                rv.property_key = None

            else:
                return (None, 601, f"The method {parts[0]!r} does not exists.")
        if len(parts) == 3:
            if parts[2]:
                if parts[2] in PROPERTY_KEYS:
                    rv.property_key = parts[2]

                else:
                    return (None, 602, f"The property key {parts[2]!r} does not exists.")

        return (rv, None, None)


class QueryParser:
    pass
