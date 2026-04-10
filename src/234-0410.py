# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        s = []
        ln = head
        while ln:
            s.append(ln)
            ln = ln.next

        (i, j) = (0, len(s)-1)

        while j-i >= 1:
            if s[i].val != s[j].val: return False
            i += 1
            j -= 1

        
        return True
