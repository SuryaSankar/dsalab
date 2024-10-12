from typing import Callable, Self
from collections import deque

class BinaryTree:

    class Node:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
        
        def set_left(self, node: Self):
            self.left = node

        def set_right(self, node: Self):
            self.right = node


    def __init__(self, node: Node):
        self.root = node

    def pre_order_traverse(self, func: Callable):
        func(self.root)
        if self.root.left:
            BinaryTree(self.root.left).pre_order_traverse(func)
        if self.root.right:
            BinaryTree(self.root.right).pre_order_traverse(func)

    def pre_order_traverse_iterative(self, func: Callable):
        stack = [self.root]
        while stack:
            node = stack.pop()
            func(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def post_order_traverse(self, func: Callable):
        if self.root.left:
            BinaryTree(self.root.left).post_order_traverse(func)
        if self.root.right:
            BinaryTree(self.root.right).post_order_traverse(func)
        func(self.root)

    def post_order_traverse_iterative(self, func: Callable):
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while result:
            func(result.pop())

    def in_order_traverse(self, func: Callable):
        if self.root.left:
            BinaryTree(self.root.left).in_order_traverse(func)
        func(self.root)
        if self.root.right:
            BinaryTree(self.root.right).in_order_traverse(func)
    
    def in_order_traverse_iterative(self, func: Callable):
        stack = []
        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                func(node)
                node = node.right

    def level_order_traverse(self, func: Callable):
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            func(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    @staticmethod
    def _build_tree_from_pre_order_in_order(pre_order: list, in_order: list, pre_order_index: int, in_order_start: int, in_order_end: int) -> Node:
        if in_order_start > in_order_end:
            return None
        node = BinaryTree.Node(pre_order[pre_order_index])
        in_order_index = in_order.index(pre_order[pre_order_index])
        node.left = BinaryTree._build_tree_from_pre_order_in_order(pre_order, in_order, pre_order_index+1, in_order_start, in_order_index-1)
        node.right = BinaryTree._build_tree_from_pre_order_in_order(pre_order, in_order, pre_order_index+in_order_index-in_order_start+1, in_order_index+1, in_order_end)
        return node

    @staticmethod
    def construct_from_pre_order_in_order(pre_order: list, in_order: list) -> Self:
        return BinaryTree(
            BinaryTree._build_tree_from_pre_order_in_order(pre_order, in_order, 0, 0, len(in_order)-1)
        )

if __name__ == '__main__':
    root = BinaryTree.Node(1)
    root.set_left(BinaryTree.Node(2))
    root.set_right(BinaryTree.Node(3))
    root.left.set_left(BinaryTree.Node(4))
    root.left.set_right(BinaryTree.Node(5))
    root.right.set_left(BinaryTree.Node(6))
    root.right.set_right(BinaryTree.Node(7))
    binary_tree = BinaryTree(root)
    print('Recursive Pre-order Traversal')
    binary_tree.pre_order_traverse(lambda node: print(node.value)) # 1 2 4 5 3 6 7
    print('Iterative Pre-order Traversal')
    binary_tree.pre_order_traverse_iterative(lambda node: print(node.value)) # 1 2 4 5 3 6 7
    print('Recursive Post-order Traversal')
    binary_tree.post_order_traverse(lambda node: print(node.value)) # 4 5 2 6 7 3 1
    print('Iterative Post-order Traversal')
    binary_tree.post_order_traverse_iterative(lambda node: print(node.value)) # 4 5 2 6 7 3 1
    print('Recursive In-order Traversal')
    binary_tree.in_order_traverse(lambda node: print(node.value)) # 4 2 5 1 6 3 7
    print('Iterative In-order Traversal')
    binary_tree.in_order_traverse_iterative(lambda node: print(node.value)) # 4 2 5 1 6 3 7
    print('Level-order Traversal')
    binary_tree.level_order_traverse(lambda node: print(node.value)) # 1 2 3 4 5 6 7