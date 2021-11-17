import pytest

from loafang.methods import Methods
from loafang.query import QueryBuilder
from loafang.utils import err_msg
from loafang.utils import map_parser


@pytest.fixture()
def query_builder():
    query = QueryBuilder("database")
    query.add_argument("name", type=str, default="users")


@pytest.fixture()
def methods():

    class MyMethods(Methods):

        def __init__(self) -> None:
            pass

        def get(self, args, content):
            return super().get(args, content)

        def post(self, args, content):
            return super().post(args, content)

        def put(self, args, content):
            return super().put(args, content)

        def delete(self, args, contents):
            return super().delete(args, contents)

        def patch(self, args, content):
            return super().patch(args, content)

    return MyMethods


@pytest.mark.parametrize(
    ("input", "output"),
    (
        (600, "Something went wrong."),
        (605, "Invalid data type for the argument in the query."),
        (612, ""),
        (500, "")
    )
)
def test_err_msg(input, output):
    assert err_msg(input) == output


def test_map_parser_all(methods, query_builder):
    map_parser(methods, query_builder, apply_to=[])

    assert hasattr(methods, "get_query_parser")
    assert hasattr(methods, "post_query_parser")
    assert hasattr(methods, "put_query_parser")
    assert hasattr(methods, "delete_query_parser")
    assert hasattr(methods, "patch_query_parser")

    assert methods.get_query_parser == query_builder
    assert methods.post_query_parser == query_builder
    assert methods.put_query_parser == query_builder
    assert methods.delete_query_parser == query_builder
    assert methods.patch_query_parser == query_builder


def test_map_parser_some_intialized(methods, query_builder):
    map_parser(methods, query_builder, apply_to=["get", "put", "delete"])

    assert hasattr(methods, "get_query_parser")
    assert hasattr(methods, "post_query_parser")
    assert hasattr(methods, "put_query_parser")
    assert hasattr(methods, "delete_query_parser")
    assert hasattr(methods, "patch_query_parser")

    assert methods.get_query_parser == query_builder
    assert methods.post_query_parser is None
    assert methods.put_query_parser == query_builder
    assert methods.delete_query_parser == query_builder
    assert methods.patch_query_parser is None
