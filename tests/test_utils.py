import pytest

from loafang.utils import err_msg


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
