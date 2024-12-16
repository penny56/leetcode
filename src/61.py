# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head: return head
        (head, tail, length) = self.reverse(head)

        # print(f"head = {head}, tail = {tail}")

        tail.next = head

        cnt = k%length

        while cnt != 0:
            head = head.next
            tail = tail.next
            cnt -= 1
        
        tail.next = None

        head, tail, length = self.reverse(head)

        return head
        

    def reverse(self, head):
        stack = []
        cnt = 0
        while head:
            stack.append(head.val)
            head = head.next
            cnt += 1
        
        head = ListNode()
        prev = head
        while len(stack):
            curr = ListNode(stack.pop())
            prev.next = curr
            prev = curr

        return head.next, curr, cnt
            
        
                   



sol = Solution()
a5 = ListNode(5, None)
a4 = ListNode(4, a5)
a3 = ListNode(3, a4)
a2 = ListNode(2, a3)
head = ListNode(1, a2)

k = 2 

res = sol.rotateRight(head, k)

while res:
    print (res.val)
    res = res.next





