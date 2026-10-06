# getHeight recursively measures a binary search tree by taking the taller of the left
# and right subtrees and adding one, with an empty node counting as -1.

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:

    def getHeight(self,root):
        if root == None:

            return -1

        left_height = self.getHeight(root.left)

        right_height = self.getHeight(root.right)

        return max(left_height, right_height) + 1

myTree = Solution()
test_root = Node(3)
test_root.left = Node(2)
test_root.left.left = Node(1)
test_root.right = Node(5)
test_root.right.left = Node(4)
test_root.right.right = Node(6)
test_root.right.right.right = Node(7)

print(f"Height of the tree: {myTree.getHeight(test_root)}")