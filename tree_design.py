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

class CompositeNode(Node):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: List[Node] = []

    def add_child(self, child: Node) -> None:
        child.set_parent(self)
        self._children.append(child)
        print(f'[Composite] Adicionando flho "{child.name}" a "{self.name}"')

    def remove_child(self, child: Node) -> None:
        self._children.remove(child)
        child.set_parent(None)
        print(f'[Composite] Removendo filho "{child.name}" de "{self.name}"')

    def children(self) -> List[Node]:
        return list(self._children)
    
    def is_leaf(self) -> bool:
        return False
    
    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_decision(self)

class DecisionNode(CompositeNode):
    def __init__(self, name: str, splitting_feature: Optional[str] = None) -> None:
        super().__init__(name)
        self.splitting_feature = splitting_feature