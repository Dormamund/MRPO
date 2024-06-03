from dataclasses import dataclass, field

@dataclass(frozen=True)
class Macronutrients:
    protein: float
    fat: float
    carbs: float