from .binary_tree import BinaryTree
from typing import Any
from collections import deque

def delete_element_from_binary_tree(root: BinaryTree.Node, val: Any):
    deepest_node = root
    prev_node = None
    queue = deque([root])
    val_node = None
    last_node_direction = None
    while queue:
        prev_node = deepest_node
        node = queue.popleft()
        deepest_node = node
        if node.value == val:
            val_node = node
        if node.left:
            last_node_direction = 'left'
            queue.append(node.left)
        if node.right:
            last_node_direction = 'right'
            queue.append(node.right)
    val_node.value, deepest_node.value = deepest_node.value, val_node.value
    if last_node_direction == 'left':
        prev_node.left = None
    else:
        prev_node.right = None

    

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
    delete_element_from_binary_tree(binary_tree.root, 3)
    assert binary_tree.root.right is None
    assert binary_tree.root.left.right is None
    assert binary_tree.root.left.left.value == 4
    assert binary_tree.root.left.right.value == 5

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
    delete_element_from_binary_tree(binary_tree.root, 5)
    assert binary_tree.root.left.right is None
    assert binary_tree.root.left.left.value == 4
    assert binary_tree.root.right.right.right.value == 7

    print('All test cases passed successfully.')

    

    
