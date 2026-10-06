# insert recursively places values into a binary search tree. levelOrder prints the tree
# breadth-first by using a list as a queue of nodes still to visit.

class Node:

    def __init__(self, data):

        self.data = data

        self.left = None
        self.right = None

class Solution:

    def insert(self, root, data):

        if root == None:
            return Node(data)

        else:
            if data <= root.data:

                root.left = self.insert(root.left, data)

            if data > root.data:

                root.right = self.insert(root.right, data)

        return root

    def levelOrder(self, root):

        if root == None:
            return

        queue = []

        queue.append(root)

        while len(queue) > 0:

            current = queue.pop(0)

            print(current.data, end=" ")

            if current.left != None:

                queue.append(current.left)

            if current.right != None:

                queue.append(current.right)

T = int(input())

myTree = Solution()

root = None

for _ in range(T):

    data = int(input())

    root = myTree.insert(root, data)

myTree.levelOrder(root)