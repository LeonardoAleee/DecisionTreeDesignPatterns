from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional, Any

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

class LeafNode(Node):
    def __init__(self, name: str, prediction: Optional[Any] = None) -> None:
        super().__init__(name)
        self.prediction = prediction

    def is_leaf(self) -> bool:
        return True
    
    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_leaf(self)

#######################################################################
# Iterator: PreOrderIterator
#######################################################################

class PreOrderIterator:
    def __init__(self, root: Node) -> None:
        self._snapshot = []
        self._build_snapshot(root)
        self._index = 0
        print(f"[Iterator] Snapshot criado com {len(self._snapshot)} nós (pre-order).")

    def _build_snapshot(self, node: Node) -> None:
        self._snapshot.append(node)
        if isinstance(node, CompositeNode):
            for child in node.children():
                self._build_snapshot(child)

    def __iter__(self):
        return self
    
    def __next__(self) -> Node:
        if self._index >= len(self._snapshot):
            raise StopIteration
        node = self._snapshot[self._index]
        self._index += 1
        return node
