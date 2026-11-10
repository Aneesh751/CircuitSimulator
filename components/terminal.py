from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from components.component import Component
    from circuit.wire import Wire

class Terminal:
    def __init__(self, component: Component, name: str, xOffset: int, yOffset: int):
        self.component = component
        self.name = name
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.wires: list[Wire] = []
