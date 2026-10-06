# Builds a sorted linked list from the input, then removeDuplicates walks it and skips
# over any node whose value equals the next one before the list is displayed.

class Node:

    def __init__(self, data):

        self.data = data

        self.next = None

class Solution:

    def insert(self, head, data):

        p = Node(data)

        if head == None:

            head = p

        else:

            current = head

            while current.next != None:

                current = current.next

            current.next = p

        return head

    def removeDuplicates(self, head):
        if head is None:
            return head

        current = head

        while current is not None and current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def display(self, head):
        current = head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

mylist = Solution()
T = int(input())
head = None
for _ in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)