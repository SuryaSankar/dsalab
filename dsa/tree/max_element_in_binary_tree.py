# Find maximum element in a binary tree
# Given a binary tree, find the maximum element in it.

# Example:
# Input:
#       1
#      / \
#     2   3
#    / \
#   4   5
# Output: 5

from .binary_tree import BinaryTree

def max_element_in_binary_tree(root: BinaryTree.Node) -> int:
    if root is None:
        return float('-inf')
    return max(max_element_in_binary_tree(root.left), root.value, max_element_in_binary_tree(root.right))


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
    assert max_element_in_binary_tree(binary_tree.root) == 5

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
    assert max_element_in_binary_tree(binary_tree.root) == 7
    
    print('All test cases passed successfully.')
