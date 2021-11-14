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


@pytest.mark.parametrize(
    'input,output',
    (
        ("get", (None, 603, "Missing ID.")),
        ("GETS", (None, 603, "Missing ID.")),
        ("GETS:test-id", (None, 601, "The method 'GETS' does not exists.")),
        ("get:test-id", (None, 601, "The method 'get' does not exists.")),
        ("", (None, 600, "The header cannot be empty.")),
        ("GET:id:pe:test", (None, 600, "The header cannot be more than 3 parts.")),
        ("GET:id:p4", (None, 602, "The property key 'p4' does not exists.")),
    )
)
def test_header_parser_error(input, output):
    assert HeaderParser(input).parse() == output
