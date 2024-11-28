# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        now_point = head
        done_point = set()

        while now_point is not None and now_point.next is not None:
            done_point.add(now_point)
            now_point = now_point.next
            if now_point in done_point:
                return True
    
        return False
