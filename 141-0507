# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        (s, ln) = (set(), head)

        while ln:
            if ln not in s:
                s.add(ln)
            else:
                return True
            ln = ln.next
            
        return False
