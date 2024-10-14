from .binary_tree import BinaryTree
from collections import deque

def height_of_binary_tree(root: BinaryTree.Node) -> int:
    if root is None:
        return 0
    return 1 + max(height_of_binary_tree(root.left), height_of_binary_tree(root.right))

# def height_of_binary_tree_iterative(root: BinaryTree.Node) -> int:
#     if root is None:
#         return 0
#     queue = [root]
#     height = 0
#     while queue:
#         height += 1
#         for _ in range(len(queue)):
#             node = queue.pop(0)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#     return height

def height_of_binary_tree_iterative(root: BinaryTree.Node) -> int:
        queue = deque([root])
        height = 0
        while queue:
             height += 1
             for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                     queue.append(node.right)
        return height
                



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
    assert height_of_binary_tree(binary_tree.root) == 3
    assert height_of_binary_tree_iterative(binary_tree.root) == 3

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
    assert height_of_binary_tree(binary_tree.root) == 4
    assert height_of_binary_tree_iterative(binary_tree.root) == 4
    
    print('All test cases passed successfully.')