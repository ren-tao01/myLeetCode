# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = head
        p2 = head.next
        while not p2 == None:
            p1 = p1.next
            if p2.next == None:
                p2 = p2.next
                continue
            p2 = p2.next.next
            
        print(p1)
        return p1
        