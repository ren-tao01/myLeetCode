class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 2: IMPROVEMENT - USE A DICTIONARY
        # Pre-Computation
        numbers = {}
        for i in range(len(nums)):
            numbers.update({nums[i]: i})

        ans = []
        for i in range(len(nums)):
            m = target - nums[i]
            try:
                ind = numbers[m]
                if i == ind: continue
                ans.append(i)
                ans.append(ind)
                break
            except KeyError:
                continue
        
        return ans
        # Solution 1:
        # nums.sort()
        # print(nums)
        # ans = list()
        # for i in range(0, len(nums)-1):
        #     # n + m = target
        #     m = target - nums[i]
        #     # print(nums[i+1:])
        #     if m in nums[i+1:]:
        #         ans.append(i)
        #         j = nums[i+1:].index(m) + i+1
        #         ans.append(j)
        #         return ans
        
        # return ans
