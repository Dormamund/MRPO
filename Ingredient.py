from dataclasses import dataclass, field

@dataclass(frozen=True)
class Ingredient:
    ingredient_id: int
    name: str