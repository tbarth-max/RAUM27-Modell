"""Clean Nano-Container: elastic billiard inside [0, Q].

No coupling to any outer net. The result stays inside the binary frame.
"""

from __future__ import annotations

SHIFT = 40
Q_WALL = 1 << SHIFT
M_CENTER = 1 << (SHIFT - 1)


class Raum27NanoContainer:
    def __init__(self, x: int, y: int, z: int, vx: int, vy: int, vz: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def current_octant(self) -> int:
        bx = 1 if self.x >= M_CENTER else 0
        by = 1 if self.y >= M_CENTER else 0
        bz = 1 if self.z >= M_CENTER else 0
        return (bx << 2) | (by << 1) | bz

    def step(self) -> int:
        self.x = fold(self.x + self.vx)
        self.y = fold(self.y + self.vy)
        self.z = fold(self.z + self.vz)
        return self.current_octant()

    def reverse(self) -> None:
        self.vx = -self.vx
        self.vy = -self.vy
        self.vz = -self.vz


def fold(value: int) -> int:
    """Elastic reflection into [0, Q_WALL] by period 2*Q folding."""
    period = Q_WALL << 1
    value %= period
    if value < 0:
        value += period
    if value >= Q_WALL:
        value = period - value
    return value
