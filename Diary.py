from dataclasses import dataclass
from User import User

@dataclass(frozen=True)
class Diary:
    id: int
    user: User
    name: str
    dish: str