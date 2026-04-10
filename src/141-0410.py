# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        ln = head
        while ln:
            if ln in s:
                return True
            else:
                s.add(ln)
            ln = ln.next
        
        return False
