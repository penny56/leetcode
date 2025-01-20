# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        stack = []
        ln = head
        while ln:
            stack.append(ln.val)
            ln = ln.next
        
        half = len(stack)//2

        while half != 0:
            tail = stack.pop()
            if head.val != tail:
                return False
            head = head.next
            half -= 1
        
        return True
    
    @classmethod
    def arrToLinkNode(self, arr):
        head = ListNode()
        prev = head
        for elem in arr:
            ln = ListNode(elem)
            prev.next = ln
            prev = prev.next

        return head.next


sol = Solution()

arr = [1,2]

head = sol.arrToLinkNode(arr)

res = sol.isPalindrome(head)

print(f"{res}")