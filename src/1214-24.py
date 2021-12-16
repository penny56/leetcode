'''
Created on Dec 14, 2021

1. 参考题解中的把链表分成两个的方案。

@author: mayijie
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: return head
        (odd, oddCurr, even, evenCurr) = (head, head, head.next, head.next)
        while head.next != None:
            head = head.next.next
            oddCurr.next = head
            oddCurr = oddCurr.next
            if head == None: 
                break
            else:
                evenCurr.next = head.next
                evenCurr = evenCurr.next
        
        # Do the exchange
        (head, evenCurr, oddCurr) = (even, even, odd)
        while True:
            evenCurr = even.next
            even.next = oddCurr
            oddCurr = odd.next
            if evenCurr != None:
                odd.next = evenCurr
                (odd, even) = (oddCurr, evenCurr) 
            else:
                break
        
        return head


if __name__ == "__main__":
    sol = Solution()
    e = ListNode('e')
    d = ListNode('d', e)
    c = ListNode('c', d)
    b = ListNode('b', c)
    a = ListNode('a', b)

    res = sol.swapPairs(a)
    if res == None:
        print("[]")
    else:
        while res != None:
            print (res.val)
            res = res.next