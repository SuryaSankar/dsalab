from .binary_tree import BinaryTree
from typing import List

def _all_paths_binary_tree(root: BinaryTree.Node) -> List[List[int]]:
    if root.left is None and root.right is None:
       return [[root.value]]
    left_result = []
    right_result = []
    if root.left:
        left_result = _all_paths_binary_tree(root.left)
        for path_list in left_result:
           path_list.append(root.value)
    if root.right:
        right_result = _all_paths_binary_tree(root.right)
        for path_list in right_result:
            path_list.append(root.value)
    result = left_result + right_result
    return result

def all_paths_binary_tree(root: BinaryTree.Node) -> List[List[int]]:
    return [list(reversed(path_list)) for path_list in _all_paths_binary_tree(root)]

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
    assert all_paths_binary_tree(binary_tree.root) == [[1, 2, 4], [1, 2, 5], [1, 3]]

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
    assert all_paths_binary_tree(binary_tree.root) == [[1, 2, 4], [1, 2, 5], [1, 3, 6, 7]]
