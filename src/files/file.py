from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int  # bytes
