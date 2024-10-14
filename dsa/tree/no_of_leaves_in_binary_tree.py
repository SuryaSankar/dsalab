from .binary_tree import BinaryTree

def no_of_leaves_in_binary_tree(root: BinaryTree.Node) -> int:
    tree = BinaryTree(root)
    no_of_leaves = 0
    for node in tree.level_order_traverse_iterator():
        if node.left is None and node.right is None:
            no_of_leaves += 1
    return no_of_leaves

if __name__ == '__main__':
    # Example 1
    # Construct the binary tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = BinaryTree.Node(1)
    root.set_left(BinaryTree.Node(2))
    root.set_right(BinaryTree.Node(3))
    root.left.set_left(BinaryTree.Node(4))
    root.left.set_right(BinaryTree.Node(5))
    binary_tree = BinaryTree(root)
    assert no_of_leaves_in_binary_tree(binary_tree.root) == 3

    # Example 2
    # Construct the binary tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    #             \
    #              7
    root = BinaryTree.Node(1)
    root.set_left(BinaryTree.Node(2))
    root.set_right(BinaryTree.Node(3))
    root.left.set_left(BinaryTree.Node(4))
    root.left.set_right(BinaryTree.Node(5))
    root.right.set_right(BinaryTree.Node(6))
    root.right.right.set_right(BinaryTree.Node(7))
    binary_tree = BinaryTree(root)
    assert no_of_leaves_in_binary_tree(binary_tree.root) == 3
    print('All test cases pass')
