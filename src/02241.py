#-- coding:utf8 --

'''
Created on Feb 24, 2021

1. 数组在指定index插入元素：list.insert(index, value)

@author: mayijie
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        res = []
        while len(l1)>0 and len(l2)>0:
            e1 = l1.pop(0)
            e2 = l2.pop(0)
            if e1 < e2:
                res.append(e1)
                l2.insert(0, e2)
            else:
                res.append(e2)
                l1.insert(0, e1)
        if len(l1) != 0: res.extend(l1)
        if len(l2) != 0: res.extend(l2)
        return res


if __name__ == "__main__":
    sol = Solution()
    res = sol.mergeTwoLists([], [0])
    print res