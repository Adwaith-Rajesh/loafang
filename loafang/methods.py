from abc import ABC
from abc import abstractmethod
from argparse import Namespace
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .query import QueryBuilder


# this class is what is used to generate the output for the each query in the execution block
class Methods(ABC):

    @abstractmethod
    def __init__(self) -> None:
        self.get_query_parser: Optional[QueryBuilder] = None
        self.post_query_parser: Optional[QueryBuilder] = None
        self.put_query_parser: Optional[QueryBuilder] = None
        self.delete_query_parser: Optional[QueryBuilder] = None
        self.patch_query_parser: Optional[QueryBuilder] = None

    @abstractmethod
    def get(self, args: Namespace, content: List[str]) -> Any:
        return None

    @abstractmethod
    def post(self, args: Namespace, content: Dict[str, Any]) -> Any:
        return None

    @abstractmethod
    def put(self, args: Namespace, content: Dict[str, Any]) -> Any:
        return None

    @abstractmethod
    def delete(self, args: Namespace, contents: List[str]) -> Any:
        return None

    @abstractmethod
    def patch(self, args: Namespace, content: Dict[str, Any]) -> Any:
        return None
