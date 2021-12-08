'''
Created on Dec 7, 2021

1. Wrong Wrong Wrong, I mistook the order.

@author: mayijie
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodeToNum(self, nod: ListNode) -> int:
        res = 0
        if nod.val == 0:
            return 0
        while nod.next != None:
            res += nod.val
            res *= 10
            nod = nod.next
        res += nod.val
        return res
    
    def numToNode(self, num: int) -> ListNode:
        res = ListNode(0)
        if num == 0:
            return res
        while num != 0:
            b = num%10
            temp = ListNode(b, res)
            res = temp
            num = int(num/10)
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        return res

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        (n1, n2) = (0, 0)
        n1 = self.nodeToNum(l1)
        n2 = self.nodeToNum(l2)
        res = n1 + n2
        return self.numToNode(res)

if __name__ == "__main__":
    sol = Solution()

    n13 = ListNode(2)
    n12 = ListNode(1, n13)
    l1 = n12

    n23 = ListNode(4)
    n22 = ListNode(3, n23)
    l2 = n22

    res = sol.addTwoNumbers(l1, l2)
    while res.next != None:
        print (res.val)
        res = res.next
    print (res.val)