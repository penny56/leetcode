# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    @classmethod
    def arrToListNode(self, arr):
        head = ln = ListNode(0)

        for i in range(len(arr)):
            curr = ListNode(arr[i])
            ln.next = curr
            ln = ln.next
        return head.next
    
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        (l, ln, odd) = (1, head, True)
        while ln.next:
            l += 1
            ln = ln.next
        
        if l%2 == 0: odd = False

        (step, deep) = (0, l//2)
        stack = []
        ln = head
        while step != deep :
            stack.append(ln.val)
            step += 1
            ln = ln.next
        
        if odd: ln = ln.next

        while ln:
            if not stack: return False
            if ln.val != stack.pop(): return False
            ln = ln.next

        if len(stack) == 0:
            return True 
        else:
            return False


if __name__ == "__main__":
    sol = Solution()

    head = sol.arrToListNode([1])
 
    print(sol.isPalindrome(head))
