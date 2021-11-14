import argparse  # noqa: F401
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    print("Hello World")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
