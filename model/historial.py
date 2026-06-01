from dataclasses import dataclass

@dataclass
class HistoryRecord:
    input_unit: str
    output_unit: str
    input_value: float
    output_value: float
    timestamp: str