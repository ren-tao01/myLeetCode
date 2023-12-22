class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        rnge = len(s) // 2
        last = len(s) - 1
        for i in range(0, rnge):
            s[i], s[last - i] = s[last - i], s[i]