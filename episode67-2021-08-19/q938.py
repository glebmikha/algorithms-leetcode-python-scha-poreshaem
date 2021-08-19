from typing import Optional
from collections import deque
from math import floor


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# geeks for geeks
def buildTree(ip):
    # Create the root of the tree
    root = TreeNode(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = TreeNode(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = TreeNode(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level=level + 1)
        print(3 * ' ' * level + str(node.val))
        print_tree(node.left, level=level + 1)


def print_tree1(node):
    if node is not None:
        print_tree1(node.left)
        print(str(node.val))
        print_tree1(node.right)


class Solution:

    def __init__(self):
        self.sum_range = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.sum_range = 0

        def _inorder_traversal(node):
            if node is not None:
                _inorder_traversal(node.left)
                if low <= node.val <= high:
                    self.sum_range += node.val
                _inorder_traversal(node.right)

        _inorder_traversal(root)
        return self.sum_range


if __name__ == '__main__':
    tree_array = [10, 5, 15, 3, 7, 'N', 18]
    low = 7
    high = 15
    root = buildTree(tree_array)
    print_tree(root)
    print(Solution().rangeSumBST(root, low, high))
