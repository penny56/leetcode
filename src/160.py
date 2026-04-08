# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 只想到最笨的方法，双循环，把headA的所有node让headB去试，看有没有被headB走到

        # search AI, 要利用好题目给的条件：保证整个link不存在环！
        # 1 找到tA, tB, 如果不等，return None
        
        # 1 遍历headA, 将node放进set
        # 2 遍历headB, 判断nodeB有没有在 set 中，如果遍历完都没有，就是无交点


        (lna, lnb) = (headA, headB)
        nodesA = set()
        while lna:
            nodesA.add(lna)
            lna = lna.next

        while lnb:
            if lnb in nodesA: return lnb
            lnb = lnb.next

        return None

