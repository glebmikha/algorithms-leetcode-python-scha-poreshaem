from collections import deque


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


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        self.inorder = []

        # O(n)
        def _inorder_traversal(node):
            if node is not None:
                _inorder_traversal(node.left)
                self.inorder.append(node)
                _inorder_traversal(node.right)

        _inorder_traversal(root)

        # O(n)
        n = len(self.inorder)
        cur = self.inorder[-1].val
        cumsum = [cur]
        for i in range(n - 2, -1, -1):
            cur = cur + self.inorder[i].val
            cumsum.append(cur)

        # O(n)
        for i, node in enumerate(self.inorder):
            node.val = node.val + cumsum[n - 1 - i]

        return root


if __name__ == '__main__':
    root_arr = [4, 1, 6, 0, 2, 5, 7, 'N', 'N', 'N', 3, 'N', 'N', 'N', 8]
    root = buildTree(root_arr)
    print_tree(root)
    print(Solution().bstToGst(root))
    print_tree(root)
