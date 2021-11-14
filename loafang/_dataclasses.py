from dataclasses import dataclass
from typing import Optional


@dataclass
class Header:
    method: str
    id: str
    property_key: Optional[str] = None
