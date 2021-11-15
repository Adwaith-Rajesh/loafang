from typing import Any
from typing import Dict
from typing import List
from typing import Union

from .methods import Methods

dataType = Dict[str, Dict[str, Union[List[str], Dict[str, Any], str]]]


def verify_data_type(data: object) -> bool:
    # I'll implement this later
    return True


def parse(methods: Methods, data: object) -> None:

    if verify_data_type(data):
        pass
