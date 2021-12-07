'''
Created on Dec 7, 2021

1. (val1, val2) = (1, 2)

@author: mayijie
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        (head, carry) = (l1, 0)

        while l1 != None and l2 != None:
            if l1.val + l2.val + carry >= 10:
                l1.val = int((l1.val + l2.val + carry) % 10)
                carry = 1
            else:
                l1.val = l1.val + l2.val + carry
                carry = 0
            (t1, l1, l2) = (l1, l1.next, l2.next)

        if l1 == None and l2 != None:
            (l1, t1.next) = (l2, l2)
            # 这里记得要考虑上一个l1最高一位的carry
            if l1.val + carry == 10:
                l1.val = 0
            else:
                l1.val += carry
                # carry已使用，记得reset
                carry = 0
            (t1, l1) = (l1, l1.next)            
        
        while l1 != None and carry == 1:
            if l1.val + carry == 10:
                (l1.val, t1, l1) = (0, l1, l1.next)
            else:
                l1.val += 1
                break     

        if l1 == None and carry == 1:
            t1.next = ListNode(1)

        return head



if __name__ == "__main__":
    sol = Solution()

    #n13 = ListNode(9)
    n12 = ListNode(6)
    n11 = ListNode(8, n12)
    l1 = n11

    #n24 = ListNode(9)
    n23 = ListNode(8)
    n22 = ListNode(4, n23)
    n21 = ListNode(6, n22)
    l2 = n21

    res = sol.addTwoNumbers(l1, l2)
    while res.next != None:
        print (res.val)
        res = res.next
    print (res.val)