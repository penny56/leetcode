# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ln = head
        ls = []
        index = 0
        while ln:
            if ln not in ls:
                ls.append(ln)
            else:
                return ln

            index += 1
            ln = ln.next
        
        return None
