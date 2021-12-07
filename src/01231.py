#-- coding:utf8 --

'''
Created on Jan 23, 2021

这道题是抄的标准答案中的迭代法（递归法依然没有学习。）
注意这里在每次更新prev.next之后，要 prev = prev.next

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
        
        prehead = ListNode(-1)
        
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        if l1 == None:
            prev.next = l2
        else:
            prev.next = l1
            
        return prehead.next
        

if __name__ == "__main__":
    
    l1 = ListNode()
    l12 = ListNode()
    l14 = ListNode()
    
    l1.val = 1
    l1.next = l12
    
    l12.val = 2
    l12.next = l14
    
    l14.val = 4
    l14.next = None
    
    l2 = ListNode()
    l23 = ListNode()
    l24 = ListNode()
    
    l2.val = 1
    l2.next = l23
    
    l23.val = 3
    l23.next = l24
    
    l24.val = 4
    l24.next = None
    
    sol = Solution()
    res = sol.mergeTwoLists(l1, l2)
    while res != None:
        print (res.val)
        res = res.next