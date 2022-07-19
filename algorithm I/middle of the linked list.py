class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare = head   
        tortoise = head
        while hare and  hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            
        return tortoise