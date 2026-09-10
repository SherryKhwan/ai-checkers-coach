from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple


Square = Tuple[int, int]


@dataclass(frozen=True)
class Move:
    """Represents a single American checkers move.

    A move is defined by the starting and ending board coordinates, plus an
    optional captured piece position. This keeps the class intentionally small and
    easy for game logic to work with.
    """

    from_row: int
    from_col: int
    to_row: int
    to_col: int
    captured: Optional[Square] = None

    @classmethod
    def from_coords(
        cls,
        from_square: Square,
        to_square: Square,
        captured: Optional[Square] = None,
    ) -> "Move":
        """Create a move from two coordinate pairs."""
        from_row, from_col = from_square
        to_row, to_col = to_square
        return cls(
            from_row=from_row,
            from_col=from_col,
            to_row=to_row,
            to_col=to_col,
            captured=captured,
        )

    @property
    def from_square(self) -> Square:
        return (self.from_row, self.from_col)

    @property
    def to_square(self) -> Square:
        return (self.to_row, self.to_col)

    @property
    def is_capture(self) -> bool:
        return self.captured is not None

    @property
    def is_jump(self) -> bool:
        return self.is_capture

    @property
    def delta(self) -> Square:
        return (self.to_row - self.from_row, self.to_col - self.from_col)

    def __str__(self) -> str:
        return f"{self.from_square}->{self.to_square}"

    def __repr__(self) -> str:
        return (
            f"Move(from_row={self.from_row}, from_col={self.from_col}, "
            f"to_row={self.to_row}, to_col={self.to_col}, "
            f"captured={self.captured})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Move):
            return NotImplemented

        return (
            self.from_square == other.from_square
            and self.to_square == other.to_square
            and self.captured == other.captured
        )