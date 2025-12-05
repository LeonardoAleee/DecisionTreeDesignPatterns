from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional

#######################################################################
# Composite: Node, DecisionNode, LeafNode
#######################################################################

class Node(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self._parent: Optional[Node] = None

    @abstractmethod
    def is_leaf(self) -> bool: ...

    def set_parent(self, parent: Optional[Node]) -> None:
        self._parent = parent

    @abstractmethod
    def accept(self, visitor: "Visitor") -> None: ...