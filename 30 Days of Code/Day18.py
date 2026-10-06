# Pushes every character onto a stack and a queue, then compares the popped (last-in)
# and dequeued (first-in) characters for half the length to decide whether the word is a
# palindrome.

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop(0)

s = input()
l = len(s)
obj = Solution()

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

if isPalindrome == False:
    print(f"The word, {s}, is not a palindrome.")
else:
    print(f"The word, {s}, is a palindrome.")