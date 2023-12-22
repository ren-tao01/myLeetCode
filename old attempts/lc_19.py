# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        nums = list()
        # p1 = pointer 1, follow p2 by n spaces
        for i in range(n):
            nums.append(p2.val)
            p2 = p2.next
            
        while not p2 == None:
            nums.append(p2.val)
            p1 = p1.next
            p2 = p2.next
        
        s = len(nums)
        nums.pop(s - n)
        if len(nums) == 0:
            return None
        lastN = len(nums) - 1
        res = ListNode(nums[lastN])
        for i in range(len(nums) - 1):
            res = ListNode(nums[lastN - 1 - i], res)

        print(res)
        return res
