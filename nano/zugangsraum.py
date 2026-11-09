"""Access-space checkpoint: state space vs access space.

Question: does the billiard give more than one independent entry
direction per octant, or only a different drawing of the same path?

An entry is the pair (octant, sign triple of velocity) at the moment
the trajectory enters that octant. If the same octant is reached with
more than one distinct sign triple, the access count is > 1.
"""

from __future__ import annotations

from collections import defaultdict

from nano_container import Raum27NanoContainer


def sign_triple(container: Raum27NanoContainer) -> tuple[int, int, int]:
    return (
        1 if container.vx >= 0 else -1,
        1 if container.vy >= 0 else -1,
        1 if container.vz >= 0 else -1,
    )


def measure_access(container: Raum27NanoContainer, steps: int) -> dict[int, set[tuple[int, int, int]]]:
    access: dict[int, set[tuple[int, int, int]]] = defaultdict(set)
    previous = container.current_octant()
    access[previous].add(sign_triple(container))
    for _ in range(steps):
        octant = container.step()
        if octant != previous:
            access[octant].add(sign_triple(container))
            previous = octant
    return access


def report(access: dict[int, set[tuple[int, int, int]]]) -> str:
    lines = ["octant | distinct entry directions | directions"]
    for octant in range(8):
        directions = sorted(access.get(octant, set()))
        lines.append(f"{octant:6d} | {len(directions):24d} | {directions}")
    max_access = max((len(v) for v in access.values()), default=0)
    lines.append("")
    if max_access > 1:
        lines.append(f"access space > state space: max {max_access} directions per octant")
    else:
        lines.append("access space = state space: each octant reached by one direction only")
    return "\n".join(lines)


if __name__ == "__main__":
    container = Raum27NanoContainer(
        x=649_755_813_888,
        y=299_755_813_888,
        z=599_755_813_888,
        vx=314_159_265_358,
        vy=271_828_182_845,
        vz=161_803_398_874,
    )
    print(report(measure_access(container, steps=100_000)))
