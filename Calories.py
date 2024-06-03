from dataclasses import dataclass, field

@dataclass(frozen=True)
class Calories:
    amount: float