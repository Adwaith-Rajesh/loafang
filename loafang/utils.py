from ._const import ERROR_CODES


def err_msg(code: int) -> str:
    return ERROR_CODES.get(code, "")
