from __future__ import annotations
from typing import Union, Any


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, float, int]) -> Any:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Union[Distance, float, int]) -> Any:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: [int, float]) -> Any:
        return Distance(self.km * other)

    def __truediv__(self, other: [int, float]) -> Any:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
