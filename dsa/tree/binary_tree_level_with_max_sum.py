from .binary_tree import BinaryTree
from collections import deque

def level_with_max_sum(root: BinaryTree.Node) -> int:
    max_sum = 0
    max_sum_level = None
    queue = deque([root])
    level = 0
    while queue:
        level += 1
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if level_sum > max_sum:
            max_sum = level_sum
            max_sum_level = level
    return max_sum_level

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
    assert level_with_max_sum(binary_tree.root) == 3

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
    assert level_with_max_sum(binary_tree.root) == 3
