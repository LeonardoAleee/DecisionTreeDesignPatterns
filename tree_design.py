from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional, Any

#######################################################################
# Composite: Node, DecisionNode e LeafNode
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

#######################################################################
# Visitor: DepthVisitor e CountLeavesVisitor
#######################################################################

class Visitor(ABC):
    @abstractmethod
    def visit_decision(self, node: DecisionNode) -> None: ...

    @abstractmethod
    def visit_leaf(self, node: LeafNode) -> None: ...

class DepthVisitor(Visitor):
    def __init__(self) -> None:
        self._max_depth = 0
        self._current_depth = 0

    def visit_decision(self, node: DecisionNode) -> None:
        print(f'[Visitor] Visitando DecisionNode "{node.name}"')
        children = node.children()
        if not children:
            self._max_depth = max(self._max_depth, self._current_depth + 1)
            print(f'[DepthVisitor] Nó "{node.name}" é folha virtual, max_depth = {self._max_depth}')
            return
        for child in children:
            self._current_depth += 1
            child.accept(self)
            self._current_depth -= 1

    def visit_leaf(self, node: LeafNode) -> None:
        depth_here = self._current_depth + 1
        if depth_here > self._max_depth:
            self._max_depth = depth_here
        print(f'[DepthVisitor] Visitando Leaf "{node.name}" em profundidade {depth_here}')

    def result(self) -> int:
        print(f'[DepthVisitor] Profundidade máxima encontrada: {self._max_depth}')
        return self._max_depth
