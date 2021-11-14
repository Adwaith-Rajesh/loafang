import pytest

from loafang._dataclasses import Header
from loafang._parsers import HeaderParser


@pytest.mark.parametrize(
    'input,output',
    (
        ("GET:test-id:pe", (Header("GET", "test-id", "pe"), None, None)),
        ("GET:test-id:", (Header("GET", "test-id", None), None, None)),
        ("GET:test-id", (Header("GET", "test-id", None), None, None)),
        ("POST:add-user:", (Header("POST", "add-user", None), None, None)),
        ("DELETE:remove-mail", (Header("DELETE", "remove-mail", None), None, None)),
    )
)
def test_header_parser_pass(input, output):
    assert HeaderParser(input).parse() == output
