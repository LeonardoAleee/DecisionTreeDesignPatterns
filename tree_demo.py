from tree_design import *

def build_sample_tree() -> DecisionNode:
    print("\n[demo] Construindo árvore de exemplo...")
    root = DecisionNode("root", splitting_feature = "feature_root")
    left = DecisionNode("left_decision", splitting_feature = "feature_left")
    right = DecisionNode("right_decision", splitting_feature = "feature_right")

    left.add_child(LeafNode("left_leaf_1", prediction = "class_A"))
    left.add_child(LeafNode("left_leaf_2", prediction = "class_2"))

    right.add_child(LeafNode("right_leaf_1", prediction = "class_3"))

    nested = DecisionNode("right_nested", splitting_feature = "feature_nested")
    nested.add_child(LeafNode("nested_leaf_1", prediction = "class_4"))
    nested.add_child(LeafNode("nested_leaf_2", prediction = "class_5"))
    right.add_child(nested)

    root.add_child(left)
    root.add_child(right)   
    return root

def demo_iterator(root):
    print("\n[demo] Iterando na árvore em pré-ordem com PreOrderIterator:")
    for node in PreOrderIterator(root):
        node_type = "Leaf" if node.is_leaf() else "Decision"
        print(f" -> [{node_type}] {node.name}")

def demo_visitors(root):
    print("\n[demo] Executando DepthVisitor:")
    depth_visitor = DepthVisitor()
    root.accept(depth_visitor)
    depth_visitor.result()

    print("\n[demo] Executando CountLeavesVisitor:")
    count_visitor = CountLeavesVisitor()
    root.accept(count_visitor)
    count_visitor.result()