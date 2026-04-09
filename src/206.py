# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        s = []
        res = ListNode()
        (ln, pre) = (head, head)
        while ln:
            s.append(ln)
            ln = ln.next
        

        first = True
        while s:
            ln = s.pop()

            if first:
                res.next = ln
                pre = ln
                first = False
            else:
                pre.next = ln
                pre = pre.next
        
        pre.next = None
        
        return res.next
                
