class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = k % len(nums)
        h = len(nums) - r
        tail_arr = nums[-r:]
        if not r == 0:
            tail_arr.extend(nums[:h])
        
        nums.clear()
        nums.extend(tail_arr)