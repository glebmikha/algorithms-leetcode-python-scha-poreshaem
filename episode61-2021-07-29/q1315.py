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


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        level_order = self.printLevelOrder(root)
        answer = 0

        for i in range(len(level_order)):
            parent = (i - 1) // 2
            grandparent = (parent - 1) // 2

            print(level_order[i], parent, grandparent)

            if grandparent >= 0 and level_order[grandparent] != 'N' \
                    and level_order[grandparent] % 2 == 0:
                if level_order[i] != 'N':
                    answer += level_order[i]
        print(level_order)
        return answer

    def printLevelOrder(self, root):
        # Base Case
        if root is None:
            return

        # Create an empty queue
        # for level order traversal
        queue = []

        # Enqueue Root and initialize height
        queue.append(root)

        level_order = []

        while (len(queue) > 0):

            # Print front of queue and
            # remove it from queue
            # print(queue[0].val)
            if queue[0] == 'N':
                level_order.append('N')
                queue.pop(0)
                continue

            if queue[0].val is not None:
                level_order.append(queue[0].val)

            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)
            else:
                queue.append("N")

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
            else:
                queue.append("N")

        return level_order


if __name__ == '__main__':
    tree_repr = [50, 'N', 54, 98, 6, 'N', 'N', 'N', 34]
    root = buildTree(tree_repr)
    print_tree(root)
    print(Solution().sumEvenGrandparent(root))
