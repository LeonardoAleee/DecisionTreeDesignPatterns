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