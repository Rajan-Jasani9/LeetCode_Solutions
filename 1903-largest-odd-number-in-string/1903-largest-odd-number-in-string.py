class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = "13579"
        i = len(num) - 1
        while num[i] not in odd and i >= 0:
            i -= 1
        if i < 0:
            return ""
        else:
            return num[:i+1]