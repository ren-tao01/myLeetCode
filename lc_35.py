import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # recursion
        pos = 0
        if not len(nums) <= 2:
            pos  = math.ceil(len (nums) / 2) - 1   
            
        if target == nums[pos]:
            return pos
        
        if len(nums) <= 2:
            for p in range(len(nums)):
                if target <= nums[p]:
                    return p
            return len(nums)
        
        if target < nums[pos]:
            new_arr = nums[:pos]
            return self.searchInsert(new_arr, target)
        
        if target > nums[pos]:
            new_arr = nums[pos:]
            pos += self.searchInsert(new_arr, target)
        
        return pos
          
        
        