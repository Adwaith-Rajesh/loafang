from argparse import Namespace
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union


@dataclass
class Header:
    method: str
    id: str
    property_key: Optional[str] = None


@dataclass
class ListQuery:
    # used when the method is get, delete
    args: Namespace
    contents: List[str] = field(default_factory=list)


@dataclass
class DictQuery:
    # used when the values passed for methods are key value pairs
    args: Namespace
    contents: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExecutionBlock:
    header: Header
    after: 'ExecutionBlock'
    query: List[Union[ListQuery, DictQuery]] = field(default_factory=list)
