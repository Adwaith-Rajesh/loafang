import pytest

from loafang.query import gen_arg_name


@pytest.mark.parametrize(
    'input,output',
    (
        ("name", "--name"),
        ("-name", "--name"),
        ("---name", "--name"),
        ("c42", "--c42"),
        ("42", "--42"),

    )
)
def test_gen_arg_name(input, output):
    assert gen_arg_name(input) == output
