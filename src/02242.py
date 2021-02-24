#-- coding:utf8 --

'''
Created on Feb 24, 2021

1. 链表的基本操作：
  - 创建一个head；一个ListNode ln，让 ln = head
  - 找到要链接的lnx
                1) ln.next = lnx
                2) lnx = lnx.next
                3) ln = ln.next
  - 返回： head.next

@author: mayijie
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        ln = head
        while l1 and l2:
            if l1.val < l2.val:
                ln.next = l1
                l1 = l1.next
            else:
                ln.next = l2
                l2 = l2.next
            ln = ln.next
        if l1: ln.next = l1
        if l2: ln.next = l2
        return head.next

if __name__ == "__main__":
    sol = Solution()
    n13 = ListNode(4)
    n12 = ListNode(2, n13)
    n11 = ListNode(1, n12)
    l1 = n11
    n23 = ListNode(4)
    n22 = ListNode(3, n23)
    n21 = ListNode(1, n22)
    l2 = n21
    res = sol.mergeTwoLists(l1, l2)
    print res