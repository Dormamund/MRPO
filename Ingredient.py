from dataclasses import dataclass

@dataclass(frozen=True)
class Ingredient:
    name: str
