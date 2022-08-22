class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutArr = list(s1)
        
        tempArr = permutArr.copy()
        usedPermutation = list()
        
        for w in s2:
            
            #TODO: Keep track of removed letters, keep the intersection letter
            if not w in tempArr:
                if w in usedPermutation:
                    x = usedPermutation.index(w)
                    tempArr.extend(usedPermutation[0:x])
                    usedPermutation = usedPermutation[(x + 1)::]
                    usedPermutation.append(w)
                else:
                    tempArr = permutArr.copy()
                    usedPermutation.clear()
                continue
                
            if w in tempArr:
                usedPermutation.append(w)
                tempArr.remove(w)
                
            if not tempArr:
                return True

        return False
                