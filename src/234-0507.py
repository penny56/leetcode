# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 遍历listNode，放入stack
        # 从stack中pop() 与 pop(0)对比

        (ln, s) = (head, [])

        while ln:
            s.append(ln.val)
            ln = ln.next

        while len(s) > 1:
            a = s.pop()
            b = s.pop(0)

            if a != b: return False
        
        return True
