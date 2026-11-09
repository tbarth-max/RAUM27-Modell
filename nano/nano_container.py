"""Clean Nano-Container: elastic billiard inside [0, Q].

No coupling to any outer net. The result stays inside the binary frame.

Reflection is exact: each axis keeps an unfolded integer coordinate.
Position and velocity sign are derived from it, so the wall reverses
the direction without a separate flip that can be forgotten.
"""

from __future__ import annotations

SHIFT = 40
Q_WALL = 1 << SHIFT
M_CENTER = 1 << (SHIFT - 1)
PERIOD = Q_WALL << 1


class Raum27NanoContainer:
    def __init__(self, x: int, y: int, z: int, vx: int, vy: int, vz: int) -> None:
        self._ux = x
        self._uy = y
        self._uz = z
        self._vx = vx
        self._vy = vy
        self._vz = vz

    @property
    def x(self) -> int:
        return fold_position(self._ux)

    @property
    def y(self) -> int:
        return fold_position(self._uy)

    @property
    def z(self) -> int:
        return fold_position(self._uz)

    @property
    def vx(self) -> int:
        return self._vx * fold_sign(self._ux)

    @property
    def vy(self) -> int:
        return self._vy * fold_sign(self._uy)

    @property
    def vz(self) -> int:
        return self._vz * fold_sign(self._uz)

    def current_octant(self) -> int:
        bx = 1 if self.x >= M_CENTER else 0
        by = 1 if self.y >= M_CENTER else 0
        bz = 1 if self.z >= M_CENTER else 0
        return (bx << 2) | (by << 1) | bz

    def step(self) -> int:
        self._ux += self._vx
        self._uy += self._vy
        self._uz += self._vz
        return self.current_octant()

    def reverse(self) -> None:
        self._ux += self._vx
        self._uy += self._vy
        self._uz += self._vz
        self._vx = -self._vx
        self._vy = -self._vy
        self._vz = -self._vz


def fold_position(value: int) -> int:
    value %= PERIOD
    if value < 0:
        value += PERIOD
    if value >= Q_WALL:
        value = PERIOD - value
    return value


def fold_sign(value: int) -> int:
    value %= PERIOD
    if value < 0:
        value += PERIOD
    return -1 if value >= Q_WALL else 1
