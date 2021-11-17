from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

from ._const import METHODS
from ._dataclasses import ExecutionBlock
from ._dataclasses import ParserState
from ._parsers import BlockParser
from .methods import Methods


dataType = Dict[str, Dict[str, Union[List[str], Dict[str, Any], str]]]
returnDataType = Dict[str, Dict[str, Any]]  # I'm not sure about this
parserReturnType = Union[Tuple[returnDataType,
                               None, None], Tuple[None, int, str]]


def verify_data_type(data: object) -> dataType:
    # I'll implement this later
    if isinstance(data, dict):
        return data

    return dict()


def block_executor(ebs: List[ExecutionBlock], pes: List[ExecutionBlock], methods: Methods) -> parserReturnType:

    pes_ids = {i.header.id: i for i in pes}
    req_methods_dict = {i: getattr(methods, i.lower()) for i in METHODS}

    def block_output(block: ExecutionBlock) -> Any:

        q_data = {}

        for q in block.query:
            q_data[q.query] = req_methods_dict[block.header.method](
                q.args, q.contents)

        if block.after:
            q_data["after"] = block_output(pes_ids[block.after])

        return q_data

    temp_data = {}

    for eb in ebs:
        if eb.after:
            if eb.after not in pes_ids:
                return (None, 609,
                        f"The 'after' execution block {eb.after!r} does not exists for the block {eb.header.id!r}")

        temp_data[eb.header.id] = block_output(eb)

    return (temp_data, None, None)


def parse(methods: Methods, data: object) -> parserReturnType:

    curr_state = ParserState()

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

            eb, err, msg = BlockParser({k: v}, methods_dict).parse()

            if eb:
                if eb.header.id in curr_state.ids:
                    return (None, 607, "Two execution blocks cannot have the same ID")
                else:
                    curr_state.ids.append(eb.header.id)

                    if eb.header.property_key == "pe":
                        curr_state.pes.append(eb)

                    else:
                        curr_state.ebs.append(eb)
            else:
                if err and msg:
                    return (None, err, msg)

        return block_executor(ebs=curr_state.ebs, pes=curr_state.pes, methods=methods)

    return (None, 600, "Invalid Data")
