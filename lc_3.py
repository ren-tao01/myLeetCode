class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = list()
        count = 0
        highestCount = 0
        # using queue
        # n
        for e in s:
            while e in queue:
                queue.pop(0)
                count -= 1
            # q    
            if e not in queue:
                queue.append(e)
                count += 1
            
            if count > highestCount:
                highestCount = count
                
        # O(n*q); worst case = q is the length of the string s, best case q = 1, str = "aaaaa" 
        return highestCount

        