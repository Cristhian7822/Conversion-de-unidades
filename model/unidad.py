from dataclasses import dataclass

@dataclass
class Unit:
    name: str
    symbol: str
    category: str
    factor: float