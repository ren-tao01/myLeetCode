from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s).most_common()
        '''
        c = [{}, {}, {}]
        '''
        res = ""
        if len(c) <= 1 and len(s)>1:
            return ""
        sameSize = False
        while not sameSize:
            if len(c) <= 1:
                sameSize = True
                break
            ch0, cnt0 = c[0]
            ch1, cnt1 = c[1]
            ch2, cnt2 = '', 0
            if len(c) > 2:
                ch2, cnt2 = c[2]
            cutCnt0 = cnt0 - cnt2
            print("cnt0 = ", cnt0)
            print("cnt1 = ", cnt1)
            print("cutCnt0 = ", cutCnt0)
 
            if cutCnt0 > cnt1 +1 and cnt2 == 0:
                return ""

            if cutCnt0 <= cnt1:
                print("Samesize")
                res += (ch0 + ch1) * cutCnt0
                print("res: ", res)
                cnt0 -= cutCnt0
                c[0] = (ch0, cnt0)
                cnt1 -= cutCnt0
                c[1] = (ch1, cnt1)
                if cnt1 == 0:
                    c.pop(1)
                sameSize = True
                continue

            if cutCnt0 >= cnt1:
                print("cutcnt0 >= cnt1")
                res += (ch0 + ch1) * cnt1
                cnt0 -= cnt1
                c[0] = (ch0, cnt0)
                print("Res: ", res)
                c.pop(1)
        # end while loop

        ch0, cnt0 = c[0]
        toAdd = ch0
        print("Res:" , res)
        pointer = 1
        csize = len(c)
        for i in range(0, cnt0):
            n = cnt0 - i
            print("n: ", n)
            t = 0
            for p in range(pointer, csize):
                ch, cnt = c[p]
                print(ch, cnt)
                if not cnt == n:
                    continue
                if cnt == n and not ch in toAdd:
                    toAdd += ch
                    
            print("length c = ", len(c))
            print(c)
            if not len(toAdd) == 1:
                res += toAdd
            if len(toAdd) == 1 and len(c) == 1:
                res += toAdd
            print("Res:" , res)  

        print(res)
        return res
        
