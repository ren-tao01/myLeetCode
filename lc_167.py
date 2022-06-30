class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSize = len(numbers)
        found = False
        res = list()
        # TODO: Two pointer solution, at start and end == done
        # TODO: Dynamic programming, keeping track the previous number
        numsArr = list()
        for x in range(0, numSize // 2):
            lastPos = numSize - 1 - x
            lastNum = numbers[lastPos]
            thisArr = [numbers[x], lastNum]
            if thisArr in numsArr:
                continue
            # print(numsArr)
            if numbers[x] + lastNum == target:
                res.append(x + 1)
                res.append(lastPos + 1)
                return res
            
            numsArr.append(thisArr)
            for y in range((x + 1), lastPos):
                if numbers[x] + numbers[y] == target:
                    res.append(x + 1)
                    res.append(y + 1)
                    found = True
                    break
                if numbers[lastPos] + numbers[y] == target:
                    res.append(y + 1)
                    res.append(lastPos + 1)
                    found = True
                    break
                    
            if found:
                break
                
        return res
                  
            
                    