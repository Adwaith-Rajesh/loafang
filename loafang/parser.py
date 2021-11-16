from pprint import pprint
from typing import Any
from typing import Dict
from typing import List
from typing import Union

from ._parsers import BlockParser
from .methods import Methods


dataType = Dict[str, Dict[str, Union[List[str], Dict[str, Any], str]]]


def verify_data_type(data: object) -> dataType:
    # I'll implement this later
    if isinstance(data, dict):
        return data

    return dict()


def parse(methods: Methods, data: object) -> None:

    methods_dict = {
        "GET": methods.get_query_parser,
        "POST": methods.post_query_parser,
        "PUT": methods.put_query_parser,
        "PATCH": methods.patch_query_parser,
        "DELETE": methods.delete_query_parser,
    }

    data = verify_data_type(data)

    if data:
        for k, v in data.items():
            eb = BlockParser({k: v}, methods_dict).parse()
            pprint(eb)
