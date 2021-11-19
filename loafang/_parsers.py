from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from ._const import METHODS
from ._const import PROPERTY_KEYS
from ._dataclasses import DictQuery
from ._dataclasses import ExecutionBlock
from ._dataclasses import Header
from ._dataclasses import ListQuery
from .query import QueryBuilder
from .utils import err_msg


blockType = Dict[str, Dict[str, Union[List[str], Dict[str, Any], str]]]
queryType = Dict[str, Union[List[str], Dict[str, Any], str]]
queryContentType = Union[ListQuery, DictQuery]


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
            return (None, 601, err_msg(601))

        if len(parts) == 1:
            return (None, 604, err_msg(604))

        if len(parts) > 3:
            return (None, 600, "The header cannot be more than 3 parts.")

        if len(parts) >= 2:
            if parts[0] in METHODS:
                rv.method = parts[0]
                rv.id = parts[1]
                rv.property_key = None

            else:
                return (None, 602, f"The method {parts[0]!r} does not exists.")
        if len(parts) == 3:
            if parts[2]:
                if parts[2] in PROPERTY_KEYS:
                    rv.property_key = parts[2]

                else:
                    return (None, 603, f"The property key {parts[2]!r} does not exists.")

        return (rv, None, None)


class QueryParser:

    def __init__(self, query: queryType, method: str, parser: QueryBuilder) -> None:
        self.query = query
        self.method = method
        self.parser = parser

    def parse(self) -> Union[Tuple[queryContentType, None, None], Tuple[None, int, str]]:

        args_str = list(self.query)[0]
        contents = list(self.query.values())[0]

        if self.method == "GET" or self.method == "DELETE":
            if not isinstance(contents, list):
                return (None, 606, "The content container type must be a list for GET and DELETE")

        else:
            if not isinstance(contents, dict):
                return (None, 606, "The content container type must be dict for POST, PUT, and PATCH")

        args, _ = self.parser._inner_parser.parse_known_args(args_str.split())

        if self.method in ["GET", "DELETE"]:
            if isinstance(contents, list):
                return (ListQuery(args=args, contents=contents, query=args_str), None, None)

        else:
            if isinstance(contents, dict):
                return (DictQuery(args=args, contents=contents, query=args_str), None, None)

        return (None, 600, err_msg(600))


class BlockParser:

    """
    Uses the other two parsers to parser the block
    """

    def __init__(self, block: blockType, methods_dict: Dict[str, Optional[QueryBuilder]]) -> None:
        self.block = block
        self.methods_dict = methods_dict

    def parse(self) -> Union[Tuple[ExecutionBlock, None, None], Tuple[None, int, str]]:
        header, err, msg = HeaderParser(list(self.block.keys())[0]).parse()

        if not header and err and msg:
            return (None, err, msg)

        queries = []
        after: Optional[str] = None

        if header:

            for q, c in list(self.block.values())[0].items():

                if q == "after":

                    if header.property_key != "pe":

                        if not isinstance(c, str):
                            return (None, 609, err_msg(609))

                        else:
                            after = c
                            continue
                    else:
                        return (None, 612, err_msg(612))

                curr_parser = self.methods_dict[header.method]

                if curr_parser:

                    query, err, msg = QueryParser(
                        {q: c}, header.method, curr_parser).parse()
                    if query:
                        queries.append(query)

                    else:
                        if err and msg:
                            return (None, err, msg)

                else:
                    return (None, 607, f"Parser does not exists for {header.method!r}")

            return (ExecutionBlock(header=header, after=after, query=queries), None, None)
        return (None, 600, err_msg(600))
