from dataclasses import dataclass
from typing import List


@dataclass
class RowDataModel:
    """
    Data model representing a row from the programming languages table.
    """
    website: str
    frontend: List[str]
    backend: List[str]
    popularity: int
