# 自分のコードを書き直す
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        while current is not None:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False

