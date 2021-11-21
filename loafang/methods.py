from argparse import Namespace
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .query import QueryBuilder


class MethodsError(Exception):

    def __init__(self, code: int = 614, msg: str = "Some error occurred") -> None:
        self.code = code
        self.msg = msg

    def __str__(self) -> str:
        return f"{self.code} {self.msg}"


# this class is what is used to generate the output for the each query in the execution block
class Methods:

    def __init__(self) -> None:
        self.get_query_parser: Optional[QueryBuilder] = None
        self.post_query_parser: Optional[QueryBuilder] = None
        self.put_query_parser: Optional[QueryBuilder] = None
        self.delete_query_parser: Optional[QueryBuilder] = None
        self.patch_query_parser: Optional[QueryBuilder] = None

    def get(self, args: Namespace, contents: List[str]) -> Any:
        raise NotImplementedError("GET is not implemented")

    def post(self, args: Namespace, contents: Dict[str, Any]) -> Any:
        raise NotImplementedError("POST is not implemented")

    def put(self, args: Namespace, contents: Dict[str, Any]) -> Any:
        raise NotImplementedError("PUT is not implemented")

    def delete(self, args: Namespace, contents: List[str]) -> Any:
        raise NotImplementedError("DELETE is not implemented")

    def patch(self, args: Namespace, contents: Dict[str, Any]) -> Any:
        raise NotImplementedError("PATCH is not implemented")
