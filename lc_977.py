class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Precomputation
        neg_nums = list()
        pos_nums = list()
        
        for n in nums:
            if n < 0:
                m = n * n
                neg_nums.insert(0, m)
            
            if n >= 0:    
                pos_nums.append(n * n)

        sorted_res = list()
        for i in range(len(nums)):
            if len(neg_nums) == 0:
                sorted_res.extend(pos_nums)
                break
                
            if len(pos_nums) == 0:
                sorted_res.extend(neg_nums)
                break
            
            negN = neg_nums[0]
            posN = pos_nums[0]     
            if negN <= posN :
                sorted_res.append(negN)
                neg_nums.pop(0)
            else:
                sorted_res.append(posN)
                pos_nums.pop(0)   
        # end for loop
        return sorted_res
    
    # can be solve with 2 pointers(start and end)