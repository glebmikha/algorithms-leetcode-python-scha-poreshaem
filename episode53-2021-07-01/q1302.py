from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:

    def get_max_depth(self, root):

        global max_depth

        max_depth = 0

        def _get_max_depth(node, level=0):
            global max_depth
            if node is not None:

                _get_max_depth(node.right, level=level + 1)
                if level > max_depth:
                    max_depth = level
                _get_max_depth(node.left, level=level + 1)

        _get_max_depth(root)

        return max_depth

    def deepestLeavesSum(self, root: TreeNode) -> int:
        global max_depth
        global sum_max_depth

        max_depth = self.get_max_depth(root)
        sum_max_depth = 0

        def _traverse(node, level=0):
            global max_depth
            global sum_max_depth

            if node is not None:

                _traverse(node.right, level=level + 1)
                if level == max_depth:
                    sum_max_depth = sum_max_depth + node.val
                _traverse(node.left, level=level + 1)

        _traverse(root)

        return sum_max_depth


# Function to Build Tree
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


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 'N', 6, 7, 'N', 'N', 'N', 'N', 8]
    nodes = [6, 7, 8, 2, 7, 1, 3, 9, 'N', 1, 4, 'N', 'N', 'N', 5]
    root = buildTree(nodes)

    print_tree(root)

    print(Solution().get_max_depth(root))
    print(Solution().deepestLeavesSum(root))
